# LangChain / LangGraph 学习示例

这组示例的目标不是重写主系统，而是帮你把“当前项目怎么做”和“LangChain / LangGraph 分别在里面扮演什么角色”串起来。

当前项目的真实情况是：

- 已经实际使用了 LangChain 相关能力
- 具体是 `ChatPromptTemplate`、`PydanticOutputParser`、`ChatOpenAI`
- 还没有真正把主流程写成 LangGraph 图

所以这组示例分成两层：

1. 先用 LangChain 解释当前项目已经在做什么
2. 再用一个简化 LangGraph 版本解释“如果把这套状态流写成图，会是什么样”

## 建议学习顺序

### 1. `example_01_prompt_and_parser.py`

学习目标：

- 理解 `ChatPromptTemplate` 是怎么组织提示词的
- 理解 `PydanticOutputParser` 为什么能把模型输出收敛成结构化对象
- 对应项目里的 `llm_understand_turn`

运行：

```bash
python examples/example_01_prompt_and_parser.py
```

如果没有配置 `OPENAI_API_KEY`，示例会直接提示并退出，不会报错。

你应该重点观察：

- prompt 里如何声明任务边界
- parser 如何定义输出 schema
- `chain = prompt | llm | parser` 这种链式写法是什么意思

### 2. `example_02_rule_plus_llm.py`

学习目标：

- 理解为什么项目不是“只靠模型”
- 理解规则提取、LLM 提取、结果合并三步
- 对应项目里的 `rule_understand_turn`、`llm_understand_turn`、`merge_nlu_results`

运行：

```bash
python examples/example_02_rule_plus_llm.py
```

你应该重点观察：

- 规则提取对确定格式字段更稳定
- LLM 作为补充理解器，而不是流程控制器
- 合并时为什么让规则覆盖模型结果

### 3. `example_03_state_machine_loop.py`

学习目标：

- 把项目里的核心算法骨架单独看清楚
- 理解 `process_user_turn -> understand -> update -> decide -> apply`
- 不引入 LangGraph，先看懂状态机本身

运行：

```bash
python examples/example_03_state_machine_loop.py
```

你应该重点观察：

- `SimpleState` 里哪些字段真正驱动流程
- `missing_slots` 如何决定系统继续追问还是进入确认
- `awaiting_confirmation` 如何把“确认”变成一个显式状态阶段

### 4. `example_04_langgraph_rewrite.py`

学习目标：

- 理解 LangGraph 的核心思路是“把状态流转拆成图节点”
- 理解为什么它适合表达多步 agent / workflow
- 把项目中的主链路映射到节点化执行

运行：

```bash
python examples/example_04_langgraph_rewrite.py
```

你应该重点观察：

- `StateGraph(GraphState)` 里的 `GraphState` 就是图里共享的状态
- 节点函数本质上仍是“读旧状态，产出新状态”
- 即便换成 LangGraph，核心仍然是状态推进，不是随意生成回复

## 和项目源码的映射关系

从示例回到真实项目，可以按下面方式理解：

- `example_01` 对应 [`dialogue_core.py`](/Users/Zhuanz/lvsoso/rnotes/code/agents/cake-booking/dialogue_core.py) 里的 `llm_understand_turn`
- `example_02` 对应 [`dialogue_core.py`](/Users/Zhuanz/lvsoso/rnotes/code/agents/cake-booking/dialogue_core.py) 里的规则理解 + LLM 理解 + 合并策略
- `example_03` 对应 [`dialogue_core.py`](/Users/Zhuanz/lvsoso/rnotes/code/agents/cake-booking/dialogue_core.py) 里的主状态机骨架
- `example_04` 不是当前主系统的真实实现，而是帮助你把 `example_03` 想象成图式工作流

## 建议你怎么对照源码学习

1. 先跑 `example_03_state_machine_loop.py`
2. 再去看 [`dialogue_core.py`](/Users/Zhuanz/lvsoso/rnotes/code/agents/cake-booking/dialogue_core.py) 的 `process_user_turn`
3. 再跑 `example_02_rule_plus_llm.py`
4. 再去看真实项目里的 `rule_understand_turn` 和 `llm_understand_turn`
5. 最后跑 `example_04_langgraph_rewrite.py`，把“状态机”转换成“图节点”来理解

## 一个最重要的认识

读这组代码时，建议你一直记住一句话：

> LangChain 主要帮你做“模型调用与结构化输出”，LangGraph 主要帮你做“多步状态流编排”。

而当前这个项目真正的核心，仍然是状态设计本身。
