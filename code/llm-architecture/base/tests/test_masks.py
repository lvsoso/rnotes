#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
作者: Zhuanz
日期: 2026-02-23
依赖: torch>=2.0, pytest>=7.0

本文件测试掩码生成逻辑是否满足自回归与 padding 要求，
以保证注意力模块在训练和推理阶段不会“偷看未来”或关注到 padding。
"""

import torch

from transformer.utils import create_padding_mask, create_subsequent_mask, create_tgt_mask


def test_padding_mask_shape_and_values():
    """
    验证 padding mask 形状与数值分布是否符合预期。
    """

    pad_idx = 0
    seq = torch.tensor([[1, 2, pad_idx], [3, pad_idx, pad_idx]])
    mask = create_padding_mask(seq, pad_idx)
    assert mask.shape == (2, 1, 1, 3)
    # 非 padding 位置应为 True，padding 位置为 False
    assert mask[0, 0, 0].tolist() == [True, True, False]
    assert mask[1, 0, 0].tolist() == [True, False, False]


def test_subsequent_mask_lower_triangular():
    """
    验证下三角 mask 是否确实禁止看到未来位置。
    """

    size = 4
    mask = create_subsequent_mask(size)
    assert mask.shape == (1, size, size)
    # 主对角线及以下应为 1，上三角为 0
    for i in range(size):
        for j in range(size):
            if j <= i:
                assert mask[0, i, j]
            else:
                assert not mask[0, i, j]


def test_tgt_mask_combines_padding_and_causal():
    """
    目标端 mask 应同时考虑 padding 和自回归条件，
    即 padding 列整列为 False，对角线以上为 False。
    """

    pad_idx = 0
    tgt = torch.tensor([[1, 2, pad_idx], [1, pad_idx, pad_idx]])
    mask = create_tgt_mask(tgt, pad_idx)
    # 形状: (batch, 1, tgt_len, tgt_len)
    assert mask.shape == (2, 1, 3, 3)
    # 检查第一条样本最后一个位置被完全屏蔽
    assert mask[0, 0, :, 2].tolist() == [False, False, False]

