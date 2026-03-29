import os
from typing import Dict, Optional

from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


load_dotenv()


class SimpleExtraction(BaseModel):
    task: Optional[str] = None
    slots: Dict[str, str] = Field(default_factory=dict)


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


def run_example(user_text: str) -> None:
    llm = build_llm()
    if llm is None:
        print("未检测到 OPENAI_API_KEY，跳过 LLM 调用。")
        print("这个示例主要对应项目里的 ChatPromptTemplate + PydanticOutputParser。")
        return

    parser = PydanticOutputParser(pydantic_object=SimpleExtraction)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """你是蛋糕助手的理解模块，只做结构化提取。
任务只允许：
1. book_order
2. modify_order

如果用户在下单，提取 task 和已出现的 slots。
如果没有明确任务，不要编造。

{format_instructions}""",
            ),
            ("user", "{user_text}"),
        ]
    )

    chain = prompt | llm | parser
    result = chain.invoke(
        {
            "format_instructions": parser.get_format_instructions(),
            "user_text": user_text,
        }
    )
    print("输入：", user_text)
    print("输出：", result.model_dump())


if __name__ == "__main__":
    run_example("我要预定一个6寸巧克力蛋糕")
