#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
作者: Zhuanz
日期: 2026-02-23
依赖版本: torch>=2.0, datasets>=2.0, sentencepiece>=0.1
运行示例:
    单卡训练:
        python -m transformer.train --config config.yaml
    多卡 DDP 训练:
        torchrun --nproc_per_node=4 -m transformer.train --config config.yaml

本文件实现基于 Encoder-Decoder Transformer 的机器翻译训练流程，
支持单卡与多卡 DDP、Noam 学习率调度、标签平滑、梯度累积与混合精度，
同时按步数记录日志并保存验证 BLEU 最优的 checkpoint。
"""

import argparse
import os
import time
from typing import Dict, Tuple

import torch
import torch.distributed as dist
import torch.nn as nn
from torch.nn.parallel import DistributedDataParallel as DDP
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
import yaml

from .dataset import build_dataloaders
from .model import Transformer
from .utils import (
    LabelSmoothingLoss,
    NoamLR,
    calculate_bleu,
    get_grad_norm,
    save_checkpoint,
    load_checkpoint,
    set_seed,
)


def parse_args() -> argparse.Namespace:
    """
    解析训练脚本命令行参数，配置文件与命令行参数组合控制实验。
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="config.yaml")
    parser.add_argument("--output-dir", type=str, default="./checkpoints")
    parser.add_argument("--log-dir", type=str, default="./logs")
    parser.add_argument("--resume", type=str, default="")
    parser.add_argument("--max-steps", type=int, default=-1)
    parser.add_argument("--local_rank", type=int, default=-1)
    return parser.parse_args()


def setup_distributed(local_rank: int) -> Tuple[bool, torch.device]:
    """
    初始化分布式环境，返回是否为主进程以及当前设备对象，
    以统一屏蔽 DDP 与单卡之间的环境差异。
    """

    if local_rank == -1:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        return True, device

    dist.init_process_group(backend="nccl")
    torch.cuda.set_device(local_rank)
    device = torch.device("cuda", local_rank)
    is_master = dist.get_rank() == 0
    return is_master, device


def load_config(path: str) -> Dict:
    """
    从 YAML 文件加载超参数配置，并以字典形式返回。
    """

    with open(path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    return cfg


def build_model_and_criterion(
    cfg: Dict,
    vocab_size: int,
    device: torch.device,
) -> Tuple[Transformer, nn.Module]:
    """
    根据配置构建 Transformer 模型与标签平滑损失函数，
    确保两者使用一致的 vocab_size 与 pad_idx。
    """

    model_cfg = cfg["model"]
    model = Transformer(
        src_vocab_size=vocab_size,
        tgt_vocab_size=vocab_size,
        d_model=model_cfg["d_model"],
        n_layers=model_cfg["n_layers"],
        n_heads=model_cfg["n_heads"],
        d_ff=model_cfg["d_ff"],
        dropout=model_cfg["dropout"],
        share_embeddings=model_cfg.get("share_embeddings", True),
    ).to(device)

    pad_idx = model_cfg.get("pad_idx", 0)
    crit = LabelSmoothingLoss(
        label_smoothing=cfg["training"]["label_smoothing"],
        vocab_size=vocab_size,
        ignore_index=pad_idx,
    ).to(device)
    return model, crit


def build_optimizer_and_scheduler(
    model: nn.Module,
    cfg: Dict,
) -> Tuple[torch.optim.Optimizer, NoamLR]:
    """
    构建 Adam 优化器与 Noam 调度策略，严格遵守论文参数设定。
    """

    train_cfg = cfg["training"]
    model_cfg = cfg["model"]
    optimizer = torch.optim.Adam(
        model.parameters(),
        betas=tuple(train_cfg.get("adam_betas", [0.9, 0.98])),
        eps=train_cfg.get("adam_eps", 1e-9),
    )
    scheduler = NoamLR(
        optimizer,
        d_model=model_cfg["d_model"],
        warmup_steps=train_cfg["warmup_steps"],
        factor=train_cfg["lr_factor"],
    )
    return optimizer, scheduler


def train_one_step(
    model: nn.Module,
    criterion: nn.Module,
    optimizer: torch.optim.Optimizer,
    scheduler: NoamLR,
    batch: Dict[str, torch.Tensor],
    device: torch.device,
    scaler: torch.cuda.amp.GradScaler,
    grad_accum_steps: int,
    step: int,
    max_grad_norm: float,
) -> Tuple[float, float]:
    """
    执行一次训练更新（包含梯度累积与混合精度），返回 loss 与当前 lr。
    """

    src = batch["src"].to(device)
    tgt = batch["tgt"].to(device)
    src_mask = batch["src_mask"].to(device)
    tgt_mask = batch["tgt_mask"].to(device)

    # 训练目标通常为预测下一个 token，因此标签右移一位
    tgt_inp = tgt[:, :-1]
    tgt_out = tgt[:, 1:]
    tgt_mask_inp = tgt_mask[:, :, :-1, :-1]

    with torch.cuda.amp.autocast(enabled=scaler.is_enabled()):
        logits = model(src, tgt_inp, src_mask, tgt_mask_inp)
        loss = criterion(logits, tgt_out)
        loss = loss / grad_accum_steps

    scaler.scale(loss).backward()

    if (step + 1) % grad_accum_steps == 0:
        # 在执行实际参数更新前进行梯度裁剪，避免梯度爆炸破坏训练稳定性
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=max_grad_norm)
        scaler.step(optimizer)
        scaler.update()
        optimizer.zero_grad(set_to_none=True)
        scheduler.step()

    lr = scheduler.get_last_lr()[0]
    return float(loss.item() * grad_accum_steps), lr


def evaluate_bleu(
    model: nn.Module,
    dataloader: DataLoader,
    sp_model_path: str,
    device: torch.device,
    max_len: int,
) -> float:
    """
    在验证集上用贪心解码评估 BLEU 分数，
    作为选择最佳 checkpoint 的指标。
    """

    import sentencepiece as spm

    sp = spm.SentencePieceProcessor()
    sp.load(sp_model_path)

    model.eval()
    references = []
    hypotheses = []
    pad_id = sp.pad_id()
    bos_id = sp.bos_id()
    eos_id = sp.eos_id()

    with torch.no_grad():
        for batch in dataloader:
            src = batch["src"].to(device)
            src_mask = batch["src_mask"].to(device)
            batch_size = src.size(0)

            # 使用简单贪心解码即可粗略反映模型整体质量
            ys = torch.full(
                (batch_size, 1), bos_id, dtype=torch.long, device=device
            )
            for _ in range(max_len - 1):
                tgt_mask = ys.ne(pad_id).unsqueeze(1).unsqueeze(2)
                tgt_sub = torch.tril(
                    torch.ones(1, ys.size(1), ys.size(1), device=device, dtype=torch.bool)
                )
                tgt_mask = tgt_mask & tgt_sub.unsqueeze(1)
                out = model(src, ys, src_mask, tgt_mask)
                prob = out[:, -1, :].log_softmax(dim=-1)
                next_word = prob.argmax(dim=-1, keepdim=True)
                ys = torch.cat([ys, next_word], dim=1)

            for i in range(batch_size):
                hyp_ids = ys[i].tolist()
                if eos_id in hyp_ids:
                    hyp_ids = hyp_ids[1 : hyp_ids.index(eos_id)]
                else:
                    hyp_ids = hyp_ids[1:]
                hypotheses.append(sp.decode(hyp_ids))

                tgt = batch["tgt"][i].tolist()
                if eos_id in tgt:
                    tgt = tgt[1 : tgt.index(eos_id)]
                else:
                    tgt = tgt[1:]
                references.append(sp.decode(tgt))

    bleu = calculate_bleu(references, hypotheses)
    model.train()
    return bleu


def main() -> None:
    """
    训练入口：负责组装数据管线、模型、优化器和 DDP 环境，
    并按照配置运行完整训练流程与周期性验证。
    """

    args = parse_args()
    cfg = load_config(args.config)
    set_seed(cfg.get("seed", 42))

    is_master, device = setup_distributed(args.local_rank)
    writer = SummaryWriter(log_dir=args.log_dir) if is_master else None
    train_cfg = cfg["training"]
    data_cfg = cfg["data"]

    rank = dist.get_rank() if args.local_rank != -1 else 0
    world_size = dist.get_world_size() if args.local_rank != -1 else 1

    train_loader, valid_loader, _, vocab_size = build_dataloaders(
        dataset_name=data_cfg["dataset_name"],
        lang_pair=data_cfg["lang_pair"],
        data_dir=data_cfg["data_dir"],
        vocab_size=data_cfg["vocab_size"],
        max_len=data_cfg["max_len"],
        batch_size=train_cfg["batch_size"],
        num_workers=data_cfg.get("num_workers", 2),
        distributed=args.local_rank != -1,
        rank=rank,
        world_size=world_size,
    )

    model, criterion = build_model_and_criterion(cfg, vocab_size, device)
    optimizer, scheduler = build_optimizer_and_scheduler(model, cfg)

    if args.local_rank != -1:
        model = DDP(model, device_ids=[args.local_rank], find_unused_parameters=False)

    scaler = torch.cuda.amp.GradScaler(enabled=train_cfg.get("mixed_precision", True))

    start_step = 0
    best_bleu = 0.0
    sp_model_path = os.path.join(data_cfg["data_dir"], f"spm_{data_cfg['vocab_size']}.model")

    if args.resume:
        start_step = load_checkpoint(
            args.resume, model.module if isinstance(model, DDP) else model, optimizer, scheduler
        )

    global_step = start_step
    optimizer.zero_grad(set_to_none=True)

    model_to_save = model.module if isinstance(model, DDP) else model

    if args.max_steps > 0:
        total_steps = args.max_steps
    else:
        total_steps = train_cfg["total_steps"]

    grad_accum_steps = train_cfg.get("grad_accum_steps", 1)
    log_interval = train_cfg.get("log_interval", 100)
    eval_interval = train_cfg.get("eval_interval", 1000)

    t_start = time.time()
    epoch = 0
    train_sampler = getattr(train_loader, "sampler", None)
    while global_step < total_steps:
        if args.local_rank != -1 and hasattr(train_sampler, "set_epoch"):
            train_sampler.set_epoch(epoch)
        for batch in train_loader:
            loss, lr = train_one_step(
                model,
                criterion,
                optimizer,
                scheduler,
                batch,
                device,
                scaler,
                grad_accum_steps,
                global_step,
                train_cfg.get("max_grad_norm", 1.0),
            )
            global_step += 1

            if is_master and global_step % log_interval == 0:
                tokens = batch["src"].numel() + batch["tgt"].numel()
                elapsed = time.time() - t_start
                toks_per_s = tokens * log_interval / (elapsed + 1e-9)
                grad_norm = get_grad_norm(model_to_save.parameters())
                print(
                    f"step {global_step} | loss {loss:.4f} | lr {lr:.6e} | "
                    f"grad_norm {grad_norm:.2f} | tok/s {toks_per_s:.1f}"
                )
                if writer is not None:
                    writer.add_scalar("train/loss", loss, global_step)
                    writer.add_scalar("train/lr", lr, global_step)
                    writer.add_scalar("train/grad_norm", grad_norm, global_step)
                    writer.add_scalar("train/tokens_per_s", toks_per_s, global_step)
                t_start = time.time()

            if is_master and global_step % eval_interval == 0:
                bleu = evaluate_bleu(
                    model_to_save,
                    valid_loader,
                    sp_model_path,
                    device,
                    data_cfg["max_len"],
                )
                print(f"[eval] step {global_step} | BLEU {bleu:.2f}")
                if writer is not None:
                    writer.add_scalar("eval/bleu", bleu, global_step)
                if bleu > best_bleu:
                    best_bleu = bleu
                    path = os.path.join(args.output_dir, f"step_{global_step}.pt")
                    save_checkpoint(path, model_to_save, optimizer, scheduler, global_step)
                    print(f"保存新最佳 checkpoint 到: {path}")

            if global_step >= total_steps:
                break
        epoch += 1

    if is_master:
        print("训练完成")
        if writer is not None:
            writer.close()


if __name__ == "__main__":
    main()
