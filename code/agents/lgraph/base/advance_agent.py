import os
from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode
from langchain_core.prompts import FewShotChatMessagePromptTemplate
from langchain_community.callbacks import get_openai_callback


@tool
def calculate(expression: str) -> str:
    """计算表达式"""
    return str(eval(expression))

tools = [calculate]

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个智能助手，能够执行简单的数学计算。"),
    ("placeholder", "{messages}")
])


def agent(state: MessagesState):
    llm = ChatOpenAI(
        model_name=os.getenv("LLM_MODEL_ID"),
        api_key=os.getenv("LLM_API_KEY"),
        base_url=os.getenv("LLM_BASE_URL"),
    )
    # 强制要求模型调用 calculate 工具
    # 使用 tool_choice="calculate" 强制调用特定工具
    # 也可以使用 tool_choice="any" 强制调用任意工具（需模型支持）
    llm_with_tools = llm.bind_tools(tools, tool_choice="calculate")
    
    chain = prompt | llm_with_tools
    response = chain.invoke(state)
    return {"messages": [response]}

def should_continue(state: MessagesState) -> bool:
    """判断是否继续执行"""
    last_message = state["messages"][-1]
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "tools"
    return END


graph = StateGraph(MessagesState)
graph.add_node("agent", agent)
graph.add_node("tools", ToolNode(tools))
graph.add_edge(START, "agent")
# 显式声明条件边的目标节点，以便生成的图能正确显示连接
graph.add_conditional_edges("agent", should_continue, ["tools", END])
graph.add_edge("tools", "agent")

app = graph.compile()

# graph_png = app.get_graph().draw_mermaid_png()
# with open("graph.png", "wb") as f:
#     f.write(graph_png)
# print("已生成 graph.png，请查看本地文件")


with get_openai_callback() as cb:
    response = app.invoke({
        "messages": [("user", "计算 (25 + 75) * 2 / 10")]
    })
    
    print(f" 提示词 Tokens: {cb.prompt_tokens}")
    print(f" 回复 Tokens: {cb.completion_tokens}")
    print(f" 总计 Tokens: {cb.total_tokens}")
    print(f" 总计成本: ${cb.total_cost:.6f}")

print("Final Answer:", response["messages"][-1].content)

# 打印工具调用信息
for msg in response["messages"]:
    if hasattr(msg, 'tool_calls') and msg.tool_calls:
        print(f"\nTool Call: {msg.tool_calls}")
    if hasattr(msg, 'name') and msg.name:
        print(f"\nTool Output ({msg.name}): {msg.content}")