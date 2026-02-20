import os
from dotenv import load_dotenv
load_dotenv()

from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode


llm = ChatOpenAI(
    model_name=os.getenv("LLM_MODEL_ID"),
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL"),
)


@tool
def calculator(expression: str) -> str:
    """执行数学计算。输入格式：'数字1 运算符 数字2'（如 '25 * 4'）"""
    try:
        parts = expression.strip().split()
        if len(parts) != 3:
            return "格式错误，请使用: 数字1 运算符 数字2"
        num1, op, num2 = parts
        num1, num2 = float(num1), float(num2)
        if op == '+': return str(num1 + num2)
        elif op == '-': return str(num1 - num2)
        elif op == '*': return str(num1 * num2)
        elif op == '/': return str(num1 / num2) if num2 != 0 else "除数不能为零"
        else: return f"不支持的运算符: {op}"
    except:
        return "计算错误"

@tool
def get_weather(city: str) -> str:
    """查询城市天气。输入：城市名称"""
    # 模拟天气查询
    weather_db = {
        "北京": "晴天，15°C",
        "上海": "多云，18°C",
        "深圳": "阴天，22°C"
    }
    return weather_db.get(city, "未知城市")

tools = [calculator, get_weather]

llm_with_tools = llm.bind_tools(tools)

def chatbot(state: MessagesState):
    return {'messages': [llm_with_tools.invoke(state['messages'])]}

def should_continue(state: MessagesState):
    last_message = state['messages'][-1]
    if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
        return 'tools'
    return 'end'

graph = StateGraph(MessagesState)
graph.add_node('chatbot', chatbot)
graph.add_node('tools', ToolNode(tools))

graph.add_edge(START, 'chatbot')
graph.add_conditional_edges('chatbot', should_continue, 
    {'tools': 'tools', 'end': END})
graph.add_edge('tools', END)

app = graph.compile()

response = app.invoke({'messages': [HumanMessage(content="北京今天天气怎么样？")]})
print(response['messages'][-1].content)

graph_png = app.get_graph().draw_mermaid_png()
with open("graph.png", "wb") as f:
    f.write(graph_png)
print("已生成 graph.png，请查看本地文件")
