#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
作者: Zhuanz
日期: 2026-02-23

本包提供从零实现的 Encoder-Decoder Transformer 模型，
包含模型结构定义、数据加载、训练脚本与推理工具。
"""

from .model import Transformer

__all__ = ["Transformer"]

