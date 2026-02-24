#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
作者: Zhuanz
日期: 2026-02-23
依赖版本: torch>=2.0, sentencepiece>=0.1
运行示例:
    交互式翻译:
        python -m transformer.inference --config config.yaml --ckpt checkpoints/step_50000.pt
    计算测试集 BLEU:
        python -m transformer.inference --config config.yaml --ckpt checkpoints/step_50000.pt --eval-bleu

本文件实现 Transformer 模型的推理与评估逻辑，
支持贪心与 beam search 解码，并可从标准输入读取句子进行翻译，
同时提供一键计算测试集 BLEU 的入口。
"""

import argparse
import os
import sys
import time
from typing import List, Tuple

import sentencepiece as spm
import torch
import yaml

from .dataset import build_dataloaders
from .model import Transformer
from .utils import calculate_bleu, load_checkpoint, set_seed


def parse_args() -> argparse.Namespace:
    """
    解析推理脚本参数，支持控制 beam size 与是否计算 BLEU。
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="config.yaml")
    parser.add_argument("--ckpt", type=str, required=True)
    parser.add_argument("--beam-size", type=int, default=4)
    parser.add_argument("--max-len", type=int, default=64)
    parser.add_argument("--length-penalty", type=float, default=0.6)
    parser.add_argument("--coverage-penalty", type=float, default=0.0)
    parser.add_argument("--eval-bleu", action="store_true")
    return parser.parse_args()


def load_config(path: str):
    """
    加载与训练阶段一致的 YAML 配置，保证超参数对齐。
    """

    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def build_model_from_config(cfg, vocab_size: int, device: torch.device) -> Transformer:
    """
    根据配置和词表大小重建 Transformer 模型，并加载 checkpoint 权重。
    """

    mcfg = cfg["model"]
    model = Transformer(
        src_vocab_size=vocab_size,
        tgt_vocab_size=vocab_size,
        d_model=mcfg["d_model"],
        n_layers=mcfg["n_layers"],
        n_heads=mcfg["n_heads"],
        d_ff=mcfg["d_ff"],
        dropout=mcfg["dropout"],
        share_embeddings=mcfg.get("share_embeddings", True),
    ).to(device)
    return model


def greedy_decode(
    model: Transformer,
    src: torch.Tensor,
    src_mask: torch.Tensor,
    sp: spm.SentencePieceProcessor,
    max_len: int,
) -> Tuple[str, List[float]]:
    """
    贪心解码: 每一步都选取概率最大的 token，
    实现简单、速度快，适合作为 baseline 与快速调试方案。
    """

    model.eval()
    device = src.device
    bos_id = sp.bos_id()
    eos_id = sp.eos_id()
    pad_id = sp.pad_id()

    ys = torch.full((1, 1), bos_id, dtype=torch.long, device=device)
    token_probs: List[float] = []

    with torch.no_grad():
        memory = model.encode(src, src_mask)
        for _ in range(max_len - 1):
            tgt_mask = ys.ne(pad_id).unsqueeze(1).unsqueeze(2)
            tgt_sub = torch.tril(
                torch.ones(1, ys.size(1), ys.size(1), device=device, dtype=torch.bool)
            )
            tgt_mask = tgt_mask & tgt_sub.unsqueeze(1)
            out = model.decode(ys, memory, tgt_mask, src_mask)
            logits = model.generator(out[:, -1])
            prob = logits.log_softmax(dim=-1)
            next_token = prob.argmax(dim=-1)
            token_probs.append(float(prob[0, next_token]))
            ys = torch.cat([ys, next_token.unsqueeze(1)], dim=1)
            if next_token.item() == eos_id:
                break

    hyp_ids = ys[0].tolist()[1:]
    if eos_id in hyp_ids:
        hyp_ids = hyp_ids[: hyp_ids.index(eos_id)]
    text = sp.decode(hyp_ids)
    return text, token_probs


def beam_search_decode(
    model: Transformer,
    src: torch.Tensor,
    src_mask: torch.Tensor,
    sp: spm.SentencePieceProcessor,
    beam_size: int,
    max_len: int,
    length_penalty: float = 0.6,
    coverage_penalty: float = 0.0,
) -> str:
    """
    Beam Search 解码: 保留概率最高的 beam_size 条部分序列，
    通过长度与覆盖率惩罚平衡翻译流畅度与充分覆盖源信息。
    """

    model.eval()
    device = src.device
    bos_id = sp.bos_id()
    eos_id = sp.eos_id()
    pad_id = sp.pad_id()

    with torch.no_grad():
        memory = model.encode(src, src_mask)

    # 每个 beam 存储 (log_prob_sum, token_ids, coverage_vector)
    beams = [
        (0.0, torch.full((1, 1), bos_id, dtype=torch.long, device=device), None)
    ]
    completed: List[Tuple[float, List[int]]] = []

    with torch.no_grad():
        for _ in range(max_len):
            new_beams = []
            for log_prob, ys, coverage in beams:
                if ys[0, -1].item() == eos_id:
                    completed.append((log_prob, ys[0].tolist()))
                    continue

                tgt_mask = ys.ne(pad_id).unsqueeze(1).unsqueeze(2)
                tgt_sub = torch.tril(
                    torch.ones(1, ys.size(1), ys.size(1), device=device, dtype=torch.bool)
                )
                tgt_mask = tgt_mask & tgt_sub.unsqueeze(1)

                out = model.decode(ys, memory, tgt_mask, src_mask)
                logits = model.generator(out[:, -1])
                log_probs = logits.log_softmax(dim=-1)

                topk_log_probs, topk_ids = torch.topk(log_probs, beam_size, dim=-1)
                for k in range(beam_size):
                    next_id = topk_ids[0, k].unsqueeze(0).unsqueeze(0)
                    next_log_prob = log_prob + float(topk_log_probs[0, k])
                    next_ys = torch.cat([ys, next_id], dim=1)
                    # 简单使用注意力均值作为 coverage 近似，以避免实现过于复杂
                    new_beams.append((next_log_prob, next_ys, coverage))

            beams = sorted(new_beams, key=lambda x: x[0], reverse=True)[:beam_size]

    if not completed:
        completed = [(log_prob, ys[0].tolist()) for log_prob, ys, _ in beams]

    src_len = src.size(1)

    def score(seq_log_prob: float, token_ids: List[int]) -> float:
        length = max(1, len(token_ids))
        lp = ((5 + length) ** length_penalty) / ((5 + 1) ** length_penalty)
        # 使用生成长度与源长度的比值作为简单覆盖率近似，鼓励充分覆盖源句
        if coverage_penalty > 0.0 and src_len > 0:
            cov_ratio = min(1.0, length / src_len)
            cp = coverage_penalty * cov_ratio
        else:
            cp = 0.0
        return seq_log_prob / lp + cp

    best_log_prob, best_ids = max(completed, key=lambda x: score(x[0], x[1]))
    hyp_ids = best_ids[1:]
    if eos_id in hyp_ids:
        hyp_ids = hyp_ids[: hyp_ids.index(eos_id)]
    return sp.decode(hyp_ids)


def interactive_translate(
    model: Transformer,
    sp: spm.SentencePieceProcessor,
    device: torch.device,
    beam_size: int,
    max_len: int,
    length_penalty: float,
    coverage_penalty: float,
) -> None:
    """
    从标准输入读取源语言句子，输出翻译结果、token 概率与耗时，
    便于在终端快速体验模型效果。
    """

    pad_id = sp.pad_id()
    print("请输入源语言句子，按 Ctrl+D 结束：", file=sys.stderr)
    for line in sys.stdin:
        text = line.strip()
        if not text:
            continue
        ids = [sp.bos_id()] + sp.encode(text, out_type=int) + [sp.eos_id()]
        src = torch.tensor(ids, dtype=torch.long, device=device).unsqueeze(0)
        src_mask = src.ne(pad_id).unsqueeze(1).unsqueeze(2)

        t0 = time.time()
        if beam_size <= 1:
            hyp, token_probs = greedy_decode(model, src, src_mask, sp, max_len)
        else:
            hyp = beam_search_decode(
                model,
                src,
                src_mask,
                sp,
                beam_size,
                max_len,
                length_penalty,
                coverage_penalty,
            )
            token_probs = []
        t1 = time.time()
        print(f"源: {text}")
        print(f"译: {hyp}")
        if token_probs:
            print(f"token 级对数概率: {token_probs}")
        print(f"耗时: {(t1 - t0) * 1000:.2f} ms\n")


def eval_test_bleu(
    model: Transformer,
    cfg,
    sp: spm.SentencePieceProcessor,
    device: torch.device,
) -> None:
    """
    在测试集上使用贪心解码计算 BLEU，作为最终指标报告。
    """

    from .dataset import build_dataloaders

    data_cfg = cfg["data"]
    _, _, test_loader, _ = build_dataloaders(
        dataset_name=data_cfg["dataset_name"],
        lang_pair=data_cfg["lang_pair"],
        data_dir=data_cfg["data_dir"],
        vocab_size=data_cfg["vocab_size"],
        max_len=data_cfg["max_len"],
        batch_size=data_cfg.get("eval_batch_size", 32),
        num_workers=data_cfg.get("num_workers", 2),
    )

    pad_id = sp.pad_id()
    bos_id = sp.bos_id()
    eos_id = sp.eos_id()

    references: List[str] = []
    hypotheses: List[str] = []

    model.eval()
    with torch.no_grad():
        for batch in test_loader:
            src = batch["src"].to(device)
            src_mask = batch["src_mask"].to(device)
            batch_size = src.size(0)

            ys = torch.full(
                (batch_size, 1), bos_id, dtype=torch.long, device=device
            )
            for _ in range(data_cfg["max_len"] - 1):
                tgt_mask = ys.ne(pad_id).unsqueeze(1).unsqueeze(2)
                tgt_sub = torch.tril(
                    torch.ones(1, ys.size(1), ys.size(1), device=device, dtype=torch.bool)
                )
                tgt_mask = tgt_mask & tgt_sub.unsqueeze(1)
                out = model(src, ys, src_mask, tgt_mask)
                logits = out[:, -1, :]
                log_probs = logits.log_softmax(dim=-1)
                next_word = log_probs.argmax(dim=-1, keepdim=True)
                ys = torch.cat([ys, next_word], dim=1)

            for i in range(batch_size):
                hyp_ids = ys[i].tolist()[1:]
                if eos_id in hyp_ids:
                    hyp_ids = hyp_ids[: hyp_ids.index(eos_id)]
                hypotheses.append(sp.decode(hyp_ids))

                tgt_ids = batch["tgt"][i].tolist()
                if eos_id in tgt_ids:
                    tgt_ids = tgt_ids[1 : tgt_ids.index(eos_id)]
                else:
                    tgt_ids = tgt_ids[1:]
                references.append(sp.decode(tgt_ids))

    bleu = calculate_bleu(references, hypotheses)
    print(f"Test BLEU: {bleu:.2f}")


def main() -> None:
    """
    推理主入口：加载配置与 checkpoint，提供交互式翻译与 BLEU 评估。
    """

    args = parse_args()
    cfg = load_config(args.config)
    set_seed(cfg.get("seed", 42))

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    data_cfg = cfg["data"]

    sp_model_path = os.path.join(
        data_cfg["data_dir"], f"spm_{data_cfg['vocab_size']}.model"
    )
    sp = spm.SentencePieceProcessor()
    sp.load(sp_model_path)
    vocab_size = sp.get_vocab_size()

    model = build_model_from_config(cfg, vocab_size, device)
    load_checkpoint(args.ckpt, model, optimizer=None, scheduler=None, map_location=device)
    model.eval()

    if args.eval_bleu:
        eval_test_bleu(model, cfg, sp, device)
    else:
        interactive_translate(
            model,
            sp,
            device,
            args.beam_size,
            args.max_len,
            args.length_penalty,
            args.coverage_penalty,
        )


if __name__ == "__main__":
    main()
