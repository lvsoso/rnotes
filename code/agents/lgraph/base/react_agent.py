import getpass
import os
from dotenv import load_dotenv

# from tmp.tool_agent import llm_with_tools  # 移除无效引用
load_dotenv()

from langchain_openai import ChatOpenAI
# from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode


llm = ChatOpenAI(
    model_name=os.getenv("LLM_MODEL_ID"),
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL"),
)

# 定义一个简单的计算工具
@tool
def calculator(expression: str) -> str:
    """计算数学表达式的值。例如: '2 + 2' 或 '3 * 4'"""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {e}"

# search = TavilySearchResults(max_results=2)
# tools = [search]
tools = [calculator]

llm_with_tools = llm.bind_tools(tools)

def agent(state: MessagesState):
    # 添加 ReAct 提示词
    system_message = """你是一个 ReAct (Reasoning + Acting) Agent。
处理用户问题时，请遵循以下步骤：
1. Thought（思考）：分析问题需要什么信息
2. Action（行动）：决定调用哪个工具
3. Observation（观察）：分析工具返回的结果
4. Answer（回答）：基于观察给出最终答案

始终展示你的推理过程。"""

    messages = [{"role": "system", "content": system_message}] + state["messages"]
    return {"messages": [llm_with_tools.invoke(messages)]}


def should_continue(state: MessagesState):
    last_message = state["messages"][-1]
    if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
        return "tools"
    return END

graph = StateGraph(MessagesState)
graph.add_node("agent", agent)
graph.add_node("tools", ToolNode(tools))

graph.add_edge(START, "agent")
graph.add_conditional_edges("agent", should_continue, ["tools", END])
graph.add_edge("tools", "agent")

app = graph.compile()

# 测试
print("Starting ReAct Agent...")
response = app.invoke({
    "messages": [("user", "计算 (34 * 12) + 100 等于多少？")]
})
print("Agent finished.")
print("Final Answer:", response["messages"][-1].content)

# 打印工具调用过程以便观察
for msg in response["messages"]:
    if hasattr(msg, 'tool_calls') and msg.tool_calls:
        print(f"\nTool Call: {msg.tool_calls}")
    if hasattr(msg, 'name') and msg.name:
        print(f"\nTool Output ({msg.name}): {msg.content}")