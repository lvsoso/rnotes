#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
作者: Zhuanz
日期: 2026-02-23
依赖版本: datasets>=2.0, sentencepiece>=0.1, torch>=2.0
运行示例:
    构建数据集与 DataLoader:
        python -m transformer.dataset --dataset wmt17 --lang-pair zh-en

本文件负责机器翻译数据的下载、子词切分与批数据构造，
默认使用 HuggingFace datasets 加载 IWSLT/WMT 系列语料，
并基于 sentencepiece 训练 BPE 子词模型，便于跨语种共享词表。
"""

import argparse
import os
from dataclasses import dataclass
from typing import Dict, List, Tuple

import datasets
import sentencepiece as spm
import torch
from torch.utils.data import DataLoader, Dataset, DistributedSampler

from .utils import create_padding_mask, create_tgt_mask


SPECIAL_TOKENS = ["<pad>", "<bos>", "<eos>", "<unk>"]


def _get_spm_model_prefix(data_dir: str, vocab_size: int) -> str:
    """
    统一 sentencepiece 模型命名，方便在训练和推理阶段复用。
    """

    return os.path.join(data_dir, f"spm_{vocab_size}")


def train_sentencepiece(
    texts: List[str],
    data_dir: str,
    vocab_size: int = 16000,
) -> str:
    """
    在给定文本上训练 SentencePiece BPE 模型，
    通过子词分解缓解 OOV 问题并控制词表大小。
    """

    os.makedirs(data_dir, exist_ok=True)
    prefix = _get_spm_model_prefix(data_dir, vocab_size)
    model_path = prefix + ".model"
    if os.path.exists(model_path):
        return model_path

    corpus_path = os.path.join(data_dir, "spm_corpus.txt")
    with open(corpus_path, "w", encoding="utf-8") as f:
        for line in texts:
            f.write(line.strip() + "\n")

    # 训练 BPE 时显式指定特殊符号，确保它们具有固定 id 便于 mask 构造
    spm.SentencePieceTrainer.Train(
        input=corpus_path,
        model_prefix=prefix,
        vocab_size=vocab_size,
        model_type="bpe",
        character_coverage=1.0,
        user_defined_symbols=[],
        pad_id=0,
        bos_id=1,
        eos_id=2,
        unk_id=3,
    )
    return model_path


def load_sentencepiece(model_path: str) -> spm.SentencePieceProcessor:
    """
    加载已训练好的 SentencePiece 模型，供 tokenization 使用。
    """

    sp = spm.SentencePieceProcessor()
    sp.load(model_path)
    return sp


@dataclass
class TranslationExample:
    """
    轻量封装单个样本的 token 序列，方便类型检查与调试。
    """

    src_ids: List[int]
    tgt_ids: List[int]


class TranslationDataset(Dataset):
    """
    将原始字符串样本转换为 ID 序列，并裁剪到 max_len，
    同时添加 BOS/EOS 标记以适配自回归训练目标。
    """

    def __init__(
        self,
        split: str,
        dataset_name: str,
        lang_pair: str,
        data_dir: str,
        sp_model_path: str,
        max_len: int,
    ) -> None:
        super().__init__()
        self.split = split
        self.max_len = max_len
        self.sp = load_sentencepiece(sp_model_path)

        src_lang, tgt_lang = lang_pair.split("-")
        # 使用 datasets 统一加载语料，避免自行处理下载与缓存细节
        self.ds = datasets.load_dataset(dataset_name, lang_pair, cache_dir=data_dir)[
            split
        ]
        self.src_lang = src_lang
        self.tgt_lang = tgt_lang

    def __len__(self) -> int:
        return len(self.ds)

    def __getitem__(self, idx: int) -> TranslationExample:
        item = self.ds[idx]
        src_text = item["translation"][self.src_lang]
        tgt_text = item["translation"][self.tgt_lang]

        # 使用 sentencepiece 对两端统一编码，并添加 BOS/EOS 标记
        src_ids = [self.sp.bos_id()] + self.sp.encode(src_text, out_type=int)[: self.max_len - 2] + [self.sp.eos_id()]
        tgt_ids = [self.sp.bos_id()] + self.sp.encode(tgt_text, out_type=int)[: self.max_len - 2] + [self.sp.eos_id()]
        return TranslationExample(src_ids=src_ids, tgt_ids=tgt_ids)


def collate_fn(
    batch: List[TranslationExample],
    pad_id: int,
) -> Dict[str, torch.Tensor]:
    """
    自定义 collate 函数，用于在 DataLoader 中对 batch 做动态 padding，
    避免在所有样本上使用统一的最大长度造成显存浪费。
    """

    src_seqs = [torch.tensor(ex.src_ids, dtype=torch.long) for ex in batch]
    tgt_seqs = [torch.tensor(ex.tgt_ids, dtype=torch.long) for ex in batch]

    src_lens = [len(s) for s in src_seqs]
    tgt_lens = [len(s) for s in tgt_seqs]
    max_src_len = max(src_lens)
    max_tgt_len = max(tgt_lens)

    batch_size = len(batch)
    src_batch = torch.full(
        (batch_size, max_src_len), pad_id, dtype=torch.long
    )
    tgt_batch = torch.full(
        (batch_size, max_tgt_len), pad_id, dtype=torch.long
    )

    for i, (src, tgt) in enumerate(zip(src_seqs, tgt_seqs)):
        src_batch[i, : src.size(0)] = src
        tgt_batch[i, : tgt.size(0)] = tgt

    src_mask = create_padding_mask(src_batch, pad_id)
    tgt_mask = create_tgt_mask(tgt_batch, pad_id)

    return {
        "src": src_batch,
        "tgt": tgt_batch,
        "src_mask": src_mask,
        "tgt_mask": tgt_mask,
    }


def build_dataloaders(
    dataset_name: str,
    lang_pair: str,
    data_dir: str,
    vocab_size: int,
    max_len: int,
    batch_size: int,
    num_workers: int = 2,
    distributed: bool = False,
    rank: int = 0,
    world_size: int = 1,
) -> Tuple[DataLoader, DataLoader, DataLoader, int]:
    """
    构建 train/valid/test 三个 DataLoader，并返回词表大小，
    以保证模型嵌入层的 vocab_size 与实际 token id 一致。
    """

    os.makedirs(data_dir, exist_ok=True)
    raw_ds = datasets.load_dataset(dataset_name, lang_pair, cache_dir=data_dir)
    src_lang, tgt_lang = lang_pair.split("-")

    # 将训练集文本用于训练 SentencePiece，避免泄露验证/测试信息
    train_texts: List[str] = []
    for ex in raw_ds["train"]:
        train_texts.append(ex["translation"][src_lang])
        train_texts.append(ex["translation"][tgt_lang])
    sp_model_path = train_sentencepiece(train_texts, data_dir, vocab_size)
    sp = load_sentencepiece(sp_model_path)
    vocab_size = sp.get_vocab_size()

    train_set = TranslationDataset(
        split="train",
        dataset_name=dataset_name,
        lang_pair=lang_pair,
        data_dir=data_dir,
        sp_model_path=sp_model_path,
        max_len=max_len,
    )
    valid_set = TranslationDataset(
        split="validation",
        dataset_name=dataset_name,
        lang_pair=lang_pair,
        data_dir=data_dir,
        sp_model_path=sp_model_path,
        max_len=max_len,
    )
    test_split = "test" if "test" in raw_ds else "validation"
    test_set = TranslationDataset(
        split=test_split,
        dataset_name=dataset_name,
        lang_pair=lang_pair,
        data_dir=data_dir,
        sp_model_path=sp_model_path,
        max_len=max_len,
    )

    pad_id = sp.pad_id()

    train_sampler = None
    if distributed:
        train_sampler = DistributedSampler(
            train_set,
            num_replicas=world_size,
            rank=rank,
            shuffle=True,
        )
    train_loader = DataLoader(
        train_set,
        batch_size=batch_size,
        shuffle=train_sampler is None,
        sampler=train_sampler,
        num_workers=num_workers,
        collate_fn=lambda b: collate_fn(b, pad_id),
    )
    valid_loader = DataLoader(
        valid_set,
        batch_size=batch_size,
        shuffle=False,
        num_workers=num_workers,
        collate_fn=lambda b: collate_fn(b, pad_id),
    )
    test_loader = DataLoader(
        test_set,
        batch_size=batch_size,
        shuffle=False,
        num_workers=num_workers,
        collate_fn=lambda b: collate_fn(b, pad_id),
    )

    return train_loader, valid_loader, test_loader, vocab_size


def _parse_args() -> argparse.Namespace:
    """
    命令行工具，方便单独调试数据管线是否工作正常。
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=str, default="wmt17")
    parser.add_argument("--lang-pair", type=str, default="zh-en")
    parser.add_argument("--data-dir", type=str, default="./data/wmt17_zh_en")
    parser.add_argument("--vocab-size", type=int, default=16000)
    parser.add_argument("--max-len", type=int, default=64)
    parser.add_argument("--batch-size", type=int, default=32)
    return parser.parse_args()


def main() -> None:
    """
    简易自检入口: 构建一个小批次并打印张量形状，
    以验证 sentencepiece + DataLoader 流程是否打通。
    """

    args = _parse_args()
    train_loader, _, _, vocab_size = build_dataloaders(
        dataset_name=args.dataset,
        lang_pair=args.lang_pair,
        data_dir=args.data_dir,
        vocab_size=args.vocab_size,
        max_len=args.max_len,
        batch_size=args.batch_size,
    )
    print(f"词表大小: {vocab_size}")
    batch = next(iter(train_loader))
    for k, v in batch.items():
        print(k, v.shape)


if __name__ == "__main__":
    main()
