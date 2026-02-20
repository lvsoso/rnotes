from langgraph.graph import MessagesState, StateGraph, START, END
from langchain_core.messages import RemoveMessage, HumanMessage, AIMessage
from IPython.display import Image, display

class ConversationState(MessagesState):
    max_messages: int

def chat_node(state: ConversationState):
    """模拟 AI 响应"""
    print(f"  chat_node: 收到 {len(state['messages'])} 条消息")
    response = AIMessage(content="I understand your question.", name="Bot")
    return {"messages": [response]}

def cleanup_node(state: ConversationState):
    """清理旧消息，只保留最新的 max_messages 条"""
    messages = state["messages"]
    max_msgs = state.get("max_messages", 10)

    if len(messages) > max_msgs:
        num_to_delete = len(messages) - max_msgs
        # import pdb; pdb.set_trace()
        delete_messages = [RemoveMessage(id=m.id) for m in messages[:num_to_delete]]
        print(f"  cleanup_node: 删除 {num_to_delete} 条旧消息")
        return {"messages": delete_messages}

    print(f"  cleanup_node: 无需清理 ({len(messages)} <= {max_msgs})")
    return {}

builder = StateGraph(ConversationState)
builder.add_node("chat", chat_node)
builder.add_node("cleanup", cleanup_node)

builder.add_edge(START, "chat")
builder.add_edge("chat", "cleanup")
builder.add_edge("cleanup", END)

graph = builder.compile()

display(Image(graph.get_graph().draw_mermaid_png()))

initial_state = {
    "messages": [HumanMessage(content=f"Message {i}", id=str(i)) for i in range(12)],
    "max_messages": 10
}

print(f"初始消息数: {len(initial_state['messages'])}")
print(f"最大保留数: {initial_state['max_messages']}")
print("\n执行图:")

result = graph.invoke(initial_state)

print(f"\n最终消息数: {len(result['messages'])}")
print("保留的消息 ID:", [m.id for m in result['messages']])