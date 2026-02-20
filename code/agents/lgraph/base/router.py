import os
from dotenv import load_dotenv

load_dotenv()
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition
from utils import save_graph


llm = ChatOpenAI(
    model_name=os.getenv("LLM_MODEL_ID"),
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL"),
)

def multiply(a: int, b: int) -> int:
    """计算两个整数的乘积
    Args:
        a (int): 第一个整数
        b (int): 第二个整数
    
    Returns:
        int: 两个整数的乘积
    """
    return a * b

llm_with_tools = llm.bind_tools([multiply])

def tool_calling_llm(state: MessagesState):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

def manual_tool_node(state: MessagesState):
    last_message = state["messages"][-1]
    tool_calls = last_message.tool_calls

    tool_messages = []
    for call in tool_calls:
        if call["name"] == "multiply":
            result = multiply(**call["args"])
            tool_messages.append(ToolMessage(
                content=str(result),
                tool_call_id=call["id"]
            ))

    return {"messages": tool_messages}


class SafeToolNode:
    def __init__(self, tools):
        self.tool_node = ToolNode(tools)

    def __call__(self, state: MessagesState):
        try:
            return self.tool_node(state)
        except Exception as e:
            # 返回错误消息
            return {"messages": [ToolMessage(
                content=f"Error executing tool: {str(e)}",
                tool_call_id=state["messages"][-1].tool_calls[0]["id"]
            )]}


builder = StateGraph(MessagesState)
builder.add_node("tool_calling_llm", tool_calling_llm)
builder.add_node("tools", SafeToolNode([multiply]))
builder.add_edge(START, "tool_calling_llm")
builder.add_conditional_edges("tool_calling_llm", tools_condition)
builder.add_edge("tools", END)
graph = builder.compile()

save_graph(graph)

print("=== 测试 1：工具调用 ===")
result = graph.invoke({"messages": [HumanMessage(content="What is 2 multiplied by 3?")]})
for m in result['messages']:
    m.pretty_print()

print("\n=== 测试 2：直接回答 ===")
result = graph.invoke({"messages": [HumanMessage(content="Hello world.")]})
for m in result['messages']:
    m.pretty_print()