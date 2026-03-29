# 蛋糕预定系统学习教程

这份教程不是抽象的架构空谈，而是基于当前仓库里的真实实现来讲解这个系统是怎么工作的、为什么这样设计，以及状态机算法是如何驱动整段对话的。

当前仓库的真实入口非常轻：

- [`main.py`](/Users/Zhuanz/lvsoso/rnotes/code/agents/cake-booking/main.py) 只负责启动 CLI
- [`dialogue_core.py`](/Users/Zhuanz/lvsoso/rnotes/code/agents/cake-booking/dialogue_core.py) 承担几乎全部核心逻辑
- [`tests/test_dialogue_core.py`](/Users/Zhuanz/lvsoso/rnotes/code/agents/cake-booking/tests/test_dialogue_core.py) 是理解系统行为的最好辅助材料

这也意味着，如果你之前看到过“主逻辑都在 `main.py`”这一类描述，那已经不符合当前代码结构了。当前系统已经把核心职责收敛到了 `dialogue_core.py`。

## 1. 先理解这个系统在解决什么问题

这个项目实现的是一个任务导向型对话系统，业务范围被故意限制得很小，只处理两件事：

- `book_order`：创建蛋糕订单
- `modify_order`：修改已有订单

这个限制不是“能力不足”，而是一个典型的工程取舍：

1. 业务边界越清晰，状态机越稳定。
2. 可以把对话中的“自由表达”收敛成有限槽位。
3. 可以把最终动作限制为少数几个可验证的业务工具。
4. 当 LLM 不可用时，规则系统仍然能跑通主流程。

所以这个系统的设计理念不是“让模型自己决定一切”，而是：

- 用显式状态保存会话上下文
- 用规则优先保证确定性
- 用 LLM 做增强理解，而不是做流程控制
- 用状态机统一驱动“下一步该问什么、该确认什么、该执行什么”

你可以把它理解成一句话：

> 模型负责“理解用户说了什么”，状态机负责“系统接下来做什么”。

## 2. 代码结构为什么这样拆

从结构上看，当前系统虽然在一个核心文件里，但内部其实已经分成了几个清晰层次。

### 2.1 入口层：只负责启动

[`main.py`](/Users/Zhuanz/lvsoso/rnotes/code/agents/cake-booking/main.py) 很简单：

```python
from dialogue_core import run_cake_booking_agent

if __name__ == "__main__":
    run_cake_booking_agent()
```

这里体现的是一个很好的设计习惯：入口文件不承载业务逻辑，只负责调用真正的应用入口。这样有两个直接好处：

- 测试时不需要从 CLI 入口切入
- 核心逻辑可以被复用、单测、重构

### 2.2 数据模型层：先定义“系统记住什么”

在 [`dialogue_core.py`](/Users/Zhuanz/lvsoso/rnotes/code/agents/cake-booking/dialogue_core.py) 里，最先出现的核心对象是这些 Pydantic 模型：

- `ModelConfig`
- `NLUResult`
- `DialogueState`
- `ActionDecision`
- `LLMExtraction`

这几个模型分别代表不同层次的“结构化信息”。

#### `ModelConfig`

它只负责读取模型配置，例如模型名、温度、超时、API Key、Base URL。这个对象的价值在于把环境变量读取集中处理，而不是把 `os.getenv(...)` 散落到业务代码各处。

#### `NLUResult`

它表示“这一轮用户输入被理解成了什么”。里面最关键的字段有：

- `task`：用户当前想做的是预定还是改单
- `slots`：本轮识别到的槽位
- `slot_patch`：改单场景下，这一轮想修改的字段
- `user_goal_changed`：用户是否切换了任务目标
- `confidence`：理解置信度

这个对象很重要，因为它把“理解”从“状态更新”里拆开了。也就是说，系统先理解用户说了什么，再决定要不要把它写入当前状态。

#### `DialogueState`

这是整个状态机的状态载体，也是本系统最值得认真理解的对象。它不是一个简单的“当前步骤编号”，而是一组共同决定系统行为的状态字段。

最关键的字段有：

- `active_task`：当前任务类型
- `confirmed_slots`：已经确认可用的槽位
- `pending_slots`：本轮提取出的候选槽位
- `missing_slots`：当前还缺哪些信息
- `expected_slot`：系统当前最希望用户补充哪个槽位
- `awaiting_confirmation`：是否处于“等待用户确认执行”的阶段
- `system_response`：系统当前要回复的话
- `business_error` / `invalid_slot_message`：错误信息

这就是本系统的核心思想之一：

> 状态不是一个单独的枚举值，而是多个字段组合出来的“业务上下文状态”。

#### `ActionDecision`

它代表“系统下一步决定做什么”。可选动作只有五类：

- `ask_slot`
- `clarify`
- `confirm`
- `execute_tool`
- `respond_error`

这五个动作相当于状态机里的“边”，它们决定系统是继续追问、澄清、确认、执行业务，还是返回错误。

### 2.3 业务工具层：只做业务，不管对话

`CakeBookingTools` 是一个很典型的 mock 工具层，提供：

- `create_order`
- `query_order`
- `modify_order`
- `clear`

这里的重点不是“数据库设计”，而是职责边界：

- 工具层只关心订单数据的创建、查询、修改
- 它不决定下一句问什么
- 它不负责多轮对话
- 它只接受参数并返回结构化结果

这让状态机和业务动作解耦了。

### 2.4 理解层：把自然语言变成结构化槽位

理解层由两类函数组成。

第一类是规则解析和归一化：

- `normalize_cake_type`
- `normalize_size`
- `normalize_phone`
- `extract_order_id`
- `extract_contact_name`
- `parse_pickup_time`
- `resolve_modify_patch`

第二类是总控理解函数：

- `rule_understand_turn`
- `llm_understand_turn`
- `merge_nlu_results`
- `bind_expected_slot_if_needed`
- `understand_turn`

设计上它体现出一个明确策略：

1. 先用规则提取
2. 再用 LLM 补充理解
3. 最后以规则结果优先覆盖 LLM

这不是偶然，而是为了可控性。比如尺寸、手机号、订单号、时间这种字段，本来就适合规则解析，没必要交给模型自由发挥。

### 2.5 决策与执行层：状态机真正发生的地方

决定系统行为的主链路是：

```python
process_user_turn
  -> understand_turn
  -> update_dialogue_state
  -> decide_next_action
  -> apply_action
```

这一条链路就是整个系统的“算法骨架”。

## 3. 系统设计理念：为什么不是全靠 LLM

很多人第一次看这类系统时，会问一个问题：既然已经接了 LLM，为什么还要写这么多规则和状态字段？

答案是因为这套系统的目标不是“看起来聪明”，而是“流程可靠”。

如果完全把流程交给模型，你会遇到这些问题：

- 模型可能跳过必填信息
- 模型可能误解改单和新建单
- 模型可能在用户没确认前直接执行
- 模型可能把上下文中的旧值和本轮新值混在一起
- 模型很难稳定地做相同的状态推进

当前实现的解决方案是把责任拆开：

- 规则和 LLM 负责识别任务、槽位、修改意图
- `update_dialogue_state` 负责把识别结果落到状态里
- `decide_next_action` 负责判断下一步流程
- `apply_action` 负责副作用和回复文本

这样做之后，LLM 就不再是“流程大脑”，而是“输入理解器”。

## 4. 当前系统的代码结构图

可以把整个系统抽象成下面这张图：

```text
用户输入
  -> preprocess_user_input
  -> understand_turn
       -> rule_understand_turn
       -> llm_understand_turn（可选）
       -> merge_nlu_results
       -> bind_expected_slot_if_needed
  -> update_dialogue_state
  -> decide_next_action
  -> apply_action
       -> execute_business_action（必要时）
  -> 返回新的 DialogueState
```

这条链路说明了一个关键事实：

> 系统每轮并不是“直接回一句话”，而是“先生产下一状态，再由状态推出回复”。

这正是状态机思维。

## 5. 状态机算法到底是什么

这一部分是本教程的重点。

### 5.1 这个系统的状态机不是“节点图”，而是“字段驱动”

有些状态机会显式定义很多状态名，比如：

- `INIT`
- `ASK_CAKE_TYPE`
- `ASK_SIZE`
- `ASK_TIME`
- `CONFIRM`
- `DONE`

但当前系统没有这样做。它采用的是另一种常见工程方式：**用状态字段组合隐式表达状态**。

例如：

- 当 `active_task is None` 时，系统还没进入业务任务
- 当 `active_task == "book_order"` 且 `missing_slots` 不为空时，系统处于补槽阶段
- 当 `awaiting_confirmation == True` 时，系统处于确认阶段
- 当执行成功后 `active_task` 被清空时，系统回到空闲态

这类设计更灵活，因为它不需要为每一个业务步骤都定义独立状态名。

### 5.2 状态机的核心状态变量

理解这个系统，重点看五个字段：

#### `active_task`

当前正在做哪类任务。

- `None`：还没有任务
- `"book_order"`：正在新建订单
- `"modify_order"`：正在修改订单

它决定整个流程走哪条业务分支。

#### `confirmed_slots`

已经通过校验、可以被系统信任的槽位。

例如在预定任务中，最终需要：

- `cake_type`
- `size`
- `pickup_time`
- `contact_name`
- `contact_phone`

在改单任务中，首先必须有：

- `order_id`

之后还需要至少一个可修改字段：

- `cake_type`
- `size`
- `pickup_time`

#### `missing_slots`

这是状态机非常关键的派生状态。它不是用户直接输入的，而是通过 `calculate_missing_slots` 根据当前任务和已确认槽位推导出来的。

例如：

- 新建订单时缺口味，就继续问口味
- 已有订单号但没有修改内容时，改单任务仍然缺 `modification_fields`

也就是说，`missing_slots` 决定了系统是否进入确认态，还是继续追问。

#### `expected_slot`

这个字段表示“系统当前最期待用户补哪个字段”。它的作用主要有两个：

1. 生成更具体的追问文案
2. 当用户只回复一个裸值时，帮助系统绑定到正确槽位

比如系统刚问完联系人姓名，用户只回复“张三”，这时就可以结合 `expected_slot == "contact_name"` 把它识别为姓名。

#### `awaiting_confirmation`

这是确认态开关。

- `False`：还在收集信息或处理错误
- `True`：信息已经齐了，等待用户“确认”或“取消”

这个字段的存在让“确认执行”成为状态机中的一个显式阶段，而不是一段普通回复文本。

### 5.3 主算法逐步拆解

下面按真实代码顺序解释每个阶段。

#### 第一步：`process_user_turn`

[`dialogue_core.py`](/Users/Zhuanz/lvsoso/rnotes/code/agents/cake-booking/dialogue_core.py) 中的 `process_user_turn` 是单轮驱动入口。

它做的事可以概括成五步：

1. 预处理输入
2. 处理退出逻辑
3. 把用户消息写入历史
4. 做理解、更新状态、决策动作
5. 应用动作并返回新状态

这意味着本系统不是“命令式地到处跳函数”，而是固定遵守同一轮处理管线。

#### 第二步：`understand_turn`

这个阶段只负责理解用户输入，不直接产生系统回复。

具体是：

1. `rule_understand_turn` 先基于规则识别任务和槽位
2. `llm_understand_turn` 在可用时进一步理解复杂表达
3. `merge_nlu_results` 合并两个结果，且规则覆盖 LLM
4. `bind_expected_slot_if_needed` 在“用户只回一个值”时做补绑

这里有一个值得注意的设计点：`rule_understand_turn` 在改单任务下会额外调用 `resolve_modify_patch`。这让“改大一点”“提前一天”“推迟两小时”这种修改表达，能被转换成结构化 patch。

#### 第三步：`update_dialogue_state`

这是把 NLU 结果正式写进 `DialogueState` 的阶段。

它做了几件事：

1. 写入 `pending_slots`
2. 如果用户切换任务，则调用 `reset_for_new_task`
3. 对 `slots` 和 `slot_patch` 逐个做校验
4. 合法值写入 `confirmed_slots`
5. 非法值写入 `invalid_slot_message`
6. 重新计算 `missing_slots`
7. 如果原来的 `expected_slot` 已不再缺失，则清空它

注意这里一个很重要的工程思想：

> 识别出来不等于确认成功，只有校验通过才会进入 `confirmed_slots`。

这保证了后续流程基于的是可信数据。

#### 第四步：`decide_next_action`

这里是真正的决策中心，也最接近“状态机转移函数”。

它的决策顺序大致是：

1. 如果有业务错误，返回 `respond_error`
2. 如果有槽位校验错误，返回 `respond_error`
3. 如果只是寒暄且没进入任务，返回 `clarify`
4. 如果当前没有任务，返回 `clarify`
5. 如果改单但订单不存在，返回 `respond_error`
6. 如果正在等待确认：
   - 用户确认 -> `execute_tool`
   - 用户取消 -> `clarify`
   - 其他输入 -> 继续 `confirm`
7. 如果还有缺失槽位 -> `ask_slot`
8. 否则 -> `confirm`

你可以把它看成下面这个简化伪代码：

```text
if 错误:
    返回错误
elif 没有任务:
    进入澄清
elif 正在确认:
    根据确认/取消/其他输入分流
elif 还有缺失槽位:
    继续追问
else:
    进入确认态
```

这就是一个非常典型的状态转移函数。

#### 第五步：`apply_action`

如果说 `decide_next_action` 决定了“边”，那 `apply_action` 就负责真正完成“状态跃迁”。

不同动作会更新不同字段：

- `clarify`
  - 生成澄清回复
  - 某些取消场景下清空任务状态
- `ask_slot`
  - 设置 `expected_slot`
  - 关闭确认态
- `confirm`
  - 设置 `awaiting_confirmation = True`
  - 生成确认文案
- `respond_error`
  - 生成错误回复
  - 保持当前任务上下文，允许用户继续纠正
- `execute_tool`
  - 调用 `execute_business_action`
  - 成功后清空任务相关状态
  - 失败则保留错误信息

所以整套状态机并不神秘，本质上就是：

> 用 `decide_next_action` 计算下一步，用 `apply_action` 写回下一状态。

## 6. 为什么说这是“槽位填充 + 状态推进”

这个系统不是开放聊天，而是典型的 slot-filling system。

### 6.1 新建订单所需槽位

在 `TASK_REQUIRED_SLOTS` 中，`book_order` 需要：

- `cake_type`
- `size`
- `pickup_time`
- `contact_name`
- `contact_phone`

只要这些槽位没齐，系统就不会执行下单。

### 6.2 修改订单所需槽位

`modify_order` 的硬性入口是：

- `order_id`

但这还不够。`calculate_missing_slots` 里有一个额外约束：

- 如果只有 `order_id`
- 且 `cake_type` / `size` / `pickup_time` 都没有变化
- 那么还缺一个虚拟槽位 `modification_fields`

这里的 `modification_fields` 不一定真的存入订单，它更像一个流程控制槽位，表示“用户还没说明到底要改什么”。

这是一个很值得学习的小技巧：

> 有些槽位不是业务数据本身，而是为了驱动状态机而存在的流程槽位。

## 7. 规则系统是怎么做自然语言解析的

### 7.1 简单字段：直接归一化

以下字段都适合规则提取：

- 口味：`normalize_cake_type`
- 尺寸：`normalize_size`
- 手机号：`normalize_phone`
- 订单号：`extract_order_id`
- 联系人：`extract_contact_name`

这种设计很实用，因为这些字段的格式比较稳定，完全没必要让模型来猜。

### 7.2 时间字段：规则更复杂

`parse_pickup_time` 同时支持：

- 绝对时间：`2026-03-20 15:00`
- 相对时间：`明天下午三点`、`后天10点半`

它的做法是：

1. 先尝试匹配绝对格式
2. 再识别“明天/后天”
3. 再把中文小时替换成阿拉伯数字
4. 解析上午/下午/中午/晚上
5. 最终转成统一格式 `YYYY-MM-DD HH:MM`

这个函数说明一个很重要的现实：

> 对话系统里的“时间理解”通常不是一个小功能，而是单独的复杂点。

### 7.3 改单 patch：相对修改的核心

`resolve_modify_patch` 是改单逻辑的关键。

它先提取显式修改：

- 改成 10 寸
- 改到明天下午三点
- 改成草莓

如果没有直接提取到，再结合当前订单做相对变化：

- “大一点” -> 尺寸上调
- “小一点” -> 尺寸下调
- “早一点” -> 提前 1 小时
- “晚一点” -> 延后 1 小时
- “提前一天” -> 日期减 1 天
- “推迟两小时” -> 时间加 2 小时

这一步非常值得学习，因为它说明改单不是“重新收集整张订单”，而是“基于已有订单计算变更补丁”。

## 8. 两条完整流程带你看懂状态机

下面用两个完整示例来推演。

### 8.1 示例一：新建订单

用户说：

```text
我要预定蛋糕
```

系统理解后：

- `active_task = "book_order"`
- `confirmed_slots = {}`
- `missing_slots = ["cake_type", "size", "pickup_time", "contact_name", "contact_phone"]`
- 决策为 `ask_slot`
- `expected_slot = "cake_type"`

所以系统回复类似：

```text
请告诉我想订的蛋糕口味，例如巧克力、草莓、抹茶。
```

用户再说：

```text
巧克力
```

这时：

- `rule_understand_turn` 识别出 `cake_type=巧克力`
- `update_dialogue_state` 校验通过，写入 `confirmed_slots`
- `missing_slots` 被重新计算
- 下一步缺的是 `size`
- 系统继续 `ask_slot`

如果后面用户依次输入：

```text
6寸
2026-03-20 15:00
我叫张三
13812345678
```

当最后一个必填槽位齐全后：

- `missing_slots = []`
- `decide_next_action` 返回 `confirm`
- `awaiting_confirmation = True`

此时系统会生成确认文案，而不是直接创建订单。

用户说：

```text
确认
```

这时才会：

- 命中确认态分支
- 返回 `execute_tool`
- 调用 `CakeBookingTools.create_order`
- 成功后清空任务状态，回到空闲态

这就是一个完整的“补槽 -> 确认 -> 执行”闭环。

### 8.2 示例二：修改订单

用户说：

```text
我要修改订单
```

系统进入改单任务：

- `active_task = "modify_order"`
- `missing_slots = ["order_id"]`
- `expected_slot = "order_id"`

用户输入订单号后，系统会继续问修改内容。

这里的关键是：即使已经拿到 `order_id`，也还不能确认，因为还没有真实变更。

接下来用户说：

```text
改大一点
```

如果订单原尺寸是 `8寸`，则：

- `resolve_modify_patch` 读取已有订单
- 识别到“大一点”
- 调用 `shift_size(current_size, "up")`
- 得到 `10寸`
- 将 `size=10寸` 作为 patch 写入状态

这时系统不会直接修改，而是进入确认态，并展示差异：

```text
尺寸：8寸 -> 10寸
```

如果用户说“确认”，才真正调用 `modify_order`。

这说明改单流程的本质是：

1. 先定位旧订单
2. 再计算变更补丁
3. 再展示差异供用户确认
4. 最后才落库

## 9. 一个特别值得学习的设计：任务切换重置

函数 `reset_for_new_task` 用来处理用户中途换任务。

例如用户原本在预定蛋糕，已经说了口味，结果突然说“我要修改订单”，系统会：

- 把 `active_task` 切到 `modify_order`
- 清空旧任务不适用的槽位
- 重新开始改单流程

这里有一个细节很有意思：

如果切到 `book_order`，系统会尝试保留 `contact_name` 和 `contact_phone`。这是一种“有限保留上下文”的策略：

- 既避免错误复用无关槽位
- 又允许复用对新任务依然有意义的信息

这就是状态机设计里常见的“任务切换时选择性继承状态”。

## 10. 错误处理是怎么嵌进状态机的

本系统的错误处理并不是散在各处，而是被纳入主流程。

### 10.1 槽位错误

例如：

- 时间格式错误
- 时间早于当前时间两小时
- 手机号格式错误
- 订单号格式错误

这些在 `validate_slot_with_reason` 里产生明确原因，再由 `decide_next_action` 统一转成 `respond_error`。

### 10.2 业务错误

例如：

- 订单不存在
- 修改时没有任何实际变更
- 下单时缺参数

这些在工具层返回结果，再由执行层和决策层统一接住。

这背后的设计思想是：

> 错误不是“异常中断”，而是状态机里一种正常可处理的分支。

## 11. LLM 在这个系统里到底扮演什么角色

当前系统支持 `use_llm=True`，但又允许 `use_llm=False`。这说明系统并不依赖 LLM 才能运行。

`llm_understand_turn` 的职责是：

- 读取当前任务、期望槽位、已确认槽位、历史摘要
- 让模型输出结构化 JSON
- 作为规则系统的增强补充

但最终合并时，`merge_nlu_results` 会让规则结果覆盖模型结果。这个策略体现的是：

- 规则负责稳定字段
- LLM 负责补充复杂表达
- 决定权仍在可控逻辑里

如果你以后要扩展这个系统，这个边界最好保留住。不要轻易让模型直接决定是否执行订单操作。

## 12. 测试为什么是理解系统最好的材料

如果你已经看完代码，但还是对流程没有完全形成直觉，最好的下一步就是看测试。

[`tests/test_dialogue_core.py`](/Users/Zhuanz/lvsoso/rnotes/code/agents/cake-booking/tests/test_dialogue_core.py) 覆盖了很多关键行为：

- `test_multi_turn_booking_uses_expected_slot`
  - 展示预定流程如何一步步推进 `expected_slot`
- `test_booking_can_finish_and_create_order`
  - 展示新建订单的完整闭环
- `test_modify_order_requires_order_id_and_change_field`
  - 展示改单必须先拿到订单号，再说明修改内容
- `test_task_switch_clears_previous_booking_slots`
  - 展示切换任务时状态如何重置
- `test_modify_order_can_shift_size_relatively`
  - 展示“改大一点”如何映射成尺寸变化
- `test_modify_order_can_shift_time_relatively`
  - 展示“推迟两小时”“提前一天”的 patch 计算
- `test_invalid_relative_time_returns_explicit_error`
  - 展示非法时间如何返回清晰错误
- `test_negative_confirmation_cancels_task`
  - 展示确认态里的取消分支

可以这样理解：

> 测试不是附属品，而是这个状态机行为定义的一部分。

## 13. 如果你想继续深入，建议按这个顺序读代码

建议你第二遍阅读源码时，按下面顺序看，而不是从头机械扫过去：

1. 先看 `DialogueState`
2. 再看 `process_user_turn`
3. 再看 `decide_next_action`
4. 再看 `apply_action`
5. 再看 `update_dialogue_state`
6. 最后回头看各种 `normalize_*` 和 `resolve_modify_patch`

原因很简单：

- 先看状态，才能知道系统记住什么
- 再看主流程，才能知道状态怎么流动
- 再看决策和执行，才能知道状态怎么改变
- 最后看规则细节，才不会陷进局部实现

## 14. 这套设计有什么优点和代价

最后做一个工程角度的总结。

### 优点

- 流程可控，确认执行边界清晰
- 无 LLM 时仍可运行主链路
- 规则字段稳定，易于测试
- 状态对象集中，便于调试
- 单轮入口统一，便于后续扩展

### 代价

- 核心逻辑仍集中在一个大文件中，继续增长后需要拆模块
- 状态是“字段组合状态”，理解门槛比显式枚举状态略高
- 时间解析和改单 patch 逻辑会随着需求增长变复杂
- 当前工具层是内存 mock，不是真实持久化系统

## 15. 你应该真正带走的几个理解点

读完这份教程，如果你只记住几个最关键的点，那应该是这几个：

1. 这个系统的核心不是 LLM，而是 `DialogueState`
2. 这个系统的算法主线不是“生成回复”，而是“推进状态”
3. `decide_next_action` 是最像状态机转移函数的地方
4. `apply_action` 是真正完成状态跃迁和副作用的地方
5. 单改订单不是重填整单，而是基于旧订单计算 patch
6. 测试文件就是这套对话状态机的行为说明书

如果你能把这六点串起来，这个系统的设计基本就算真正看懂了。
