(window.webpackJsonp=window.webpackJsonp||[]).push([[29],{427:function(t,v,a){"use strict";a.r(v);var _=a(5),r=Object(_.a)({},(function(){var t=this,v=t._self._c;return v("ContentSlotsDistributor",{attrs:{"slot-key":t.$parent.slotKey}},[v("h1",{attrs:{id:"大模型"}},[v("a",{staticClass:"header-anchor",attrs:{href:"#大模型"}},[t._v("#")]),t._v(" 大模型")]),t._v(" "),v("h2",{attrs:{id:"ai-infra"}},[v("a",{staticClass:"header-anchor",attrs:{href:"#ai-infra"}},[t._v("#")]),t._v(" AI Infra")]),t._v(" "),v("p",[t._v("分层")]),t._v(" "),v("ul",[v("li",[t._v("MaaS：产品")]),t._v(" "),v("li",[t._v("PaaS：平台")]),t._v(" "),v("li",[t._v("IaaS：基础设施")])]),t._v(" "),v("h2",{attrs:{id:"ai-model"}},[v("a",{staticClass:"header-anchor",attrs:{href:"#ai-model"}},[t._v("#")]),t._v(" AI Model")]),t._v(" "),v("ul",[v("li",[t._v("数据")]),t._v(" "),v("li",[t._v("算法")]),t._v(" "),v("li",[t._v("算力")])]),t._v(" "),v("p",[t._v("硬件和软件？")]),t._v(" "),v("h2",{attrs:{id:"llm-as-controller"}},[v("a",{staticClass:"header-anchor",attrs:{href:"#llm-as-controller"}},[t._v("#")]),t._v(" LLM as Controller")]),t._v(" "),v("h3",{attrs:{id:"hugginggpt"}},[v("a",{staticClass:"header-anchor",attrs:{href:"#hugginggpt"}},[t._v("#")]),t._v(" HuggingGPT")]),t._v(" "),v("ul",[v("li",[t._v("任务规划")]),t._v(" "),v("li",[t._v("模型选择")]),t._v(" "),v("li",[t._v("任务执行")]),t._v(" "),v("li",[t._v("生成结果")])]),t._v(" "),v("h3",{attrs:{id:"toolformer"}},[v("a",{staticClass:"header-anchor",attrs:{href:"#toolformer"}},[t._v("#")]),t._v(" Toolformer")]),t._v(" "),v("p",[t._v("使用多种外部工具。")]),t._v(" "),v("h3",{attrs:{id:"autogpt"}},[v("a",{staticClass:"header-anchor",attrs:{href:"#autogpt"}},[t._v("#")]),t._v(" AutoGPT")]),t._v(" "),v("p",[t._v("input->plan->assign->collect->output")]),t._v(" "),v("h3",{attrs:{id:"nexusgpt"}},[v("a",{staticClass:"header-anchor",attrs:{href:"#nexusgpt"}},[t._v("#")]),t._v(" NexusGPT")]),t._v(" "),v("p",[t._v("每个Agent实际上可以认为是一个人，每个agent擅长不同的事情，那么一个庞大的组织架构可以通过雇佣擅长各种能力的Agent来维持组织的正常运转。")]),t._v(" "),v("h3",{attrs:{id:"generative-agents"}},[v("a",{staticClass:"header-anchor",attrs:{href:"#generative-agents"}},[t._v("#")]),t._v(" Generative Agents")]),t._v(" "),v("p",[t._v("生成式智能体。")]),t._v(" "),v("p",[t._v("https://zhuanlan.zhihu.com/p/640725385?utm_id=0")]),t._v(" "),v("h3",{attrs:{id:"批量处理"}},[v("a",{staticClass:"header-anchor",attrs:{href:"#批量处理"}},[t._v("#")]),t._v(" 批量处理")]),t._v(" "),v("p",[t._v("“将多个句子拼接到一块儿作为输入” 不等于 “批量处理”。")]),t._v(" "),v("p",[v("strong",[t._v("批量处理")]),t._v(" 一般说的是并行批量。")]),t._v(" "),v("p",[t._v("将多个相互独立的问题作为输入进行批量并行处理。")]),t._v(" "),v("ul",[v("li",[t._v("使用 bacth tokenizer，截断或者填充；")]),t._v(" "),v("li",[t._v("构造prompt序列；")]),t._v(" "),v("li",[t._v("生成；")]),t._v(" "),v("li",[t._v("需要等待所有的结果生成完毕了；")])]),t._v(" "),v("p",[t._v("加快速度？生成的结果长度不会相差太大。")]),t._v(" "),v("h3",{attrs:{id:"大模型推理加速"}},[v("a",{staticClass:"header-anchor",attrs:{href:"#大模型推理加速"}},[t._v("#")]),t._v(" 大模型推理加速")]),t._v(" "),v("p",[v("a",{attrs:{href:"https://pan.baidu.com/s/1hKlrHYe0BviQUopY3hUJ1g?pwd=3mv8",target:"_blank",rel:"noopener noreferrer"}},[t._v("资料"),v("OutboundLink")],1)]),t._v(" "),v("h4",{attrs:{id:"基本结构"}},[v("a",{staticClass:"header-anchor",attrs:{href:"#基本结构"}},[t._v("#")]),t._v(" 基本结构")]),t._v(" "),v("ul",[v("li",[t._v("Layernorm")]),t._v(" "),v("li",[t._v("Attention")]),t._v(" "),v("li",[t._v("Silu")]),t._v(" "),v("li",[t._v("MatMul")]),t._v(" "),v("li",[t._v("Rotary Embedding")]),t._v(" "),v("li",[t._v("KV Cache")])]),t._v(" "),v("p",[t._v("大部分计算量在矩阵乘法。")]),t._v(" "),v("h4",{attrs:{id:"推理"}},[v("a",{staticClass:"header-anchor",attrs:{href:"#推理"}},[t._v("#")]),t._v(" 推理")]),t._v(" "),v("ul",[v("li",[t._v("Prefill -> 大部分时间")]),t._v(" "),v("li",[t._v("Decoding")])]),t._v(" "),v("p",[t._v("子过程构成：")]),t._v(" "),v("ul",[v("li",[t._v("Tokenize 将文本转换为向量 CPU")]),t._v(" "),v("li",[t._v("Computing 模型推理 GPU")]),t._v(" "),v("li",[t._v("Detokenize 将向量转为文本 CPU")]),t._v(" "),v("li",[t._v("Sampling 依据推理结果进行采样")])]),t._v(" "),v("p",[t._v("优化：")]),t._v(" "),v("ul",[v("li",[t._v("流水线策略")]),t._v(" "),v("li",[t._v("高效算子")]),t._v(" "),v("li",[t._v("动态批处理：merge step 混合多个用户的，Decoding Attention？")]),t._v(" "),v("li",[t._v("VM Allocator： 显存的分配优化（最大分配、页框、VM Allocator 预测的方式）")]),t._v(" "),v("li",[t._v("显存不够切到内存？通讯带宽太低、切换操作时间长、阻塞CPU？")]),t._v(" "),v("li",[t._v("KV Cache 量化：每个用户都有自己的kvcache，占用大部分的显存空间、限制系统的并发请求数，进行量化压缩减少占用。")]),t._v(" "),v("li",[t._v("矩阵乘法量化：服务端 int8 加速运算（计算密集），INT4 Weight Only 量化适用访存密集型的矩阵乘法")])]),t._v(" "),v("p",[t._v("页框无上限？不好估计用户容量？swap机制？")]),t._v(" "),v("p",[t._v("INT4 Weight Only 在batch大的情况下，  解量化、计算都占很多时间 ？终端多使用int4")]),t._v(" "),v("p",[t._v("FP8： https://zhuanlan.zhihu.com/p/574825662")]),t._v(" "),v("h4",{attrs:{id:"硬件"}},[v("a",{staticClass:"header-anchor",attrs:{href:"#硬件"}},[t._v("#")]),t._v(" 硬件")]),t._v(" "),v("ul",[v("li",[t._v("根据模型结构可以预估所有算子的计算量和访存需求，进而预估推理性能；")])]),t._v(" "),v("h4",{attrs:{id:"benchmark"}},[v("a",{staticClass:"header-anchor",attrs:{href:"#benchmark"}},[t._v("#")]),t._v(" Benchmark")]),t._v(" "),v("ul",[v("li",[t._v("Thougtput（吞吐量）：同一时间多个输入，测量prefill、decodeing")]),t._v(" "),v("li",[t._v("First Token Latency（首字延迟）：多长时间才能给出响应，prefill阶段")]),t._v(" "),v("li",[t._v("Latency（延迟）：每个decoding时间")]),t._v(" "),v("li",[t._v("QPS（每秒请求数量）： K / 完成K个请求的时间")])]),t._v(" "),v("p",[t._v("影响因素：")]),t._v(" "),v("ul",[v("li",[t._v("batch")]),t._v(" "),v("li",[t._v("input len")])])])}),[],!1,null,null,null);v.default=r.exports}}]);