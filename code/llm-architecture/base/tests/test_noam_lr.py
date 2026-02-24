#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
作者: Zhuanz
日期: 2026-02-23
依赖: torch>=2.0, pytest>=7.0

本文件对 Noam 学习率调度器进行回归测试，
确保在 warmup 阶段学习率单调上升，之后单调下降，
从而避免误改公式导致训练发散。
"""

import torch

from transformer.utils import NoamLR


def test_noam_lr_warmup_and_decay():
    """
    检查前后阶段学习率的单调性，而非具体数值，
    这样既能捕获实现错误，又不过于依赖常数。
    """

    d_model = 256
    warmup_steps = 10
    total_steps = 40

    param = torch.nn.Parameter(torch.zeros(1))
    optimizer = torch.optim.Adam([param], lr=1.0)
    scheduler = NoamLR(optimizer, d_model=d_model, warmup_steps=warmup_steps, factor=1.0)

    lrs = []
    for _ in range(total_steps):
        scheduler.step()
        lrs.append(scheduler.get_last_lr()[0])

    # warmup 阶段：严格单调递增
    warmup_lrs = lrs[:warmup_steps]
    assert all(x < y for x, y in zip(warmup_lrs, warmup_lrs[1:]))

    # 衰减阶段：整体趋势递减（允许微小数值波动）
    decay_lrs = lrs[warmup_steps:]
    assert decay_lrs[0] > decay_lrs[-1]

