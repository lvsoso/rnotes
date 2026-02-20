import os
from dotenv import load_dotenv
from langgraph import graph
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.checkpoint.memory import MemorySaver

llm = ChatOpenAI(
    model_name=os.getenv("LLM_MODEL_ID"),
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL"),
)

def chatbot(state: MessagesState):
    return {'messages': [llm.invoke(state['messages'])]}


graph = StateGraph(MessagesState)
graph.add_node('chatbot', chatbot)
graph.add_edge(START, 'chatbot')
graph.add_edge('chatbot', END)

memory = MemorySaver()
app = graph.compile(checkpointer=memory)

config = {'configurable': {'thread_id': 'user_001'}}

response1 = app.invoke(
    {'messages': [HumanMessage(content="你好, 我叫小花")]},
    config=config
)
print("response1:", response1['messages'][-1].content)

response2 = app.invoke(
    {'messages': [HumanMessage(content="你好, 我想知道我叫什么")]},
    config=config
)
print("response2:", response2['messages'][-1].content)

graph_png = app.get_graph().draw_mermaid_png()
with open("graph.png", "wb") as f:
    f.write(graph_png)
print("已生成 graph.png，请查看本地文件")
