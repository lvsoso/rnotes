#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
作者: Zhuanz
日期: 2026-02-23
依赖版本: transformers>=4.36, torch>=2.0
运行示例:
    将当前 Transformer 包装为 HuggingFace 模型:
        python -m transformer.hf_export --ckpt checkpoints/step_50000.pt
"""

from typing import Optional, Tuple

import torch
import torch.nn.functional as F
from torch import nn

from transformers import PreTrainedModel, PretrainedConfig
from transformers.modeling_outputs import Seq2SeqLMOutput

from .model import Transformer
from .utils import create_padding_mask, create_tgt_mask


class TransformerConfig(PretrainedConfig):
    """
    轻量级 Transformer 的 HuggingFace 配置封装,
    便于与 vLLM / sglang 等生态对接。
    """

    model_type = "custom_transformer"

    def __init__(
        self,
        vocab_size: int,
        d_model: int = 256,
        n_layers: int = 4,
        n_heads: int = 4,
        d_ff: int = 1024,
        dropout: float = 0.1,
        pad_token_id: int = 0,
        bos_token_id: int = 1,
        eos_token_id: int = 2,
        **kwargs,
    ) -> None:
        super().__init__(
            vocab_size=vocab_size,
            pad_token_id=pad_token_id,
            bos_token_id=bos_token_id,
            eos_token_id=eos_token_id,
            is_encoder_decoder=True,
            **kwargs,
        )
        self.d_model = d_model
        self.n_layers = n_layers
        self.n_heads = n_heads
        self.d_ff = d_ff
        self.dropout = dropout


class HFTransformer(PreTrainedModel):
    """
    将项目中的 Transformer 封装为 HuggingFace Seq2Seq 模型,
    方便导出到 HF Hub 或接入第三方推理引擎。
    """

    config_class = TransformerConfig

    def __init__(self, config: TransformerConfig) -> None:
        super().__init__(config)
        self.model = Transformer(
            src_vocab_size=config.vocab_size,
            tgt_vocab_size=config.vocab_size,
            d_model=config.d_model,
            n_layers=config.n_layers,
            n_heads=config.n_heads,
            d_ff=config.d_ff,
            dropout=config.dropout,
            share_embeddings=True,
        )

    def forward(
        self,
        input_ids: torch.Tensor,
        attention_mask: Optional[torch.Tensor] = None,
        decoder_input_ids: Optional[torch.Tensor] = None,
        decoder_attention_mask: Optional[torch.Tensor] = None,
        labels: Optional[torch.Tensor] = None,
        **kwargs,
    ) -> Seq2SeqLMOutput:
        device = input_ids.device
        pad_id = self.config.pad_token_id

        if attention_mask is None:
            attention_mask = (input_ids != pad_id).long()
        if decoder_input_ids is None and labels is not None:
            decoder_input_ids = labels.clone()
            decoder_input_ids = decoder_input_ids.masked_fill(decoder_input_ids == -100, pad_id)
            decoder_input_ids = torch.cat(
                [
                    torch.full(
                        (decoder_input_ids.size(0), 1),
                        self.config.bos_token_id,
                        device=device,
                        dtype=decoder_input_ids.dtype,
                    ),
                    decoder_input_ids[:, :-1],
                ],
                dim=1,
            )

        src_mask_4d = create_padding_mask(input_ids, pad_id).to(device)
        if decoder_attention_mask is None:
            decoder_attention_mask = (decoder_input_ids != pad_id).long()
        tgt_mask_4d = create_tgt_mask(decoder_input_ids, pad_id).to(device)

        logits = self.model(
            src=input_ids,
            tgt=decoder_input_ids,
            src_mask=src_mask_4d,
            tgt_mask=tgt_mask_4d,
        )

        loss: Optional[torch.Tensor] = None
        if labels is not None:
            vocab_size = logits.size(-1)
            loss = F.cross_entropy(
                logits.view(-1, vocab_size),
                labels.view(-1),
                ignore_index=pad_id,
            )

        return Seq2SeqLMOutput(
            loss=loss,
            logits=logits,
            past_key_values=None,
            decoder_hidden_states=None,
            decoder_attentions=None,
            cross_attentions=None,
            encoder_last_hidden_state=None,
            encoder_hidden_states=None,
            encoder_attentions=None,
        )
