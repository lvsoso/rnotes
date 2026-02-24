#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
作者: Zhuanz
日期: 2026-02-23
依赖版本: transformers>=4.36, torch>=2.0
运行示例:
    从本项目 checkpoint 导出 HuggingFace 兼容模型:
        cd /Users/Zhuanz/lvsoso/rnotes/code/llm-architecture/base
        python -m transformer.hf_export --ckpt checkpoints/step_50000.pt
"""

import argparse
import os

import sentencepiece as spm
import torch
import yaml

from .hf_wrapper import HFTransformer, TransformerConfig
from .model import Transformer
from .utils import load_checkpoint


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="transformer/config.yaml")
    parser.add_argument("--ckpt", type=str, required=True)
    parser.add_argument("--export-dir", type=str, default="./hf_export")
    return parser.parse_args()


def load_yaml_config(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main() -> None:
    args = parse_args()
    cfg = load_yaml_config(args.config)
    data_cfg = cfg["data"]
    model_cfg = cfg["model"]

    spm_path = os.path.join(
        data_cfg["data_dir"], f"spm_{data_cfg['vocab_size']}.model"
    )
    sp = spm.SentencePieceProcessor()
    sp.load(spm_path)
    vocab_size = sp.get_vocab_size()
    pad_id = sp.pad_id()
    bos_id = sp.bos_id()
    eos_id = sp.eos_id()

    base_model = Transformer(
        src_vocab_size=vocab_size,
        tgt_vocab_size=vocab_size,
        d_model=model_cfg["d_model"],
        n_layers=model_cfg["n_layers"],
        n_heads=model_cfg["n_heads"],
        d_ff=model_cfg["d_ff"],
        dropout=model_cfg["dropout"],
        share_embeddings=model_cfg.get("share_embeddings", True),
    )
    load_checkpoint(
        args.ckpt,
        base_model,
        optimizer=None,
        scheduler=None,
        map_location="cpu",
    )

    hf_config = TransformerConfig(
        vocab_size=vocab_size,
        d_model=model_cfg["d_model"],
        n_layers=model_cfg["n_layers"],
        n_heads=model_cfg["n_heads"],
        d_ff=model_cfg["d_ff"],
        dropout=model_cfg["dropout"],
        pad_token_id=pad_id,
        bos_token_id=bos_id,
        eos_token_id=eos_id,
    )
    hf_model = HFTransformer(hf_config)
    hf_model.model.load_state_dict(base_model.state_dict())

    os.makedirs(args.export_dir, exist_ok=True)
    hf_model.save_pretrained(args.export_dir, safe_serialization=True)
    print(f"HuggingFace safetensors 模型已导出到: {os.path.abspath(args.export_dir)}")


if __name__ == "__main__":
    main()
