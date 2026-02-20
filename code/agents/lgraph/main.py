from typing import TypedDict
from langgraph.graph import StateGraph, START


# 定义状态
class State(TypedDict):
    graph_state: str

# 定义节点
def node_1(state):
    return {"graph_state": state['graph_state'] + " I am"}

# 构建图
graph = StateGraph(State)
graph.add_node("node_1", node_1)
graph.add_edge(START, "node_1")
