from typing import Dict, List, Literal, Optional, TypedDict

from langgraph.graph import END, START, StateGraph


class GraphState(TypedDict):
    user_text: str
    active_task: Optional[str]
    confirmed_slots: Dict[str, str]
    missing_slots: List[str]
    expected_slot: Optional[str]
    awaiting_confirmation: bool
    action: Optional[str]
    system_response: str


def understand_node(state: GraphState) -> GraphState:
    user_text = state["user_text"]
    active_task = state["active_task"]
    confirmed_slots = dict(state["confirmed_slots"])

    if ("预定" in user_text or "订蛋糕" in user_text) and active_task is None:
        active_task = "book_order"
    if user_text in {"巧克力", "草莓"}:
        confirmed_slots["cake_type"] = user_text
    if user_text in {"4寸", "6寸", "8寸", "10寸"}:
        confirmed_slots["size"] = user_text
    return {
        **state,
        "active_task": active_task,
        "confirmed_slots": confirmed_slots,
    }


def update_state_node(state: GraphState) -> GraphState:
    required = ["cake_type", "size"] if state["active_task"] == "book_order" else []
    missing_slots = [slot for slot in required if not state["confirmed_slots"].get(slot)]
    expected_slot = state["expected_slot"]
    if expected_slot not in missing_slots:
        expected_slot = None
    return {
        **state,
        "missing_slots": missing_slots,
        "expected_slot": expected_slot,
    }


def decide_node(state: GraphState) -> GraphState:
    action: Literal["clarify", "ask_slot", "confirm", "execute"]
    if state["active_task"] is None:
        action = "clarify"
    elif state["awaiting_confirmation"]:
        action = "execute" if state["user_text"] == "确认" else "confirm"
    elif state["missing_slots"]:
        action = "ask_slot"
    else:
        action = "confirm"
    return {**state, "action": action}


def apply_node(state: GraphState) -> GraphState:
    action = state["action"]
    next_state = dict(state)

    if action == "clarify":
        next_state["system_response"] = "请先说“我要预定蛋糕”。"
    elif action == "ask_slot":
        next_state["expected_slot"] = next_state["missing_slots"][0]
        next_state["awaiting_confirmation"] = False
        next_state["system_response"] = f"请补充 {next_state['expected_slot']}。"
    elif action == "confirm":
        next_state["awaiting_confirmation"] = True
        next_state["expected_slot"] = None
        next_state["system_response"] = (
            f"请确认下单：{next_state['confirmed_slots'].get('cake_type')} "
            f"{next_state['confirmed_slots'].get('size')}。回复“确认”继续。"
        )
    elif action == "execute":
        next_state["system_response"] = "订单创建成功。"
        next_state["active_task"] = None
        next_state["confirmed_slots"] = {}
        next_state["missing_slots"] = []
        next_state["expected_slot"] = None
        next_state["awaiting_confirmation"] = False
    return next_state


def build_graph():
    graph = StateGraph(GraphState)
    graph.add_node("understand", understand_node)
    graph.add_node("update_state", update_state_node)
    graph.add_node("decide", decide_node)
    graph.add_node("apply", apply_node)
    graph.add_edge(START, "understand")
    graph.add_edge("understand", "update_state")
    graph.add_edge("update_state", "decide")
    graph.add_edge("decide", "apply")
    graph.add_edge("apply", END)
    return graph.compile()


def demo() -> None:
    graph = build_graph()
    state: GraphState = {
        "user_text": "",
        "active_task": None,
        "confirmed_slots": {},
        "missing_slots": [],
        "expected_slot": None,
        "awaiting_confirmation": False,
        "action": None,
        "system_response": "",
    }

    for user_text in ["你好", "我要预定蛋糕", "巧克力", "6寸", "确认"]:
        state["user_text"] = user_text
        state = graph.invoke(state)
        print("用户：", user_text)
        print("动作：", state["action"])
        print("系统：", state["system_response"])
        print(
            "状态：",
            {
                "active_task": state["active_task"],
                "confirmed_slots": state["confirmed_slots"],
                "missing_slots": state["missing_slots"],
                "expected_slot": state["expected_slot"],
                "awaiting_confirmation": state["awaiting_confirmation"],
            },
        )
        print("-" * 40)


if __name__ == "__main__":
    demo()
