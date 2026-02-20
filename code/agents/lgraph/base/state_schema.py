import random
from typing import Literal
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from utils import save_graph


class TypedDictState(TypedDict):
    name: str
    mood: Literal["happy", "sad"]

def node_1(state):
    print("---Node 1---")
    return {"name": state["name"] + " is ... "}

def node_2(state):
    print("---Node 2---")
    return {"mood": "happy"}

def node_3(state):
    print("---Node 3---")
    return {"mood": "sad"}

def decide_mood(state) -> Literal["node_2", "node_3"]:
    if random.random() < 0.5:
        return "node_2"
    else:
        return "node_3"


builder = StateGraph(TypedDictState)
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)

builder.add_edge(START, "node_1")
builder.add_conditional_edges("node_1", decide_mood)
builder.add_edge("node_2", END)
builder.add_edge("node_3", END)

graph = builder.compile()

save_graph(graph)

result = graph.invoke({"name": "Alice"})
print(result)