import os
from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, MessagesState, START, END

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

app = graph.compile()
res = app.invoke({'messages': [HumanMessage(content="你好")]})
print(res['messages'][-1].content)

graph_png = app.get_graph().draw_mermaid_png()
with open("graph.png", "wb") as f:
    f.write(graph_png)
print("已生成 graph.png，请查看本地文件")
