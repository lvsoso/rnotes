import os
import re
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Literal

from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


load_dotenv()

TaskType = Literal["book_order", "modify_order"]
ActionType = Literal["ask_slot", "clarify", "confirm", "execute_tool", "respond_error"]

SUPPORTED_CAKE_TYPES = ["巧克力", "草莓", "榴莲", "抹茶", "芒果"]
SUPPORTED_SIZES = ["4寸", "6寸", "8寸", "10寸"]
TASK_REQUIRED_SLOTS: Dict[str, List[str]] = {
    "book_order": ["cake_type", "size", "pickup_time", "contact_name", "contact_phone"],
    "modify_order": ["order_id"],
}
TASK_MUTABLE_SLOTS = ["cake_type", "size", "pickup_time"]
SLOT_LABELS = {
    "cake_type": "蛋糕口味",
    "size": "蛋糕尺寸（例如：4寸）",
    "pickup_time": "取货时间（至少提前2小时）",
    "contact_name": "联系人姓名",
    "contact_phone": "联系人手机号",
    "order_id": "订单号",
    "modification_fields": "需要修改的内容（例如改成8寸，或改到明天下午三点）",
}
SUMMARY_LABELS = {
    "cake_type": "口味",
    "size": "尺寸",
    "pickup_time": "取货时间",
}


class ModelConfig(BaseModel):
    model: str = Field(default="gpt-4o-mini")
    temperature: float = Field(default=0.0)
    timeout: int = Field(default=10)
    api_key: Optional[str] = Field(default=None)
    base_url: Optional[str] = Field(default=None)

    @classmethod
    def from_env(cls) -> "ModelConfig":
        return cls(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            temperature=float(os.getenv("OPENAI_TEMPERATURE", "0")),
            timeout=int(os.getenv("OPENAI_TIMEOUT", "10")),
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_BASE_URL"),
        )


class NLUResult(BaseModel):
    task: Optional[TaskType] = None
    slots: Dict[str, Any] = Field(default_factory=dict)
    slot_patch: Dict[str, Any] = Field(default_factory=dict)
    user_goal_changed: bool = False
    confidence: float = 0.0
    uncertain_fields: List[str] = Field(default_factory=list)
    raw_reason: Optional[str] = None


class DialogueState(BaseModel):
    active_task: Optional[TaskType] = None
    confirmed_slots: Dict[str, Any] = Field(default_factory=dict)
    pending_slots: Dict[str, Any] = Field(default_factory=dict)
    missing_slots: List[str] = Field(default_factory=list)
    expected_slot: Optional[str] = None
    history: List[Dict[str, str]] = Field(default_factory=list)
    history_summary: str = ""
    last_user_message: str = ""
    system_response: str = ""
    last_system_action: Optional[str] = None
    awaiting_confirmation: bool = False
    turn_count: int = 0
    is_ended: bool = False
    business_error: Optional[str] = None
    invalid_slot_message: Optional[str] = None


class ActionDecision(BaseModel):
    action: ActionType
    message: str


class LLMExtraction(BaseModel):
    task: Optional[TaskType] = None
    slots: Dict[str, Optional[str]] = Field(default_factory=dict)
    slot_patch: Dict[str, Optional[str]] = Field(default_factory=dict)
    user_goal_changed: bool = False
    confidence: float = 0.0
    uncertain_fields: List[str] = Field(default_factory=list)
    raw_reason: Optional[str] = None


class CakeBookingTools:
    mock_order_db: Dict[str, Dict[str, Any]] = {}

    @classmethod
    def clear(cls) -> None:
        cls.mock_order_db = {}

    @classmethod
    def create_order(cls, params: Dict[str, Any]) -> Dict[str, Any]:
        required = TASK_REQUIRED_SLOTS["book_order"]
        for field in required:
            if not params.get(field):
                return {"success": False, "message": f"缺少必填参数：{field}"}

        order_id = f"CAKE{datetime.now().strftime('%Y%m%d%H%M%S')}"
        order = {
            "order_id": order_id,
            "cake_type": params["cake_type"],
            "size": params["size"],
            "pickup_time": params["pickup_time"],
            "contact_name": params["contact_name"],
            "contact_phone": params["contact_phone"],
            "status": "已预定",
        }
        cls.mock_order_db[order_id] = order
        return {"success": True, "message": "订单创建成功", "data": order}

    @classmethod
    def query_order(cls, order_id: str) -> Optional[Dict[str, Any]]:
        if not order_id:
            return None
        return cls.mock_order_db.get(order_id)

    @classmethod
    def modify_order(cls, params: Dict[str, Any]) -> Dict[str, Any]:
        order_id = params.get("order_id")
        if not order_id or order_id not in cls.mock_order_db:
            return {"success": False, "message": "订单不存在"}

        order = cls.mock_order_db[order_id]
        changed = False
        for field in TASK_MUTABLE_SLOTS:
            if params.get(field):
                order[field] = params[field]
                changed = True

        if not changed:
            return {"success": False, "message": "请提供至少一个需要修改的字段"}

        cls.mock_order_db[order_id] = order
        return {"success": True, "message": "订单修改成功", "data": order}


_LLM_CLIENT: Optional[ChatOpenAI] = None


def get_llm_client() -> Optional[ChatOpenAI]:
    global _LLM_CLIENT
    if _LLM_CLIENT is not None:
        return _LLM_CLIENT

    config = ModelConfig.from_env()
    if not config.api_key:
        return None

    kwargs: Dict[str, Any] = {
        "model": config.model,
        "temperature": config.temperature,
        "timeout": config.timeout,
        "api_key": config.api_key,
    }
    if config.base_url:
        kwargs["base_url"] = config.base_url

    _LLM_CLIENT = ChatOpenAI(**kwargs)
    return _LLM_CLIENT


def preprocess_user_input(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip())


def summarize_history(history: List[Dict[str, str]], max_turns: int = 8) -> str:
    recent = history[-max_turns:]
    return "\n".join(f"{item['role']}: {item['content']}" for item in recent)


def is_exit_text(text: str) -> bool:
    normalized = text.strip().lower()
    return normalized in {"退出", "结束", "bye", "quit", "exit"}


def is_greeting(text: str) -> bool:
    normalized = text.strip().lower()
    return normalized in {"你好", "您好", "hi", "hello", "在吗"}


def is_affirmative(text: str) -> bool:
    normalized = text.strip().lower()
    return normalized in {"是", "好的", "好", "确认", "没问题", "嗯", "yes", "y", "ok"}


def is_negative(text: str) -> bool:
    normalized = text.strip().lower()
    return normalized in {"不是", "不对", "取消", "先别", "no", "n"}


def normalize_cake_type(text: str) -> Optional[str]:
    if not text:
        return None
    for cake_type in SUPPORTED_CAKE_TYPES:
        if cake_type in text:
            return cake_type
    return None


def normalize_size(text: str) -> Optional[str]:
    match = re.search(r"(4|6|8|10)\s*寸", text)
    if not match:
        return None
    return f"{match.group(1)}寸"


def shift_size(current_size: Optional[str], direction: str) -> Optional[str]:
    if current_size not in SUPPORTED_SIZES:
        return None
    index = SUPPORTED_SIZES.index(current_size)
    if direction == "up" and index < len(SUPPORTED_SIZES) - 1:
        return SUPPORTED_SIZES[index + 1]
    if direction == "down" and index > 0:
        return SUPPORTED_SIZES[index - 1]
    return current_size


def normalize_phone(text: str) -> Optional[str]:
    match = re.search(r"1[3-9]\d{9}", text)
    return match.group(0) if match else None


def extract_order_id(text: str) -> Optional[str]:
    match = re.search(r"CAKE\d{14}", text)
    return match.group(0) if match else None


def extract_contact_name(text: str, expected_slot: Optional[str] = None) -> Optional[str]:
    explicit_patterns = [
        r"我叫([\u4e00-\u9fa5A-Za-z]{2,12})",
        r"姓名(?:是|叫)?([\u4e00-\u9fa5A-Za-z]{2,12})",
        r"联系人(?:是|叫)?([\u4e00-\u9fa5A-Za-z]{2,12})",
    ]
    for pattern in explicit_patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1)

    if expected_slot == "contact_name" and re.fullmatch(r"[\u4e00-\u9fa5A-Za-z]{2,12}", text):
        return text
    return None


def parse_pickup_time(text: str, now: Optional[datetime] = None) -> Optional[str]:
    now = now or datetime.now()

    absolute_match = re.search(r"(20\d{2}[-/]\d{1,2}[-/]\d{1,2})\s+(\d{1,2}:\d{2})", text)
    if absolute_match:
        date_part = absolute_match.group(1).replace("/", "-")
        pickup = datetime.strptime(f"{date_part} {absolute_match.group(2)}", "%Y-%m-%d %H:%M")
        return pickup.strftime("%Y-%m-%d %H:%M")

    relative_day = None
    if "明天" in text:
        relative_day = now + timedelta(days=1)
    elif "后天" in text:
        relative_day = now + timedelta(days=2)

    if relative_day is None:
        return None

    digitized_text = text
    chinese_hours = {
        "一": "1",
        "二": "2",
        "三": "3",
        "四": "4",
        "五": "5",
        "六": "6",
        "七": "7",
        "八": "8",
        "九": "9",
        "十": "10",
    }
    for chinese, arabic in chinese_hours.items():
        digitized_text = digitized_text.replace(f"{chinese}点", f"{arabic}点")

    hour_match = re.search(r"(\d{1,2})\s*点(半)?", digitized_text)
    if not hour_match:
        return None

    hour = int(hour_match.group(1))
    minute = 30 if hour_match.group(2) else 0
    if any(token in digitized_text for token in ["下午", "晚上"]) and hour < 12:
        hour += 12
    if "中午" in digitized_text and hour < 11:
        hour += 12

    pickup = relative_day.replace(hour=hour, minute=minute, second=0, microsecond=0)
    return pickup.strftime("%Y-%m-%d %H:%M")


def shift_pickup_time(current_value: Optional[str], hours: int = 0, days: int = 0) -> Optional[str]:
    if not current_value:
        return None
    try:
        current_dt = datetime.strptime(current_value, "%Y-%m-%d %H:%M")
    except ValueError:
        return None
    shifted = current_dt + timedelta(hours=hours, days=days)
    return shifted.strftime("%Y-%m-%d %H:%M")


def normalize_slot_value(slot_name: str, text: str) -> Optional[str]:
    if slot_name == "cake_type":
        return normalize_cake_type(text)
    if slot_name == "size":
        return normalize_size(text)
    if slot_name == "contact_phone":
        return normalize_phone(text)
    if slot_name == "order_id":
        return extract_order_id(text)
    if slot_name == "contact_name":
        return extract_contact_name(text, expected_slot="contact_name")
    if slot_name == "pickup_time":
        return parse_pickup_time(text)
    return None


def validate_slot(slot_name: str, value: str) -> Optional[str]:
    if slot_name == "cake_type":
        return value if value in SUPPORTED_CAKE_TYPES else None
    if slot_name == "size":
        return value if value in SUPPORTED_SIZES else None
    if slot_name == "contact_phone":
        return value if re.fullmatch(r"1[3-9]\d{9}", value) else None
    if slot_name == "contact_name":
        return value if re.fullmatch(r"[\u4e00-\u9fa5A-Za-z]{2,12}", value) else None
    if slot_name == "order_id":
        return value if re.fullmatch(r"CAKE\d{14}", value) else None
    if slot_name == "pickup_time":
        try:
            pickup_dt = datetime.strptime(value, "%Y-%m-%d %H:%M")
        except ValueError:
            return None
        if pickup_dt < datetime.now() + timedelta(hours=2):
            return None
        return value
    return value


def validate_slot_with_reason(slot_name: str, value: str) -> (Optional[str], Optional[str]):
    if slot_name == "pickup_time":
        try:
            pickup_dt = datetime.strptime(value, "%Y-%m-%d %H:%M")
        except ValueError:
            return None, "取货时间格式错误，请使用 YYYY-MM-DD HH:MM。"
        if pickup_dt < datetime.now() + timedelta(hours=2):
            return None, "取货时间需至少提前2小时，请重新提供时间。"
        return value, None

    validated = validate_slot(slot_name, value)
    if validated is not None:
        return validated, None
    if slot_name == "size":
        return None, "尺寸仅支持 4寸、6寸、8寸、10寸。"
    if slot_name == "cake_type":
        return None, f"口味仅支持：{'、'.join(SUPPORTED_CAKE_TYPES)}。"
    if slot_name == "order_id":
        return None, "订单号格式不正确。"
    if slot_name == "contact_phone":
        return None, "手机号格式不正确。"
    if slot_name == "contact_name":
        return None, "联系人姓名格式不正确。"
    return None, f"{SLOT_LABELS.get(slot_name, slot_name)}无效。"


def resolve_modify_patch(existing_order: Optional[Dict[str, Any]], user_text: str) -> Dict[str, Any]:
    patch: Dict[str, Any] = {}

    cake_type = normalize_cake_type(user_text)
    size = normalize_size(user_text)
    pickup_time = parse_pickup_time(user_text)
    if cake_type:
        patch["cake_type"] = cake_type
    if size:
        patch["size"] = size
    if pickup_time:
        patch["pickup_time"] = pickup_time

    if existing_order is None:
        return patch

    if "size" not in patch:
        current_size = existing_order.get("size")
        if any(token in user_text for token in ["大一点", "大一寸", "加大"]):
            shifted = shift_size(current_size, "up")
            if shifted:
                patch["size"] = shifted
        elif any(token in user_text for token in ["小一点", "小一寸", "缩小"]):
            shifted = shift_size(current_size, "down")
            if shifted:
                patch["size"] = shifted

    if "pickup_time" not in patch:
        current_pickup = existing_order.get("pickup_time")
        if any(token in user_text for token in ["早一点", "提前一点"]):
            shifted = shift_pickup_time(current_pickup, hours=-1)
            if shifted:
                patch["pickup_time"] = shifted
        elif any(token in user_text for token in ["晚一点", "延后一点", "推迟一点"]):
            shifted = shift_pickup_time(current_pickup, hours=1)
            if shifted:
                patch["pickup_time"] = shifted

        hour_delta_match = re.search(r"(提前|推迟|延后|往后)\s*([一二三四五六七八九十两\d]+)\s*小时", user_text)
        if hour_delta_match:
            raw_hours = hour_delta_match.group(2)
            hours = chinese_number_to_int(raw_hours)
            if hours is not None:
                direction = -hours if hour_delta_match.group(1) == "提前" else hours
                shifted = shift_pickup_time(current_pickup, hours=direction)
                if shifted:
                    patch["pickup_time"] = shifted

        day_delta_match = re.search(r"(提前|推迟|延后|往后)\s*([一二三四五六七八九十两\d]+)\s*天", user_text)
        if day_delta_match:
            raw_days = day_delta_match.group(2)
            days = chinese_number_to_int(raw_days)
            if days is not None:
                direction = -days if day_delta_match.group(1) == "提前" else days
                shifted = shift_pickup_time(current_pickup, days=direction)
                if shifted:
                    patch["pickup_time"] = shifted

    return patch


def chinese_number_to_int(raw: str) -> Optional[int]:
    if raw.isdigit():
        return int(raw)
    mapping = {
        "一": 1,
        "二": 2,
        "两": 2,
        "三": 3,
        "四": 4,
        "五": 5,
        "六": 6,
        "七": 7,
        "八": 8,
        "九": 9,
        "十": 10,
    }
    if raw in mapping:
        return mapping[raw]
    return None


def detect_task_by_rules(text: str, state: DialogueState) -> Optional[TaskType]:
    if any(keyword in text for keyword in ["修改", "改一下", "改成", "改到", "变更"]):
        return "modify_order"
    if any(keyword in text for keyword in ["预定", "预订", "订蛋糕", "订一个蛋糕", "买蛋糕"]):
        return "book_order"
    if state.active_task:
        return state.active_task
    return None


def rule_understand_turn(state: DialogueState, user_text: str) -> NLUResult:
    task = detect_task_by_rules(user_text, state)
    slots: Dict[str, Any] = {}
    slot_patch: Dict[str, Any] = {}
    existing_order = None
    if state.active_task == "modify_order" and state.confirmed_slots.get("order_id"):
        existing_order = CakeBookingTools.query_order(state.confirmed_slots["order_id"])

    cake_type = normalize_cake_type(user_text)
    size = normalize_size(user_text)
    pickup_time = parse_pickup_time(user_text)
    phone = normalize_phone(user_text)
    order_id = extract_order_id(user_text)
    contact_name = extract_contact_name(user_text, expected_slot=state.expected_slot)

    if cake_type:
        slots["cake_type"] = cake_type
    if size:
        slots["size"] = size
    if pickup_time:
        slots["pickup_time"] = pickup_time
    if phone:
        slots["contact_phone"] = phone
    if order_id:
        slots["order_id"] = order_id
    if contact_name:
        slots["contact_name"] = contact_name

    if task == "modify_order":
        slot_patch = resolve_modify_patch(existing_order, user_text)
        slots.update(slot_patch)

    reason = "greeting" if is_greeting(user_text) else None
    confidence = 0.15
    if task:
        confidence += 0.35
    if slots:
        confidence += 0.35

    if not task and state.active_task and slots:
        task = state.active_task

    return NLUResult(
        task=task,
        slots=slots,
        slot_patch=slot_patch,
        user_goal_changed=bool(task and state.active_task and task != state.active_task),
        confidence=min(confidence, 0.95),
        raw_reason=reason,
    )


def llm_understand_turn(state: DialogueState, user_text: str) -> Optional[NLUResult]:
    llm = get_llm_client()
    if llm is None:
        return None

    parser = PydanticOutputParser(pydantic_object=LLMExtraction)
    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """你是任务导向型蛋糕预定助手的理解模块。
只处理两个任务：
1. book_order：预定蛋糕
2. modify_order：修改已有订单

规则：
1. 只提取本轮用户新增或修正的信息，不要凭空补历史槽位。
2. 如果用户只回答一个值，要结合当前任务和 expected_slot 推断它对应的字段。
3. cake_type 只输出标准值：巧克力、草莓、榴莲、抹茶、芒果。
4. size 只输出标准值：4寸、6寸、8寸、10寸。
5. 修改订单时优先输出 slot_patch，表示这轮想改哪些字段，不要重述完整订单。
6. 如果只是寒暄，不要虚构任务和槽位。
7. 输出必须符合 JSON 格式。

{format_instructions}
active_task={active_task}
expected_slot={expected_slot}
confirmed_slots={confirmed_slots}
history_summary={history_summary}
rule_hint={rule_hint}""",
        ),
        ("user", "{user_text}"),
    ])

    chain = prompt | llm | parser
    try:
        result = chain.invoke({
            "format_instructions": parser.get_format_instructions(),
            "active_task": state.active_task,
            "expected_slot": state.expected_slot,
            "confirmed_slots": state.confirmed_slots,
            "history_summary": state.history_summary,
            "rule_hint": rule_understand_turn(state, user_text).model_dump(),
            "user_text": user_text,
        })
    except Exception:
        return None

    filtered_slots = {k: v for k, v in result.slots.items() if v}
    filtered_patch = {k: v for k, v in result.slot_patch.items() if v}
    return NLUResult(
        task=result.task,
        slots=filtered_slots,
        slot_patch=filtered_patch,
        user_goal_changed=result.user_goal_changed,
        confidence=result.confidence,
        uncertain_fields=result.uncertain_fields,
        raw_reason=result.raw_reason,
    )


def merge_nlu_results(rule_result: NLUResult, llm_result: Optional[NLUResult]) -> NLUResult:
    if llm_result is None:
        return rule_result

    merged_slots = dict(llm_result.slots)
    merged_slots.update(rule_result.slots)
    merged_patch = dict(llm_result.slot_patch)
    merged_patch.update(rule_result.slot_patch)
    task = rule_result.task or llm_result.task
    if task is None and llm_result.task:
        task = llm_result.task

    return NLUResult(
        task=task,
        slots=merged_slots,
        slot_patch=merged_patch,
        user_goal_changed=bool(rule_result.user_goal_changed or llm_result.user_goal_changed),
        confidence=max(rule_result.confidence, llm_result.confidence),
        uncertain_fields=list(dict.fromkeys(rule_result.uncertain_fields + llm_result.uncertain_fields)),
        raw_reason=rule_result.raw_reason or llm_result.raw_reason,
    )


def bind_expected_slot_if_needed(state: DialogueState, user_text: str, nlu: NLUResult) -> NLUResult:
    if nlu.slots or not state.expected_slot:
        return nlu

    value = normalize_slot_value(state.expected_slot, user_text)
    if value is None:
        return nlu

    candidate = validate_slot(state.expected_slot, value)
    if candidate is None:
        return nlu

    slots = dict(nlu.slots)
    slots[state.expected_slot] = candidate
    slot_patch = dict(nlu.slot_patch)
    if state.active_task == "modify_order":
        slot_patch[state.expected_slot] = candidate
    return nlu.model_copy(update={"slots": slots, "slot_patch": slot_patch, "task": nlu.task or state.active_task, "confidence": max(nlu.confidence, 0.6)})


def understand_turn(state: DialogueState, user_text: str, use_llm: bool = True) -> NLUResult:
    rule_result = rule_understand_turn(state, user_text)
    llm_result = llm_understand_turn(state, user_text) if use_llm else None
    merged = merge_nlu_results(rule_result, llm_result)
    return bind_expected_slot_if_needed(state, user_text, merged)


def calculate_missing_slots(task: Optional[TaskType], confirmed_slots: Dict[str, Any]) -> List[str]:
    if task is None:
        return []

    missing = [slot for slot in TASK_REQUIRED_SLOTS[task] if not confirmed_slots.get(slot)]
    if task == "modify_order" and confirmed_slots.get("order_id"):
        if not any(confirmed_slots.get(field) for field in TASK_MUTABLE_SLOTS):
            missing.append("modification_fields")
    return missing


def render_confirmation_message(state: DialogueState) -> str:
    if state.active_task == "book_order":
        return (
            "请确认是否创建订单："
            f"{state.confirmed_slots['cake_type']} {state.confirmed_slots['size']}，"
            f"取货时间 {state.confirmed_slots['pickup_time']}，"
            f"联系人 {state.confirmed_slots['contact_name']}（{state.confirmed_slots['contact_phone']}）。"
            "回复“确认”继续，回复“取消”放弃本次下单。"
        )
    existing_order = CakeBookingTools.query_order(state.confirmed_slots["order_id"])
    if existing_order is None:
        return (
            f"订单号 {state.confirmed_slots['order_id']} 不存在。"
            "请检查订单号，或回复“取消”放弃本次修改。"
        )

    changes = []
    for field in TASK_MUTABLE_SLOTS:
        new_value = state.confirmed_slots.get(field)
        if not new_value:
            continue
        old_value = existing_order.get(field)
        if old_value != new_value:
            changes.append(f"{SUMMARY_LABELS[field]}：{old_value} -> {new_value}")

    if not changes:
        return (
            f"订单号 {state.confirmed_slots['order_id']} 当前没有检测到实际变更。"
            "请继续说明修改内容，或回复“取消”放弃本次修改。"
        )

    return (
        "请确认是否修改订单："
        f"订单号 {state.confirmed_slots['order_id']}，"
        f"原订单 口味 {existing_order['cake_type']}，尺寸 {existing_order['size']}，取货时间 {existing_order['pickup_time']}；"
        f"修改内容 {'; '.join(changes)}。"
        "回复“确认”继续，回复“取消”放弃本次修改。"
    )


def reset_for_new_task(state: DialogueState, new_task: TaskType) -> DialogueState:
    preserved: Dict[str, Any] = {}
    if new_task == "book_order":
        for field in ["contact_name", "contact_phone"]:
            if state.confirmed_slots.get(field):
                preserved[field] = state.confirmed_slots[field]

    return state.model_copy(update={
        "active_task": new_task,
        "confirmed_slots": preserved,
        "pending_slots": {},
        "missing_slots": [],
        "expected_slot": None,
        "business_error": None,
    })


def update_dialogue_state(state: DialogueState, nlu: NLUResult) -> DialogueState:
    next_state = state.model_copy(deep=True)
    next_state.pending_slots = dict(nlu.slot_patch or nlu.slots)
    next_state.invalid_slot_message = None

    if nlu.task and (next_state.active_task is None or nlu.user_goal_changed):
        next_state = reset_for_new_task(next_state, nlu.task)
    elif nlu.task and next_state.active_task is None:
        next_state.active_task = nlu.task

    active_task = nlu.task or next_state.active_task
    next_state.active_task = active_task

    for slot_name, raw_value in nlu.slots.items():
        if slot_name not in SLOT_LABELS:
            continue
        validated, reason = validate_slot_with_reason(slot_name, str(raw_value))
        if validated is not None:
            next_state.confirmed_slots[slot_name] = validated
        elif reason:
            next_state.invalid_slot_message = reason

    for slot_name, raw_value in nlu.slot_patch.items():
        if slot_name not in SLOT_LABELS:
            continue
        validated, reason = validate_slot_with_reason(slot_name, str(raw_value))
        if validated is not None:
            next_state.confirmed_slots[slot_name] = validated
        elif reason:
            next_state.invalid_slot_message = reason

    next_state.missing_slots = calculate_missing_slots(next_state.active_task, next_state.confirmed_slots)
    if next_state.expected_slot not in next_state.missing_slots:
        next_state.expected_slot = None
    return next_state


def ask_for_slot_message(state: DialogueState, slot_name: str) -> str:
    if state.active_task == "modify_order" and slot_name == "modification_fields":
        return "请告诉我需要修改什么，例如“改成8寸”或“改到明天下午三点”。"
    if state.active_task == "book_order" and slot_name == "cake_type":
        return "请告诉我想订的蛋糕口味，例如巧克力、草莓、抹茶。"
    return f"请补充{SLOT_LABELS[slot_name]}。"


def decide_next_action(state: DialogueState, nlu: NLUResult) -> ActionDecision:
    if state.business_error:
        return ActionDecision(action="respond_error", message=state.business_error)

    if state.invalid_slot_message:
        return ActionDecision(action="respond_error", message=state.invalid_slot_message)

    if is_greeting(state.last_user_message) and state.active_task is None and not nlu.slots:
        return ActionDecision(
            action="clarify",
            message="我现在只处理两类业务：预定蛋糕、修改订单。你可以直接说“我要订一个巧克力蛋糕”或“我要修改订单”。",
        )

    if state.active_task is None:
        return ActionDecision(
            action="clarify",
            message="我现在只处理预定和修改订单。请直接说明你的需求，例如“我要预定蛋糕”或“我要修改订单”。",
        )

    if state.active_task == "modify_order":
        order_id = state.confirmed_slots.get("order_id")
        if order_id and CakeBookingTools.query_order(order_id) is None:
            return ActionDecision(action="respond_error", message="订单不存在，请检查订单号")

    if state.awaiting_confirmation:
        if is_affirmative(state.last_user_message):
            return ActionDecision(action="execute_tool", message="")
        if is_negative(state.last_user_message):
            return ActionDecision(action="clarify", message="已取消本次操作。你可以重新发起预定或修改订单。")
        return ActionDecision(action="confirm", message=render_confirmation_message(state))

    if state.missing_slots:
        next_slot = state.missing_slots[0]
        return ActionDecision(action="ask_slot", message=ask_for_slot_message(state, next_slot))

    return ActionDecision(action="confirm", message=render_confirmation_message(state))


def execute_business_action(state: DialogueState) -> Dict[str, Any]:
    if state.active_task == "book_order":
        return CakeBookingTools.create_order(state.confirmed_slots)
    if state.active_task == "modify_order":
        return CakeBookingTools.modify_order(state.confirmed_slots)
    return {"success": False, "message": "当前没有可执行的业务任务"}


def render_success_message(task: TaskType, result: Dict[str, Any]) -> str:
    data = result["data"]
    if task == "book_order":
        return (
            f"订单创建成功。\n"
            f"订单号：{data['order_id']}\n"
            f"蛋糕：{data['cake_type']} {data['size']}\n"
            f"取货时间：{data['pickup_time']}\n"
            f"联系人：{data['contact_name']}（{data['contact_phone']}）"
        )
    return (
        f"订单修改成功。\n"
        f"订单号：{data['order_id']}\n"
        f"当前蛋糕：{data['cake_type']} {data['size']}\n"
        f"取货时间：{data['pickup_time']}"
    )


def apply_action(state: DialogueState, decision: ActionDecision) -> DialogueState:
    next_state = state.model_copy(deep=True)
    next_state.last_system_action = decision.action

    if decision.action == "clarify":
        next_state.system_response = decision.message
        next_state.expected_slot = None
        if is_negative(next_state.last_user_message):
            next_state.active_task = None
            next_state.confirmed_slots = {}
            next_state.pending_slots = {}
            next_state.missing_slots = []
            next_state.awaiting_confirmation = False
    elif decision.action == "ask_slot":
        next_state.expected_slot = next_state.missing_slots[0]
        next_state.awaiting_confirmation = False
        next_state.system_response = decision.message
    elif decision.action == "confirm":
        next_state.awaiting_confirmation = True
        next_state.expected_slot = None
        next_state.system_response = decision.message
    elif decision.action == "respond_error":
        next_state.awaiting_confirmation = False
        next_state.system_response = f"抱歉，{decision.message}。"
    else:
        tool_result = execute_business_action(next_state)
        next_state.awaiting_confirmation = False
        if tool_result["success"]:
            next_state.system_response = render_success_message(next_state.active_task, tool_result)
            next_state.active_task = None
            next_state.confirmed_slots = {}
            next_state.pending_slots = {}
            next_state.missing_slots = []
            next_state.expected_slot = None
            next_state.business_error = None
        else:
            next_state.business_error = tool_result["message"]
            next_state.system_response = f"抱歉，{tool_result['message']}。"

    next_state.history.append({"role": "assistant", "content": next_state.system_response})
    next_state.history_summary = summarize_history(next_state.history)
    return next_state


def process_user_turn(state: DialogueState, user_text: str, use_llm: bool = True) -> DialogueState:
    cleaned = preprocess_user_input(user_text)
    if not cleaned:
        return state.model_copy(update={"system_response": "请输入有效内容。"})

    if is_exit_text(cleaned):
        next_state = state.model_copy(deep=True)
        next_state.system_response = "感谢使用蛋糕预定服务，再见！"
        next_state.is_ended = True
        next_state.history.append({"role": "user", "content": cleaned})
        next_state.history.append({"role": "assistant", "content": next_state.system_response})
        next_state.history_summary = summarize_history(next_state.history)
        return next_state

    next_state = state.model_copy(deep=True)
    next_state.turn_count += 1
    next_state.last_user_message = cleaned
    next_state.history.append({"role": "user", "content": cleaned})
    next_state.history_summary = summarize_history(next_state.history)

    nlu = understand_turn(next_state, cleaned, use_llm=use_llm)
    next_state = update_dialogue_state(next_state, nlu)
    decision = decide_next_action(next_state, nlu)
    next_state = apply_action(next_state, decision)
    return next_state


def run_cake_booking_agent() -> None:
    print("蛋糕预定助手（输入“退出”结束对话）")
    print("-" * 48)
    state = DialogueState()

    while True:
        user_text = input("\n你：")
        state = process_user_turn(state, user_text, use_llm=True)
        print(f"\n系统：{state.system_response}")
        if state.is_ended:
            break
