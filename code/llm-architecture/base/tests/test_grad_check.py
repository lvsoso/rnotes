#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
作者: Zhuanz
日期: 2026-02-23
依赖: torch>=2.0, pytest>=7.0

本文件对前馈子层进行有限差分梯度检查，
验证自动求导结果与数值梯度在容忍误差范围内一致，
从而提高实现正确性的信心。
"""

import torch

from transformer.model import PositionwiseFeedForward


def finite_diff_grad(module: torch.nn.Module, x: torch.Tensor, eps: float = 1e-3):
    """
    对输入 x 的单个维度使用中心差分估计梯度，
    这里只挑选一个维度以控制测试运行时间。
    """

    module.eval()
    x_pos = x.clone().detach()
    x_neg = x.clone().detach()
    idx = (0, 0, 0)
    x_pos[idx] += eps
    x_neg[idx] -= eps

    with torch.no_grad():
        y_pos = module(x_pos).sum()
        y_neg = module(x_neg).sum()

    num_grad = (y_pos - y_neg) / (2 * eps)
    return num_grad


def test_feedforward_grad_close_to_finite_diff():
    """
    验证前馈网络对输入梯度与有限差分近似的一致性。
    """

    torch.manual_seed(0)
    d_model = 8
    d_ff = 16
    module = PositionwiseFeedForward(d_model=d_model, d_ff=d_ff, dropout=0.0)

    x = torch.randn(1, 1, d_model, requires_grad=True)
    y = module(x).sum()
    y.backward()

    num_grad = finite_diff_grad(module, x.detach(), eps=1e-3)
    autograd_grad = x.grad[0, 0, 0]

    # 数值梯度与自动求导应在一定相对误差内接近
    assert torch.allclose(
        autograd_grad, num_grad, rtol=1e-2, atol=1e-3
    ), f"autograd={autograd_grad}, numeric={num_grad}"

