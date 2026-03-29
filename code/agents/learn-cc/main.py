import argparse
import asyncio
import json
from collections.abc import Sequence
from typing import Any

from pydantic import BaseModel

from llm_client import llm_client

DEFAULT_PROMPT = "你好，请做一个简短的自我介绍。"


class DemoStructuredAnswer(BaseModel):
    answer: str
    confidence: float


def run_complete_example(prompt: str, client: Any = llm_client) -> None:
    print(client.ask(prompt))


def run_stream_example(prompt: str, client: Any = llm_client) -> None:
    for text in client.ask_stream(prompt):
        print(text, end="")
    print()


async def run_acomplete_example(prompt: str, client: Any = llm_client) -> None:
    print(await client.aask(prompt))


async def run_astream_example(prompt: str, client: Any = llm_client) -> None:
    async for text in client.aask_stream(prompt):
        print(text, end="")
    print()


def run_json_example(prompt: str, client: Any = llm_client) -> None:
    print(json.dumps(client.ask_json(prompt), ensure_ascii=False, indent=2))


def run_structured_example(prompt: str, client: Any = llm_client) -> None:
    result = client.ask_structured(prompt, DemoStructuredAnswer)
    print(result.model_dump_json(indent=2))


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="LiteLLM 客户端最小示例")
    parser.add_argument(
        "mode",
        choices=("complete", "stream", "acomplete", "astream", "json", "structured"),
        nargs="?",
        default="complete",
        help="选择同步或异步的完整响应、流式响应、JSON 或结构化输出示例",
    )
    parser.add_argument(
        "--prompt",
        default=DEFAULT_PROMPT,
        help="发送给模型的用户消息",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> None:
    args = parse_args(argv)
    if args.mode == "json":
        run_json_example(args.prompt)
        return
    if args.mode == "structured":
        run_structured_example(args.prompt)
        return
    if args.mode == "stream":
        run_stream_example(args.prompt)
        return
    if args.mode == "acomplete":
        asyncio.run(run_acomplete_example(args.prompt))
        return
    if args.mode == "astream":
        asyncio.run(run_astream_example(args.prompt))
        return
    run_complete_example(args.prompt)


async def amain(argv: Sequence[str] | None = None) -> None:
    args = parse_args(argv)
    if args.mode == "json":
        run_json_example(args.prompt)
        return
    if args.mode == "structured":
        run_structured_example(args.prompt)
        return
    if args.mode == "astream":
        await run_astream_example(args.prompt)
        return
    if args.mode == "acomplete":
        await run_acomplete_example(args.prompt)
        return
    if args.mode == "stream":
        run_stream_example(args.prompt)
        return
    run_complete_example(args.prompt)


if __name__ == "__main__":
    main()
