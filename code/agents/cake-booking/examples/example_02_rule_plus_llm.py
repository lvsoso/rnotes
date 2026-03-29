import os
import re
from typing import Dict, Optional

from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


load_dotenv()

SUPPORTED_CAKE_TYPES = ["巧克力", "草莓", "榴莲", "抹茶", "芒果"]


class SimpleExtraction(BaseModel):
    task: Optional[str] = None
    slots: Dict[str, str] = Field(default_factory=dict)
    confidence: float = 0.0


def normalize_cake_type(text: str) -> Optional[str]:
    for cake_type in SUPPORTED_CAKE_TYPES:
        if cake_type in text:
            return cake_type
    return None


def normalize_size(text: str) -> Optional[str]:
    match = re.search(r"(4|6|8|10)\s*寸", text)
    if not match:
        return None
    return f"{match.group(1)}寸"


def rule_understand_turn(user_text: str) -> SimpleExtraction:
    task = None
    if "修改" in user_text or "改" in user_text:
        task = "modify_order"
    elif "预定" in user_text or "预订" in user_text or "订蛋糕" in user_text:
        task = "book_order"

    slots: Dict[str, str] = {}
    cake_type = normalize_cake_type(user_text)
    size = normalize_size(user_text)
    if cake_type:
        slots["cake_type"] = cake_type
    if size:
        slots["size"] = size

    confidence = 0.2
    if task:
        confidence += 0.3
    if slots:
        confidence += 0.3
    return SimpleExtraction(task=task, slots=slots, confidence=confidence)


def build_llm() -> Optional[ChatOpenAI]:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None

    kwargs = {
        "model": os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        "temperature": float(os.getenv("OPENAI_TEMPERATURE", "0")),
        "timeout": int(os.getenv("OPENAI_TIMEOUT", "10")),
        "api_key": api_key,
    }
    base_url = os.getenv("OPENAI_BASE_URL")
    if base_url:
        kwargs["base_url"] = base_url
    return ChatOpenAI(**kwargs)


def llm_understand_turn(user_text: str) -> Optional[SimpleExtraction]:
    llm = build_llm()
    if llm is None:
        return None

    parser = PydanticOutputParser(pydantic_object=SimpleExtraction)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """你是蛋糕助手理解模块。只做结构化提取。
规则：
1. task 只允许 book_order 或 modify_order。
2. slots 只提取用户这句话里明确说出的字段。
3. cake_type 只允许：巧克力、草莓、榴莲、抹茶、芒果。
4. size 只允许：4寸、6寸、8寸、10寸。

{format_instructions}""",
            ),
            ("user", "{user_text}"),
        ]
    )
    chain = prompt | llm | parser
    return chain.invoke(
        {
            "format_instructions": parser.get_format_instructions(),
            "user_text": user_text,
        }
    )


def merge_results(rule_result: SimpleExtraction, llm_result: Optional[SimpleExtraction]) -> SimpleExtraction:
    if llm_result is None:
        return rule_result

    merged_slots = dict(llm_result.slots)
    merged_slots.update(rule_result.slots)
    return SimpleExtraction(
        task=rule_result.task or llm_result.task,
        slots=merged_slots,
        confidence=max(rule_result.confidence, llm_result.confidence),
    )


def run_example(user_text: str) -> None:
    rule_result = rule_understand_turn(user_text)
    llm_result = llm_understand_turn(user_text)
    merged = merge_results(rule_result, llm_result)

    print("输入：", user_text)
    print("规则结果：", rule_result.model_dump())
    print("LLM结果：", None if llm_result is None else llm_result.model_dump())
    print("合并结果：", merged.model_dump())
    print("说明：合并时用规则结果覆盖 LLM，是为了保证尺寸、口味等字段更稳定。")


if __name__ == "__main__":
    run_example("我想预定一个六寸巧克力蛋糕")
