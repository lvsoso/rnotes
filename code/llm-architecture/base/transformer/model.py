#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
作者: Zhuanz
日期: 2026-02-23
依赖版本: torch>=2.0, python>=3.9
运行示例:
    单元测试:
        python -m transformer.model

本文件实现完整的 Encoder-Decoder Transformer 结构，
遵循《Attention Is All You Need》论文的模块拆分，
在保持结构一致的前提下适当收缩维度以控制参数量，
方便在单卡 8GB GPU 上进行机器翻译实验。
"""

import math
import time
from typing import Optional, Tuple

import torch
import torch.nn as nn
import torch.nn.functional as F


class PositionalEncoding(nn.Module):
    """
    位置编码模块: 用确定性三角函数为不同位置注入先验位置信息，
    这样模型即便完全基于自注意力也能区分 token 的先后顺序。
    """

    def __init__(self, d_model: int, dropout: float = 0.1, max_len: int = 5000) -> None:
        super().__init__()
        self.dropout = nn.Dropout(p=dropout)

        # 使用论文中的 sin/cos 封闭形式构造预计算表，避免每次前向反复计算
        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float32).unsqueeze(1)
        div_term = torch.exp(
            torch.arange(0, d_model, 2, dtype=torch.float32)
            * (-math.log(10000.0) / d_model)
        )
        pe[:, 0::2] = torch.sin(position * div_term)
        pe[:, 1::2] = torch.cos(position * div_term)
        pe = pe.unsqueeze(0)
        self.register_buffer("pe", pe)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # 将预计算的位置编码裁剪到当前序列长度并相加，保持张量形状不变
        x = x + self.pe[:, : x.size(1)]
        return self.dropout(x)


class MultiHeadAttention(nn.Module):
    """
    多头注意力模块: 将特征维度切分成多个头并行计算，
    既能扩大感受野又能让不同头关注到互补的子空间信息。
    """

    def __init__(self, d_model: int, n_heads: int, dropout: float = 0.1) -> None:
        super().__init__()
        assert d_model % n_heads == 0, "d_model 必须能被 n_heads 整除"
        self.d_model = d_model
        self.n_heads = n_heads
        self.d_k = d_model // n_heads

        # 使用单层线性映射分别生成 Q/K/V，便于后续在 head 维度上重排
        self.w_q = nn.Linear(d_model, d_model)
        self.w_k = nn.Linear(d_model, d_model)
        self.w_v = nn.Linear(d_model, d_model)
        self.w_o = nn.Linear(d_model, d_model)

        self.dropout = nn.Dropout(dropout)

    def forward(
        self,
        query: torch.Tensor,
        key: torch.Tensor,
        value: torch.Tensor,
        mask: Optional[torch.Tensor] = None,
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        batch_size = query.size(0)

        # 先投影再 reshape 成 (batch, head, seq, d_k)，方便做并行缩放点积注意力
        def transform(x: torch.Tensor, linear: nn.Linear) -> torch.Tensor:
            x = linear(x)
            return x.view(batch_size, -1, self.n_heads, self.d_k).transpose(1, 2)

        q = transform(query, self.w_q)
        k = transform(key, self.w_k)
        v = transform(value, self.w_v)

        scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.d_k)
        if mask is not None:
            # mask 使用 -inf 惩罚被遮蔽位置，使其 softmax 概率接近 0
            scores = scores.masked_fill(mask == 0, float("-inf"))

        attn = F.softmax(scores, dim=-1)
        attn = self.dropout(attn)
        output = torch.matmul(attn, v)

        # 将多头结果拼回原始维度 (batch, seq, d_model)，再做线性变换融合信息
        output = (
            output.transpose(1, 2)
            .contiguous()
            .view(batch_size, -1, self.d_model)
        )
        output = self.w_o(output)
        return output, attn


class PositionwiseFeedForward(nn.Module):
    """
    前馈网络模块: 在每个位置分别使用两层 MLP，
    引入非线性变换以提升表达能力，同时不破坏序列的并行性。
    """

    def __init__(self, d_model: int, d_ff: int, dropout: float = 0.1) -> None:
        super().__init__()
        self.linear1 = nn.Linear(d_model, d_ff)
        self.linear2 = nn.Linear(d_ff, d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # 使用 ReLU 实现论文中的前馈子层激活函数，兼顾稳定性和计算效率
        return self.linear2(self.dropout(F.relu(self.linear1(x))))


class EncoderLayer(nn.Module):
    """
    Encoder 基本层: Multi-Head Self-Attention + FFN + 残差 + LayerNorm，
    模块化设计方便堆叠多层形成深度编码器。
    """

    def __init__(
        self,
        d_model: int,
        n_heads: int,
        d_ff: int,
        dropout: float = 0.1,
    ) -> None:
        super().__init__()
        self.self_attn = MultiHeadAttention(d_model, n_heads, dropout)
        self.ffn = PositionwiseFeedForward(d_model, d_ff, dropout)
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.dropout1 = nn.Dropout(dropout)
        self.dropout2 = nn.Dropout(dropout)

    def forward(
        self, src: torch.Tensor, src_mask: Optional[torch.Tensor]
    ) -> torch.Tensor:
        # Self-Attention + 残差与规范化，提高梯度流动稳定性
        attn_output, _ = self.self_attn(src, src, src, src_mask)
        src = self.norm1(src + self.dropout1(attn_output))
        # FFN 子层同样使用残差与 LayerNorm，保持训练深层网络的可行性
        ffn_output = self.ffn(src)
        src = self.norm2(src + self.dropout2(ffn_output))
        return src


class DecoderLayer(nn.Module):
    """
    Decoder 基本层: Masked Self-Attention + Encoder-Decoder Attention + FFN，
    通过掩码避免泄露未来信息，并显式接收编码器上下文。
    """

    def __init__(
        self,
        d_model: int,
        n_heads: int,
        d_ff: int,
        dropout: float = 0.1,
    ) -> None:
        super().__init__()
        self.self_attn = MultiHeadAttention(d_model, n_heads, dropout)
        self.cross_attn = MultiHeadAttention(d_model, n_heads, dropout)
        self.ffn = PositionwiseFeedForward(d_model, d_ff, dropout)

        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.norm3 = nn.LayerNorm(d_model)
        self.dropout1 = nn.Dropout(dropout)
        self.dropout2 = nn.Dropout(dropout)
        self.dropout3 = nn.Dropout(dropout)

    def forward(
        self,
        tgt: torch.Tensor,
        memory: torch.Tensor,
        tgt_mask: Optional[torch.Tensor],
        memory_mask: Optional[torch.Tensor],
    ) -> torch.Tensor:
        # Masked Self-Attention，确保自回归解码仅依赖于历史 token
        attn_output, _ = self.self_attn(tgt, tgt, tgt, tgt_mask)
        tgt = self.norm1(tgt + self.dropout1(attn_output))
        # Encoder-Decoder Attention 让解码器在生成时显式对齐源句表示
        attn_output, _ = self.cross_attn(tgt, memory, memory, memory_mask)
        tgt = self.norm2(tgt + self.dropout2(attn_output))
        # FFN 子层引入位置独立非线性，提升解码表达能力
        ffn_output = self.ffn(tgt)
        tgt = self.norm3(tgt + self.dropout3(ffn_output))
        return tgt


class Encoder(nn.Module):
    """
    Encoder 堆叠若干层 EncoderLayer，将离散 token 序列编码成连续表示，
    该表示将作为 Decoder 的上下文供后续注意力访问。
    """

    def __init__(
        self,
        vocab_size: int,
        d_model: int = 256,
        n_layers: int = 4,
        n_heads: int = 4,
        d_ff: int = 1024,
        dropout: float = 0.1,
    ) -> None:
        super().__init__()
        self.d_model = d_model
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.pos_encoder = PositionalEncoding(d_model, dropout)
        self.layers = nn.ModuleList(
            [
                EncoderLayer(d_model, n_heads, d_ff, dropout)
                for _ in range(n_layers)
            ]
        )
        self.norm = nn.LayerNorm(d_model)

    def forward(
        self, src: torch.Tensor, src_mask: Optional[torch.Tensor]
    ) -> torch.Tensor:
        # 先做 embedding 并乘以 sqrt(d_model) 保持数值尺度与位置编码匹配
        src = self.embedding(src) * math.sqrt(self.d_model)
        src = self.pos_encoder(src)
        for layer in self.layers:
            src = layer(src, src_mask)
        return self.norm(src)


class Decoder(nn.Module):
    """
    Decoder 负责自回归生成目标序列，
    通过多层 DecoderLayer 逐步整合历史翻译和源端上下文。
    """

    def __init__(
        self,
        vocab_size: int,
        d_model: int = 256,
        n_layers: int = 4,
        n_heads: int = 4,
        d_ff: int = 1024,
        dropout: float = 0.1,
    ) -> None:
        super().__init__()
        self.d_model = d_model
        self.embedding = nn.Embedding(vocab_size, d_model)
        self.pos_encoder = PositionalEncoding(d_model, dropout)
        self.layers = nn.ModuleList(
            [
                DecoderLayer(d_model, n_heads, d_ff, dropout)
                for _ in range(n_layers)
            ]
        )
        self.norm = nn.LayerNorm(d_model)

    def forward(
        self,
        tgt: torch.Tensor,
        memory: torch.Tensor,
        tgt_mask: Optional[torch.Tensor],
        memory_mask: Optional[torch.Tensor],
    ) -> torch.Tensor:
        tgt = self.embedding(tgt) * math.sqrt(self.d_model)
        tgt = self.pos_encoder(tgt)
        for layer in self.layers:
            tgt = layer(tgt, memory, tgt_mask, memory_mask)
        return self.norm(tgt)


class Transformer(nn.Module):
    """
    完整 Transformer: Encoder-Decoder 结构 + 共享词嵌入 + 线性输出层，
    该实现保持论文结构但缩小隐藏维度和层数以控制参数量。
    """

    def __init__(
        self,
        src_vocab_size: int,
        tgt_vocab_size: int,
        d_model: int = 256,
        n_layers: int = 4,
        n_heads: int = 4,
        d_ff: int = 1024,
        dropout: float = 0.1,
        share_embeddings: bool = True,
    ) -> None:
        super().__init__()
        self.encoder = Encoder(
            vocab_size=src_vocab_size,
            d_model=d_model,
            n_layers=n_layers,
            n_heads=n_heads,
            d_ff=d_ff,
            dropout=dropout,
        )
        self.decoder = Decoder(
            vocab_size=tgt_vocab_size,
            d_model=d_model,
            n_layers=n_layers,
            n_heads=n_heads,
            d_ff=d_ff,
            dropout=dropout,
        )
        self.generator = nn.Linear(d_model, tgt_vocab_size)

        if share_embeddings and src_vocab_size == tgt_vocab_size:
            # 共享词嵌入能显著减少参数量，并帮助源/目标语言共享词形结构信息
            self.encoder.embedding.weight = self.decoder.embedding.weight

        self._reset_parameters()

    def _reset_parameters(self) -> None:
        # 使用 Xavier 初始化线性层和嵌入，遵循论文设置并保持梯度方差稳定
        for name, p in self.named_parameters():
            if p.dim() > 1 and "embedding" not in name:
                nn.init.xavier_uniform_(p)

    def encode(self, src: torch.Tensor, src_mask: Optional[torch.Tensor]) -> torch.Tensor:
        return self.encoder(src, src_mask)

    def decode(
        self,
        tgt: torch.Tensor,
        memory: torch.Tensor,
        tgt_mask: Optional[torch.Tensor],
        memory_mask: Optional[torch.Tensor],
    ) -> torch.Tensor:
        return self.decoder(tgt, memory, tgt_mask, memory_mask)

    def forward(
        self,
        src: torch.Tensor,
        tgt: torch.Tensor,
        src_mask: Optional[torch.Tensor],
        tgt_mask: Optional[torch.Tensor],
    ) -> torch.Tensor:
        # 前向过程: 先编码源句，再解码目标句，最后映射到词表 logits
        memory = self.encode(src, src_mask)
        out = self.decode(tgt, memory, tgt_mask, src_mask)
        logits = self.generator(out)
        return logits


def count_parameters(model: nn.Module) -> int:
    """
    统计可训练参数量，便于快速验证是否满足轻量级约束。
    """

    return sum(p.numel() for p in model.parameters() if p.requires_grad)


def dummy_profile(device: str = "cuda" if torch.cuda.is_available() else "cpu") -> None:
    """
    构造一个小批次伪数据跑通前向，打印参数量与显存占用，
    用于快速 sanity check 模型规模与显存需求。
    """

    torch.manual_seed(42)
    src_vocab_size = 16000
    tgt_vocab_size = 16000
    model = Transformer(
        src_vocab_size=src_vocab_size,
        tgt_vocab_size=tgt_vocab_size,
        d_model=256,
        n_layers=4,
        n_heads=4,
        d_ff=1024,
        dropout=0.1,
        share_embeddings=True,
    ).to(device)

    n_params = count_parameters(model)
    print(f"模型参数量: {n_params / 1e6:.2f} M")

    batch_size = 8
    src_len = 32
    tgt_len = 32
    src = torch.randint(0, src_vocab_size, (batch_size, src_len), device=device)
    tgt = torch.randint(0, tgt_vocab_size, (batch_size, tgt_len), device=device)

    # 构造简单的全 1 mask，实际训练时会使用 padding 与未来信息掩码
    src_mask = torch.ones(
        (batch_size, 1, 1, src_len), dtype=torch.bool, device=device
    )
    tgt_mask = torch.ones(
        (batch_size, 1, tgt_len, tgt_len), dtype=torch.bool, device=device
    )

    if device.startswith("cuda"):
        torch.cuda.reset_peak_memory_stats(device)

    start = time.time()
    with torch.no_grad():
        out = model(src, tgt, src_mask, tgt_mask)
    end = time.time()

    print(f"输出张量形状: {out.shape}")
    print(f"前向耗时: {(end - start) * 1000:.2f} ms")

    if device.startswith("cuda"):
        mem = torch.cuda.max_memory_allocated(device) / (1024 ** 2)
        print(f"峰值显存占用: {mem:.2f} MB")


if __name__ == "__main__":
    # 直接运行本文件进行快速单元测试，确保模型结构与规模符合预期
    dummy_profile()

