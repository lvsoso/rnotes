import json
from collections.abc import AsyncIterator, Iterator
from dataclasses import dataclass
from typing import Any, TypeVar

from litellm import acompletion, completion
from pydantic import BaseModel

from config import (
    LLM_API_KEY,
    LLM_BASE_URL,
    LLM_MODEL,
    LLM_PROVIDER,
    LLM_TEMPERATURE,
    LLM_TIMEOUT,
)

SchemaT = TypeVar("SchemaT", bound=BaseModel)

# ANSI 颜色
C_YELLOW = "\033[33m"  # 请求信息
C_GREEN = "\033[32m"   # 响应文本
C_BLUE = "\033[34m"    # 工具调用
C_CYAN = "\033[36m"    # 其他信息
C_RESET = "\033[0m"


@dataclass(slots=True)
class LLMResult:
    text: str | None
    reasoning_text: str | None
    finish_reason: str | None
    stop_reason: str | None
    tool_calls: list[Any]
    raw: Any


@dataclass(slots=True)
class LLMStreamEvent:
    text_delta: str | None
    reasoning_delta: str | None
    tool_call_delta: list[Any]
    finish_reason: str | None
    stop_reason: str | None
    raw: Any


@dataclass(slots=True)
class LLMClient:
    model: str
    api_key: str | None
    base_url: str | None
    temperature: float
    timeout: float
    provider: str | None = None

    @classmethod
    def from_settings(cls) -> "LLMClient":
        return cls(
            model=LLM_MODEL,
            api_key=LLM_API_KEY,
            base_url=LLM_BASE_URL,
            provider=LLM_PROVIDER or ("openai" if LLM_BASE_URL else None),
            temperature=float(LLM_TEMPERATURE),
            timeout=float(LLM_TIMEOUT),
        )

    def complete(self, messages: list[dict[str, str]], **overrides: Any) -> Any:
        request_kwargs: dict[str, Any] = {
            "model": self.model,
            "api_key": self.api_key,
            "base_url": self.base_url,
            "temperature": self.temperature,
            "timeout": self.timeout,
            "messages": messages,
            **overrides,
        }
        if self.provider:
            request_kwargs["custom_llm_provider"] = self.provider

        # 调试输出：请求参数
        print(f"{C_YELLOW}[LLM Request]{C_RESET} model={self.model}, provider={self.provider}")
        if "tools" in request_kwargs:
            tools_names = [t.get("function", {}).get("name", t.get("name")) for t in request_kwargs["tools"]]
            print(f"{C_YELLOW}[LLM Request]{C_RESET} tools={tools_names}")
        print(f"{C_YELLOW}[LLM Request]{C_RESET} messages_count={len(messages)}")

        response = completion(**request_kwargs)

        # 调试输出：原始响应摘要
        choice = response["choices"][0]
        msg = choice["message"]
        finish = choice.get("finish_reason")
        tool_calls = msg.get("tool_calls", [])
        print(f"{C_CYAN}[LLM Response]{C_RESET} finish_reason={finish}, has_tool_calls={bool(tool_calls)}")

        return response

    @staticmethod
    def build_messages(prompt: str) -> list[dict[str, str]]:
        return [{"role": "user", "content": prompt}]

    @staticmethod
    def _extract_message_content(response: Any) -> str:
        message = response["choices"][0]["message"]
        return message["content"]

    @staticmethod
    def _extract_message_parsed(response: Any) -> Any | None:
        message = response["choices"][0]["message"]
        return message.get("parsed")

    @staticmethod
    def _extract_reasoning_content(payload: Any) -> str | None:
        if not isinstance(payload, dict):
            return None
        value = payload.get("reasoning_content") or payload.get("reason_content")
        return value if isinstance(value, str) else None

    @staticmethod
    def _extract_tool_calls(payload: Any) -> list[Any]:
        # 处理字典格式
        if isinstance(payload, dict):
            tool_calls = payload.get("tool_calls")
        # 处理对象格式（Message 对象）
        elif hasattr(payload, "tool_calls"):
            tool_calls = payload.tool_calls
        else:
            return []

        if not isinstance(tool_calls, list):
            return []

        # 转换对象为字典
        result = []
        for tc in tool_calls:
            if isinstance(tc, dict):
                result.append(tc)
            elif hasattr(tc, "model_dump"):
                result.append(tc.model_dump())
            elif hasattr(tc, "__dict__"):
                result.append(tc.__dict__)
        return result

    @classmethod
    def _build_result(cls, response: Any) -> LLMResult:
        choice = response["choices"][0]
        message = choice["message"]
        result = LLMResult(
            text=message.get("content"),
            reasoning_text=cls._extract_reasoning_content(message),
            finish_reason=choice.get("finish_reason"),
            stop_reason=message.get("stop_reason") or response.get("stop_reason"),
            tool_calls=cls._extract_tool_calls(message),
            raw=response,
        )
        # 调试输出：LLMResult 详情
        text_preview = (result.text[:80] + "...") if result.text and len(result.text) > 80 else result.text
        print(f"{C_GREEN}[LLMResult]{C_RESET} text={text_preview!r}")
        if result.tool_calls:
            tc_names = [tc.get("function", {}).get("name") for tc in result.tool_calls]
            print(f"{C_BLUE}[LLMResult]{C_RESET} tool_calls={tc_names}")
        print(f"{C_CYAN}[LLMResult]{C_RESET} finish_reason={result.finish_reason}, stop_reason={result.stop_reason}")
        return result

    @classmethod
    def _build_stream_event(cls, chunk: Any) -> LLMStreamEvent:
        choice = chunk["choices"][0]
        delta = choice.get("delta", {})
        return LLMStreamEvent(
            text_delta=delta.get("content"),
            reasoning_delta=cls._extract_reasoning_content(delta),
            tool_call_delta=cls._extract_tool_calls(delta),
            finish_reason=choice.get("finish_reason"),
            stop_reason=delta.get("stop_reason") or chunk.get("stop_reason"),
            raw=chunk,
        )

    @staticmethod
    def _json_fallback_messages(prompt: str, schema: type[BaseModel]) -> list[dict[str, str]]:
        schema_json = json.dumps(schema.model_json_schema(), ensure_ascii=False)
        return [
            {
                "role": "system",
                "content": (
                    f"你必须只返回合法 JSON，且输出必须满足这个 JSON Schema：{schema_json}"
                ),
            },
            {"role": "user", "content": prompt},
        ]

    def complete_text(self, messages: list[dict[str, str]], **overrides: Any) -> str:
        response = self.complete(messages, **overrides)
        return self._extract_message_content(response)

    def complete_result(self, messages: list[dict[str, str]], **overrides: Any) -> LLMResult:
        response = self.complete(messages, **overrides)
        return self._build_result(response)

    def ask(self, prompt: str, **overrides: Any) -> str:
        return self.complete_text(self.build_messages(prompt), **overrides)

    def ask_result(self, prompt: str, **overrides: Any) -> LLMResult:
        return self.complete_result(self.build_messages(prompt), **overrides)

    def ask_json(self, prompt: str, **overrides: Any) -> dict[str, Any]:
        return json.loads(self.ask(prompt, **overrides))

    def ask_structured(self, prompt: str, schema: type[SchemaT], **overrides: Any) -> SchemaT:
        try:
            response = self.complete(
                self.build_messages(prompt),
                response_format=schema,
                **overrides,
            )
            parsed = self._extract_message_parsed(response)
            if parsed is not None:
                return schema.model_validate(parsed)
            return schema.model_validate_json(self._extract_message_content(response))
        except Exception:
            fallback_payload = self.complete_text(
                self._json_fallback_messages(prompt, schema),
                **overrides,
            )
            return schema.model_validate_json(fallback_payload)

    async def acomplete(self, messages: list[dict[str, str]], **overrides: Any) -> Any:
        request_kwargs: dict[str, Any] = {
            "model": self.model,
            "api_key": self.api_key,
            "base_url": self.base_url,
            "temperature": self.temperature,
            "timeout": self.timeout,
            "messages": messages,
            **overrides,
        }
        if self.provider:
            request_kwargs["custom_llm_provider"] = self.provider
        return await acompletion(**request_kwargs)

    async def acomplete_text(self, messages: list[dict[str, str]], **overrides: Any) -> str:
        response = await self.acomplete(messages, **overrides)
        return self._extract_message_content(response)

    async def acomplete_result(self, messages: list[dict[str, str]], **overrides: Any) -> LLMResult:
        response = await self.acomplete(messages, **overrides)
        return self._build_result(response)

    async def aask(self, prompt: str, **overrides: Any) -> str:
        return await self.acomplete_text(self.build_messages(prompt), **overrides)

    async def aask_result(self, prompt: str, **overrides: Any) -> LLMResult:
        return await self.acomplete_result(self.build_messages(prompt), **overrides)

    async def aask_json(self, prompt: str, **overrides: Any) -> dict[str, Any]:
        return json.loads(await self.aask(prompt, **overrides))

    async def aask_structured(
        self, prompt: str, schema: type[SchemaT], **overrides: Any
    ) -> SchemaT:
        try:
            response = await self.acomplete(
                self.build_messages(prompt),
                response_format=schema,
                **overrides,
            )
            parsed = self._extract_message_parsed(response)
            if parsed is not None:
                return schema.model_validate(parsed)
            return schema.model_validate_json(self._extract_message_content(response))
        except Exception:
            fallback_payload = await self.acomplete_text(
                self._json_fallback_messages(prompt, schema),
                **overrides,
            )
            return schema.model_validate_json(fallback_payload)

    def stream(self, messages: list[dict[str, str]], **overrides: Any) -> Any:
        return self.complete(messages, stream=True, **overrides)

    def stream_text(self, messages: list[dict[str, str]], **overrides: Any) -> Iterator[str]:
        for chunk in self.stream(messages, **overrides):
            yield chunk["choices"][0]["delta"].get("content") or ""

    def ask_stream(self, prompt: str, **overrides: Any) -> Iterator[str]:
        return self.stream_text(self.build_messages(prompt), **overrides)

    def stream_events(
        self, messages: list[dict[str, str]], **overrides: Any
    ) -> Iterator[LLMStreamEvent]:
        for chunk in self.stream(messages, **overrides):
            yield self._build_stream_event(chunk)

    def stream_result(self, prompt: str, **overrides: Any) -> Iterator[LLMStreamEvent]:
        return self.stream_events(self.build_messages(prompt), **overrides)

    def collect_result(self, prompt: str, **overrides: Any) -> LLMResult:
        text_parts: list[str] = []
        reasoning_parts: list[str] = []
        tool_calls: list[Any] = []
        finish_reason: str | None = None
        stop_reason: str | None = None
        last_raw: Any = None

        for event in self.stream_result(prompt, **overrides):
            last_raw = event.raw
            if event.text_delta:
                text_parts.append(event.text_delta)
            if event.reasoning_delta:
                reasoning_parts.append(event.reasoning_delta)
            if event.tool_call_delta:
                tool_calls.extend(event.tool_call_delta)
            if event.finish_reason is not None:
                finish_reason = event.finish_reason
            if event.stop_reason is not None:
                stop_reason = event.stop_reason

        return LLMResult(
            text="".join(text_parts) or None,
            reasoning_text="".join(reasoning_parts) or None,
            finish_reason=finish_reason,
            stop_reason=stop_reason,
            tool_calls=tool_calls,
            raw=last_raw,
        )

    async def astream(self, messages: list[dict[str, str]], **overrides: Any) -> Any:
        return await self.acomplete(messages, stream=True, **overrides)

    async def astream_text(
        self, messages: list[dict[str, str]], **overrides: Any
    ) -> AsyncIterator[str]:
        stream = await self.astream(messages, **overrides)
        async for chunk in stream:
            yield chunk["choices"][0]["delta"].get("content") or ""

    async def aask_stream(self, prompt: str, **overrides: Any) -> AsyncIterator[str]:
        async for chunk in self.astream_text(self.build_messages(prompt), **overrides):
            yield chunk

    async def astream_events(
        self, messages: list[dict[str, str]], **overrides: Any
    ) -> AsyncIterator[LLMStreamEvent]:
        stream = await self.astream(messages, **overrides)
        async for chunk in stream:
            yield self._build_stream_event(chunk)

    async def astream_result(self, prompt: str, **overrides: Any) -> AsyncIterator[LLMStreamEvent]:
        async for event in self.astream_events(self.build_messages(prompt), **overrides):
            yield event

    async def acollect_result(self, prompt: str, **overrides: Any) -> LLMResult:
        text_parts: list[str] = []
        reasoning_parts: list[str] = []
        tool_calls: list[Any] = []
        finish_reason: str | None = None
        stop_reason: str | None = None
        last_raw: Any = None

        async for event in self.astream_result(prompt, **overrides):
            last_raw = event.raw
            if event.text_delta:
                text_parts.append(event.text_delta)
            if event.reasoning_delta:
                reasoning_parts.append(event.reasoning_delta)
            if event.tool_call_delta:
                tool_calls.extend(event.tool_call_delta)
            if event.finish_reason is not None:
                finish_reason = event.finish_reason
            if event.stop_reason is not None:
                stop_reason = event.stop_reason

        return LLMResult(
            text="".join(text_parts) or None,
            reasoning_text="".join(reasoning_parts) or None,
            finish_reason=finish_reason,
            stop_reason=stop_reason,
            tool_calls=tool_calls,
            raw=last_raw,
        )


llm_client = LLMClient.from_settings()
