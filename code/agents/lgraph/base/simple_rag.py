from langgraph.graph import StateGraph, MessagesState
from langchain_community.vectorstores import FAISS

class RAGState(MessagesState):
    context: str

def retrieve_node(state: RAGState):
    """检索相关文档"""
    last_message = state["messages"][-1].content
    docs = retriever.invoke(last_message)
    context = "\n".join([doc.page_content for doc in docs])
    return {"context": context}

def generate_node(state: RAGState):
    """生成回答"""
    prompt = ChatPromptTemplate.from_messages([
        ("system", "请根据以下上下文回答\n{context}"),
        ("placeholder", "{messages}")
    ])

    llm = ChatOpenAI(model="gpt-5-nano")
    chain = prompt | llm

    response = chain.invoke({
        "context": state["context"],
        "messages": state["messages"]
    })

    return {"messages": [response]}

# 构建 RAG 图
graph = StateGraph(RAGState)
graph.add_node("retrieve", retrieve_node)
graph.add_node("generate", generate_node)
graph.add_edge("retrieve", "generate")