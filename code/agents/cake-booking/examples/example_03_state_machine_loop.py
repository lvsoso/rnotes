from typing import Dict, List, Optional

from pydantic import BaseModel, Field


TASK_REQUIRED_SLOTS = {
    "book_order": ["cake_type", "size"],
}


class SimpleNLUResult(BaseModel):
    task: Optional[str] = None
    slots: Dict[str, str] = Field(default_factory=dict)


class SimpleState(BaseModel):
    active_task: Optional[str] = None
    confirmed_slots: Dict[str, str] = Field(default_factory=dict)
    missing_slots: List[str] = Field(default_factory=list)
    expected_slot: Optional[str] = None
    awaiting_confirmation: bool = False
    system_response: str = ""


def understand_turn(user_text: str) -> SimpleNLUResult:
    if "预定" in user_text or "订蛋糕" in user_text:
        return SimpleNLUResult(task="book_order")
    if user_text in {"巧克力", "草莓"}:
        return SimpleNLUResult(slots={"cake_type": user_text})
    if user_text in {"4寸", "6寸", "8寸", "10寸"}:
        return SimpleNLUResult(slots={"size": user_text})
    return SimpleNLUResult()


def calculate_missing_slots(task: Optional[str], confirmed_slots: Dict[str, str]) -> List[str]:
    if task is None:
        return []
    return [slot for slot in TASK_REQUIRED_SLOTS[task] if not confirmed_slots.get(slot)]


def update_state(state: SimpleState, nlu: SimpleNLUResult) -> SimpleState:
    next_state = state.model_copy(deep=True)
    if nlu.task and next_state.active_task is None:
        next_state.active_task = nlu.task
    next_state.confirmed_slots.update(nlu.slots)
    next_state.missing_slots = calculate_missing_slots(next_state.active_task, next_state.confirmed_slots)
    if next_state.expected_slot not in next_state.missing_slots:
        next_state.expected_slot = None
    return next_state


def decide_next_action(state: SimpleState, user_text: str) -> str:
    if state.active_task is None:
        return "clarify"
    if state.awaiting_confirmation:
        if user_text == "确认":
            return "execute"
        return "confirm"
    if state.missing_slots:
        return "ask_slot"
    return "confirm"


def apply_action(state: SimpleState, action: str) -> SimpleState:
    next_state = state.model_copy(deep=True)
    if action == "clarify":
        next_state.system_response = "请先说“我要预定蛋糕”。"
    elif action == "ask_slot":
        next_state.expected_slot = next_state.missing_slots[0]
        next_state.system_response = f"请补充 {next_state.expected_slot}。"
    elif action == "confirm":
        next_state.awaiting_confirmation = True
        next_state.system_response = (
            f"请确认下单：{next_state.confirmed_slots.get('cake_type')} "
            f"{next_state.confirmed_slots.get('size')}。回复“确认”继续。"
        )
    elif action == "execute":
        next_state.system_response = "订单创建成功。"
        next_state.active_task = None
        next_state.confirmed_slots = {}
        next_state.missing_slots = []
        next_state.expected_slot = None
        next_state.awaiting_confirmation = False
    return next_state


def process_user_turn(state: SimpleState, user_text: str) -> SimpleState:
    nlu = understand_turn(user_text)
    next_state = update_state(state, nlu)
    action = decide_next_action(next_state, user_text)
    return apply_action(next_state, action)


def demo() -> None:
    state = SimpleState()
    for user_text in ["你好", "我要预定蛋糕", "巧克力", "6寸", "确认"]:
        state = process_user_turn(state, user_text)
        print("用户：", user_text)
        print("系统：", state.system_response)
        print(
            "状态：",
            {
                "active_task": state.active_task,
                "confirmed_slots": state.confirmed_slots,
                "missing_slots": state.missing_slots,
                "expected_slot": state.expected_slot,
                "awaiting_confirmation": state.awaiting_confirmation,
            },
        )
        print("-" * 40)


if __name__ == "__main__":
    demo()
