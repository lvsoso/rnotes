# 安装：pip install langchain langchain-openai
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

# 代码示例：LangChain 基础用法（概念演示）
print("=== LangChain 核心概念 ===\n")

# 1. Prompt Templates
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "你是一个专业的{role}。"),
    ("human", "{user_input}")
])

# 格式化提示词
formatted = prompt_template.format_messages(
    role="天气助手",
    user_input="北京今天天气怎么样？"
)

print("1. Prompt Template:")
for msg in formatted:
    print(f"  [{msg.type}] {msg.content}")

# 2. 链式调用概念
print("\n2. 链式调用（Chain）:")
print("""
  User Input
      ↓
  [Prompt Template] → 格式化输入
      ↓
  [LLM] → 生成响应
      ↓
  [Output Parser] → 解析输出
      ↓
  Final Response
""")

# 3. 工具调用概念
print("3. Tools（工具）:")
tools_example = """
  - 搜索工具: 查询实时信息
  - 计算器工具: 执行数学运算
  - 数据库工具: 查询数据库
  - API 工具: 调用外部 API
"""
print(tools_example)

# LangChain 架构
print("\n4. LangChain 架构层次:")
print("""
  ┌─────────────────────────────────┐
  │   Applications (应用层)         │
  │   - Chatbots, Agents, QA系统   │
  ├─────────────────────────────────┤
  │   Chains (链式调用层)           │
  │   - LLMChain, SequentialChain  │
  ├─────────────────────────────────┤
  │   Components (组件层)           │
  │   - Prompts, LLMs, Tools       │
  ├─────────────────────────────────┤
  │   Models (模型层)               │
  │   - OpenAI, Anthropic, etc     │
  └─────────────────────────────────┘
""")