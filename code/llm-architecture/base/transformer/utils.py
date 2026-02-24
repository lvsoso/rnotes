#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
作者: Zhuanz
日期: 2026-02-23
依赖版本: torch>=2.0, sacrebleu>=2.4, sentencepiece>=0.1
运行示例:
    学习率调度可视化:
        python -m transformer.utils --plot-lr

本文件收集训练 Transformer 所需的通用工具函数，
包括随机种子固定、学习率调度、标签平滑、掩码构造、
BLEU 评估与 checkpoint 读写等，以避免在脚本中重复实现。
"""

import argparse
import math
import os
import random
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional, Tuple

import numpy as np
import sacrebleu
import torch
import torch.nn as nn
from torch.optim import Optimizer


def set_seed(seed: int) -> None:
    """
    固定所有常见随机源的种子，确保实验可重现性。
    """

    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)
    # 关闭一些不确定性优化选项，换取结果的稳定性
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


class NoamLR(torch.optim.lr_scheduler._LRScheduler):
    """
    Noam 学习率调度策略: 先线性 warmup 再按 step^-0.5 衰减，
    利用较大学习率加速前期收敛，同时在后期保持训练稳定。
    """

    def __init__(
        self,
        optimizer: Optimizer,
        d_model: int,
        warmup_steps: int = 4000,
        factor: float = 1.0,
        last_epoch: int = -1,
    ) -> None:
        self.d_model = d_model
        self.warmup_steps = warmup_steps
        self.factor = factor
        super().__init__(optimizer, last_epoch)

    def get_lr(self) -> List[float]:
        step = max(self.last_epoch, 1)
        # 论文中的闭式公式，直接基于 step 计算当前学习率
        scale = self.factor * (self.d_model ** -0.5)
        scale *= min(step ** -0.5, step * (self.warmup_steps ** -1.5))
        return [scale for _ in self.base_lrs]


class LabelSmoothingLoss(nn.Module):
    """
    标签平滑交叉熵: 在 one-hot 标签上分配少量概率给其他类别，
    减少模型对单一类别的过度自信，提升泛化性能。
    """

    def __init__(
        self,
        label_smoothing: float,
        vocab_size: int,
        ignore_index: int = 0,
    ) -> None:
        super().__init__()
        assert 0.0 <= label_smoothing < 1.0
        self.ignore_index = ignore_index
        self.confidence = 1.0 - label_smoothing
        self.smoothing = label_smoothing
        self.vocab_size = vocab_size

    def forward(self, pred: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
        # pred: (batch, seq, vocab), target: (batch, seq)
        pred = pred.view(-1, self.vocab_size)
        target = target.view(-1)

        # 构造平滑标签分布时跳过 padding 位置，避免对损失造成污染
        mask = target.ne(self.ignore_index)
        target = target[mask]
        pred = pred[mask]

        with torch.no_grad():
            true_dist = torch.full_like(pred, self.smoothing / (self.vocab_size - 1))
            true_dist.scatter_(1, target.unsqueeze(1), self.confidence)
        loss = torch.sum(-true_dist * torch.log_softmax(pred, dim=-1), dim=-1)
        return loss.mean()


def create_padding_mask(seq: torch.Tensor, pad_idx: int) -> torch.Tensor:
    """
    根据 padding 索引构造 mask，扩展为 (batch, 1, 1, seq_len) 形状，
    便于与多头注意力中的 scores 广播相加。
    """

    mask = (seq != pad_idx).unsqueeze(1).unsqueeze(2)
    return mask


def create_subsequent_mask(size: int) -> torch.Tensor:
    """
    构造下三角 mask，确保解码阶段每个位置只能看到自己和之前的 token，
    避免自回归任务中“偷看未来”导致的暴露偏差。
    """

    attn_shape = (1, size, size)
    subsequent_mask = torch.tril(torch.ones(attn_shape, dtype=torch.bool))
    return subsequent_mask


def create_tgt_mask(tgt: torch.Tensor, pad_idx: int) -> torch.Tensor:
    """
    同时结合 padding mask 与 下三角 mask，得到完整目标端注意力掩码。
    """

    tgt_pad_mask = (tgt != pad_idx).unsqueeze(1).unsqueeze(2)
    tgt_len = tgt.size(1)
    subsequent_mask = create_subsequent_mask(tgt_len).to(tgt.device)
    mask = tgt_pad_mask & subsequent_mask.unsqueeze(1)
    return mask


def calculate_bleu(
    references: List[str], hypotheses: List[str], lowercase: bool = True
) -> float:
    """
    使用 sacrebleu 计算 BLEU，保证和论文及社区常用指标兼容。
    """

    bleu = sacrebleu.corpus_bleu(
        hypotheses,
        [references],
        lowercase=lowercase,
        tokenize="13a",
    )
    return float(bleu.score)


def save_checkpoint(
    path: str,
    model: nn.Module,
    optimizer: Optimizer,
    scheduler: Optional[torch.optim.lr_scheduler._LRScheduler],
    step: int,
    extra: Optional[Dict[str, Any]] = None,
) -> None:
    """
    将训练中间状态打包保存，便于中断后恢复或做离线推理。
    """

    state = {
        "model_state": model.state_dict(),
        "optimizer_state": optimizer.state_dict(),
        "scheduler_state": scheduler.state_dict() if scheduler is not None else None,
        "step": step,
    }
    if extra:
        state["extra"] = extra
    os.makedirs(os.path.dirname(path), exist_ok=True)
    torch.save(state, path)


def load_checkpoint(
    path: str,
    model: nn.Module,
    optimizer: Optional[Optimizer] = None,
    scheduler: Optional[torch.optim.lr_scheduler._LRScheduler] = None,
    map_location: str = "cpu",
) -> int:
    """
    从磁盘加载 checkpoint 并恢复模型 / 优化器状态，
    返回训练步数以便继续训练或复现实验。
    """

    state = torch.load(path, map_location=map_location)
    model.load_state_dict(state["model_state"])
    if optimizer is not None and "optimizer_state" in state:
        optimizer.load_state_dict(state["optimizer_state"])
    if scheduler is not None and state.get("scheduler_state") is not None:
        scheduler.load_state_dict(state["scheduler_state"])
    return int(state.get("step", 0))


def get_grad_norm(parameters: Iterable[torch.nn.Parameter]) -> float:
    """
    计算所有可训练参数的梯度范数，便于监控训练稳定性。
    """

    total_norm = 0.0
    for p in parameters:
        if p.grad is None:
            continue
        param_norm = p.grad.data.norm(2)
        total_norm += float(param_norm ** 2)
    return float(total_norm ** 0.5)


@dataclass
class LRCurveConfig:
    """
    用简单数据类描述学习率曲线生成配置，
    便于在命令行可视化 Noam 调度行为。
    """

    d_model: int = 256
    warmup_steps: int = 4000
    factor: float = 1.0
    total_steps: int = 8000


def plot_noam_lr_curve(cfg: LRCurveConfig) -> None:
    """
    控制台打印若干步的学习率值，用于直观观察 warmup 与衰减阶段。
    如需绘图，可在 notebook 中基于该函数的输出进行可视化。
    """

    dummy_param = torch.nn.Parameter(torch.zeros(1))
    optimizer = torch.optim.Adam([dummy_param], lr=1.0)
    scheduler = NoamLR(
        optimizer,
        d_model=cfg.d_model,
        warmup_steps=cfg.warmup_steps,
        factor=cfg.factor,
    )
    print("step\tlr")
    for step in range(1, cfg.total_steps + 1):
        scheduler.step()
        lr = scheduler.get_last_lr()[0]
        if step % (cfg.total_steps // 20) == 0 or step <= 10:
            print(f"{step}\t{lr:.8f}")


def _parse_args() -> argparse.Namespace:
    """
    简单命令行解析，仅用于演示和调试工具函数行为。
    """

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--plot-lr",
        action="store_true",
        help="打印 Noam 学习率曲线示例",
    )
    return parser.parse_args()


def main() -> None:
    """
    支持命令行调用本模块进行快速功能检查，
    例如打印 Noam 学习率变化趋势。
    """

    args = _parse_args()
    if args.plot_lr:
        cfg = LRCurveConfig()
        plot_noam_lr_curve(cfg)


if __name__ == "__main__":
    main()

