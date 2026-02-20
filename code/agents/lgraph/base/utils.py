from langgraph.graph import StateGraph


def save_graph(app: StateGraph):
    graph_png = app.get_graph().draw_mermaid_png()
    with open("graph.png", "wb") as f:
        f.write(graph_png)
    print("已生成 graph.png，请查看本地文件")