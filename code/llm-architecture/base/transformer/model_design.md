# 轻量级 Transformer 各层设计与作用说明

> 目录基于项目根目录 `/Users/Zhuanz/lvsoso/rnotes/code/llm-architecture/base`，模型代码主要位于 `transformer/model.py`。

本文档不再重复代码实现细节，而是从**功能与设计动机**角度解释各个子模块的作用，方便你阅读与二次修改。

---

## 1. 输入与表示层

对应代码：`Transformer.encoder.embedding` / `Transformer.decoder.embedding`、`PositionalEncoding`

- **Token Embedding**
  - 作用：将离散的 token id（由 SentencePiece 编码得到的子词）映射到 `d_model` 维度的连续向量空间。
  - 设计选择：
    - 使用 `nn.Embedding(vocab_size, d_model)`，是最直接也是最常用的做法。
    - 编码端和解码端在 vocab 相同且 `share_embeddings=True` 时权重共享，可以明显减少参数量，并鼓励源/目标语言共享词形结构信息。
  - 数值缩放：
    - 在送入位置编码前，将 embedding 乘以 `sqrt(d_model)`。
    - 原因：位置编码本身的数值范围与 embedding 初始化尺度不完全一致，这个缩放保证两者数值量级相近，有利于训练初期稳定。

- **PositionalEncoding（位置编码）**
  - 作用：为模型提供**序列位置信息**，使得纯基于注意力的结构仍能分辨 token 的先后顺序。
  - 设计选择：
    - 使用论文原版的 **sin/cos 三角函数位置编码**，而非可学习位置向量：
      - 优点：不增加可训练参数，外推到更长序列时有较好行为。
      - 形式：对偶数维使用 `sin(pos / 10000^{2i/d_model})`，奇数维使用 `cos(...)`。
    - 预先在 `max_len` 维度构造完整位置编码表，作为 `buffer` 存在，前向时只需切片加到当前 batch 上，计算开销小。

---

## 2. Multi-Head Attention（多头注意力）

对应代码：`MultiHeadAttention` 类

- **核心思想**
  - 将输入特征在通道维度上切分为 `n_heads` 个子空间，每个子空间独立做一次缩放点积注意力，然后再拼接。
  - 动机：
    - 不同头可以学习到不同的对齐模式（如短距、长距、语法、词义等），形成互补信息。
    - 并行计算，相比单头大维度注意力更易于训练收敛。

- **Q / K / V 投影**
  - 每条序列（例如 `src` 或 `tgt`）经过三套线性层生成 Query / Key / Value：
    - `w_q, w_k, w_v: Linear(d_model, d_model)`
  - 然后 reshape 为 `(batch, n_heads, seq_len, d_k)`：
    - 目的是在 head 维度上独立做注意力，提升表达能力。

- **缩放点积注意力**
  - 得分矩阵计算：`scores = QK^T / sqrt(d_k)`。
    - 缩放的目的：如果不除以 `sqrt(d_k)`，随着维度增大，内积值方差增大，softmax 区分度过高，对梯度不利。
  - 掩码（mask）：
    - 对 padding 或未来位置，用 `-inf` 填充得分，使 softmax 后概率接近 0，避免模型关注这些位置。

- **多头拼接与输出**
  - 每头得到的加权和 `head_output` 形状 `(batch, n_heads, seq_len, d_k)`。
  - 将 head 维度拼回 `(batch, seq_len, d_model)` 后，通过 `w_o` 线性层融合信息。
  - 这一层可视作对所有头输出的一个「再投影」，决定如何在头之间组合信息。

---

## 3. Positionwise Feed-Forward Network（位置前馈网络）

对应代码：`PositionwiseFeedForward`

- **作用**
  - 在每个位置上独立地应用一个两层全连接网络（`Linear -> ReLU -> Linear`），对单个 token 的表示进行非线性变换。
  - 与卷积不同，该模块不在时间维度上交互，只在通道维度上提升表示能力。

- **结构**
  - 第一层：`Linear(d_model, d_ff)`，将维度升高到 `d_ff`（通常 4×`d_model`）。
  - 激活函数：`ReLU`。
  - 第二层：`Linear(d_ff, d_model)`，再投影回 `d_model`。
  - Dropout：插入在中间，用于缓解过拟合。

- **设计动机**
  - 自注意力主要负责建模 **序列内依赖**（谁与谁相关）；FFN 则在每个位置上引入更强的非线性，从而提升表示能力。
  - 两者交替堆叠，使模型兼具**全局依赖建模**与**局部特征抽取**能力。

---

## 4. EncoderLayer：编码器基础层

对应代码：`EncoderLayer`

结构：  
`LayerNorm(x + Dropout(SelfAttention(x))) → LayerNorm(x + Dropout(FFN(x)))`

- **Self-Attention 子层**
  - 使用 `MultiHeadAttention`，`query = key = value = src`。
  - 通过自注意力，让每个源 token 的表示可以引用同一句中的其他 token 信息（如上下文、主谓宾关系）。

- **残差连接（Residual Connection）**
  - 将子层输出与输入相加：`x + sublayer(x)`。
  - 动机：
    - 缓解梯度消失/爆炸，使深层网络更易训练。
    - 保留原始表示，允许子层只学习“增量信息”。

- **LayerNorm**
  - 在残差相加后用 `LayerNorm` 规范化特征分布。
  - 作用：
    - 减少不同子层之间输出的尺度差异，稳定训练。
    - 与残差一起提高深层网络的可训练性。

- **FFN 子层**
  - 位置前馈网络对每个位置分别做非线性映射。
  - 同样通过残差 + LayerNorm 叠加回主干。

整体而言，一个 `EncoderLayer` 可以理解为：  
**先整体看一遍句子（Self-Attention），再对每个词的特征做非线性加工（FFN）**，中间借助残差与规范化保持稳定。

---

## 5. DecoderLayer：解码器基础层

对应代码：`DecoderLayer`

结构：  
`Masked Self-Attention → Enc-Dec Attention → FFN`（每步后都有残差 + LayerNorm）

- **Masked Self-Attention**
  - 与 Encoder 的 Self-Attention 类似，但加入**下三角 mask**：
    - 当前位置 `t` 只能看到 `≤ t` 的 token，不能预见未来。
  - 作用：
    - 保证自回归生成的条件独立假设：第 t 步的预测只依赖 t 之前的目标 token。

- **Encoder-Decoder Attention**
  - Query 来自解码器当前隐藏状态，Key/Value 来自编码器输出（即源句表示）。
  - 作用：
    - 在生成每个目标 token 时，显式“对齐”到源句中最相关的位置。
    - 可以类比传统机器翻译中的对齐矩阵。

- **FFN 子层**
  - 同 EncoderLayer，位置前馈网络提升表达能力。

解码器层的整体直观理解：  
**先回顾一下已经翻译的内容（Masked Self-Attn），再看看源句（Enc-Dec Attn），最后用 FFN 做非线性加工。**

---

## 6. Encoder 堆叠

对应代码：`Encoder`

- **Embedding + PosEncoding**
  - 先将 token id 映射到向量空间，并注入绝对位置信息。
  - 乘上 `sqrt(d_model)` 保持数值尺度。

- **多层 EncoderLayer 堆叠**
  - 通过 `nn.ModuleList` 存储 `n_layers` 个 `EncoderLayer`。
  - 每层都在前一层的基础上重新聚合全句信息。

- **最终 LayerNorm**
  - 在最顶层再做一次 LayerNorm，平衡所有层的输出。
  - 常见做法之一（另一种是每层前做 Norm，本实现采用的是残差后 Norm）。

最终 Encoder 输出可视作**源句的上下文表示**（memory），供 Decoder 查询。

---

## 7. Decoder 堆叠

对应代码：`Decoder`

与 Encoder 类似，但每层包含三部分：`Masked Self-Attn`、`Enc-Dec Attn`、`FFN`。

- **Embedding + PosEncoding**
  - 对目标端 token 进行嵌入和位置编码。

- **多层 DecoderLayer**
  - 每层都会利用上一层的解码状态和 encoder memory：
    - 随着层数增加，模型可以迭代地优化对齐和翻译结果。

- **最终 LayerNorm**
  - 同样在顶层输出前做一次 LayerNorm，稳定解码输出的分布。

---

## 8. 顶层 Transformer 与 Generator

对应代码：`Transformer` 类

- **整体结构**
  - `encode(src, src_mask)` → 得到 `memory`
  - `decode(tgt, memory, tgt_mask, src_mask)` → 得到解码器输出
  - `generator`（线性层）将 `d_model` 维度映射到 `tgt_vocab_size` 维 logits。

- **共享词嵌入（可选）**
  - 若源/目标 vocab 相同且开启 `share_embeddings`：
    - Encoder 和 Decoder 使用相同的 embedding 权重。
    - 理由：
      - 减少参数量。
      - 对于中英等词形差异较大的语种，仍然可以共享部分子词结构，有助于泛化。

- **训练目标**
  - 损失函数使用标签平滑交叉熵：
    - 输入：`logits`（模型输出）和 `tgt_out`（右移一位的目标序列）。
    - 标签平滑缓解模型对某个单一 token 的过度自信，提高泛化。

---

## 9. 掩码设计与自回归约束

掩码逻辑主要在 `transformer/utils.py` 和 `transformer/dataset.py` 中构造，这里从功能角度总结：

- **Padding 掩码**
  - 目的：避免注意力关注到 padding token。
  - 形状：`(batch, 1, 1, seq_len)`。
  - 使用方式：
    - 在注意力 scores 上用 `masked_fill(mask == 0, -inf)`，使得这些位置 softmax 后概率为 0。

- **Subsequent Mask（下三角 mask）**
  - 目的：保证解码阶段的自回归特性，禁止看到未来 token。
  - 形状：`(1, tgt_len, tgt_len)`，下三角为 True，上三角为 False。

- **目标端综合掩码**
  - `create_tgt_mask` 将 padding mask 与 subsequent mask 结合：
    - 既屏蔽 padding，又屏蔽未来位置。
  - 形状：`(batch, 1, tgt_len, tgt_len)`。

这种掩码设计确保了训练与推理时的概率模型假设：  
**在任意时间步，模型仅依赖于过往已生成的 token 和源句。**

---

## 10. 轻量化设计与可扩展性

当前实现保留了论文中所有关键结构，但在超参数上做了「小型化」处理：

- `d_model = 256`、`n_layers = 4`、`n_heads = 4`、`d_ff = 1024`。
  - 参数量约 20M 量级，在单张 8GB GPU 上训练相对轻松。
  - 对 IWSLT/WMT 级别任务仍有不错的建模能力。

你可以在 `transformer/config.yaml` 中修改以下参数以扩展模型：

- 增大 `d_model`（如 512）与 `n_layers`（如 6）：
  - 提升模型容量，但显存和训练时间显著增加。
- 调整 `n_heads` 与 `d_ff`：
  - 更多头数有助于捕获更丰富的注意力模式；
  - 更大的 `d_ff` 带来更强的非线性表达能力。

在扩展时建议：

1. 先用当前轻量配置验证训练流程与指标。
2. 再逐步增大规模，并观测参数量、显存占用与收敛速度。

---

如果你希望从「结构设计」角度进一步优化（例如改成 Pre-LN、加入相对位置编码、增加深度缩放因子等），可以以本文各层作用说明为基础，再对对应模块进行小步迭代。另有需求随时可以继续补充说明。 

