import importlib
import sys
import types
import unittest
from unittest.mock import AsyncMock, Mock

from pydantic import BaseModel


class Person(BaseModel):
    name: str
    age: int


class TestLLMClient(unittest.TestCase):
    @staticmethod
    def _stub_litellm(completion_mock: Mock, acompletion_mock: AsyncMock | None = None) -> None:
        litellm_module = types.ModuleType("litellm")
        setattr(litellm_module, "completion", completion_mock)
        setattr(litellm_module, "acompletion", acompletion_mock or AsyncMock())
        sys.modules["litellm"] = litellm_module

    def tearDown(self) -> None:
        sys.modules.pop("llm_client", None)
        sys.modules.pop("litellm", None)

    def test_import_module_does_not_send_request(self) -> None:
        completion_mock = Mock(return_value={"choices": []})
        self._stub_litellm(completion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")

        self.assertTrue(hasattr(module, "LLMClient"))
        completion_mock.assert_not_called()

    def test_complete_calls_litellm_completion_with_instance_config(self) -> None:
        completion_mock = Mock(return_value={"choices": [{"message": {"content": "ok"}}]})
        self._stub_litellm(completion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
        )

        result = client.complete([{"role": "user", "content": "hello"}])

        self.assertEqual(result, {"choices": [{"message": {"content": "ok"}}]})
        completion_mock.assert_called_once_with(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
            messages=[{"role": "user", "content": "hello"}],
        )

    def test_complete_passes_custom_provider_when_configured(self) -> None:
        completion_mock = Mock(return_value={"choices": [{"message": {"content": "ok"}}]})
        self._stub_litellm(completion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="Qwen/Qwen2.5-7B-Instruct",
            api_key="secret",
            base_url="https://api.siliconflow.cn/v1",
            temperature=0.2,
            timeout=30,
            provider="openai",
        )

        client.complete([{"role": "user", "content": "hello"}])

        completion_mock.assert_called_once_with(
            model="Qwen/Qwen2.5-7B-Instruct",
            api_key="secret",
            base_url="https://api.siliconflow.cn/v1",
            custom_llm_provider="openai",
            temperature=0.2,
            timeout=30,
            messages=[{"role": "user", "content": "hello"}],
        )

    def test_stream_calls_completion_with_stream_enabled(self) -> None:
        chunks = [
            {"choices": [{"delta": {"content": "he"}}]},
            {"choices": [{"delta": {"content": "llo"}}]},
        ]
        completion_mock = Mock(return_value=iter(chunks))
        self._stub_litellm(completion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
        )

        result = list(client.stream([{"role": "user", "content": "hello"}]))

        self.assertEqual(result, chunks)
        completion_mock.assert_called_once_with(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
            messages=[{"role": "user", "content": "hello"}],
            stream=True,
        )

    def test_complete_text_returns_message_content(self) -> None:
        completion_mock = Mock(
            return_value={"choices": [{"message": {"content": "纯文本结果"}}]}
        )
        self._stub_litellm(completion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
        )

        result = client.complete_text([{"role": "user", "content": "hello"}])

        self.assertEqual(result, "纯文本结果")

    def test_stream_text_yields_delta_content(self) -> None:
        chunks = [
            {"choices": [{"delta": {"content": "he"}}]},
            {"choices": [{"delta": {"content": None}}]},
            {"choices": [{"delta": {"content": "llo"}}]},
        ]
        completion_mock = Mock(return_value=iter(chunks))
        self._stub_litellm(completion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
        )

        result = list(client.stream_text([{"role": "user", "content": "hello"}]))

        self.assertEqual(result, ["he", "", "llo"])

    def test_ask_builds_single_user_message_for_complete_text(self) -> None:
        completion_mock = Mock(
            return_value={"choices": [{"message": {"content": "你好，世界"}}]}
        )
        self._stub_litellm(completion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
        )

        result = client.ask("hello")

        self.assertEqual(result, "你好，世界")
        completion_mock.assert_called_once_with(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
            messages=[{"role": "user", "content": "hello"}],
        )

    def test_ask_stream_builds_single_user_message_for_stream_text(self) -> None:
        completion_mock = Mock(
            return_value=iter(
                [
                    {"choices": [{"delta": {"content": "你"}}]},
                    {"choices": [{"delta": {"content": "好"}}]},
                ]
            )
        )
        self._stub_litellm(completion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
        )

        result = list(client.ask_stream("hello"))

        self.assertEqual(result, ["你", "好"])
        completion_mock.assert_called_once_with(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
            messages=[{"role": "user", "content": "hello"}],
            stream=True,
        )

    def test_ask_json_parses_json_text(self) -> None:
        completion_mock = Mock(
            return_value={"choices": [{"message": {"content": '{"name":"张三","age":18}'}}]}
        )
        self._stub_litellm(completion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
        )

        result = client.ask_json("hello")

        self.assertEqual(result, {"name": "张三", "age": 18})

    def test_ask_structured_uses_native_response_format_when_available(self) -> None:
        completion_mock = Mock(
            return_value={
                "choices": [{"message": {"parsed": {"name": "张三", "age": 18}}}]
            }
        )
        self._stub_litellm(completion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
        )

        result = client.ask_structured("hello", Person)

        self.assertEqual(result, Person(name="张三", age=18))
        completion_mock.assert_called_once_with(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
            messages=[{"role": "user", "content": "hello"}],
            response_format=Person,
        )

    def test_ask_structured_falls_back_to_json_prompt_and_validation(self) -> None:
        completion_mock = Mock(
            side_effect=[
                RuntimeError("native structured output not supported"),
                {"choices": [{"message": {"content": '{"name":"张三","age":18}'}}]},
            ]
        )
        self._stub_litellm(completion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
        )

        result = client.ask_structured("hello", Person)

        self.assertEqual(result, Person(name="张三", age=18))
        self.assertEqual(completion_mock.call_count, 2)
        fallback_messages = completion_mock.call_args_list[1].kwargs["messages"]
        self.assertEqual(fallback_messages[0]["role"], "system")
        self.assertIn("JSON", fallback_messages[0]["content"])
        self.assertEqual(fallback_messages[1], {"role": "user", "content": "hello"})

    def test_ask_result_returns_normalized_metadata(self) -> None:
        completion_mock = Mock(
            return_value={
                "id": "resp-1",
                "choices": [
                    {
                        "finish_reason": "tool_calls",
                        "message": {
                            "content": "final answer",
                            "reasoning_content": "thinking",
                            "tool_calls": [{"id": "call_1"}],
                        },
                    }
                ],
            }
        )
        self._stub_litellm(completion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
        )

        result = client.ask_result("hello")

        self.assertEqual(result.text, "final answer")
        self.assertEqual(result.reasoning_text, "thinking")
        self.assertEqual(result.finish_reason, "tool_calls")
        self.assertIsNone(result.stop_reason)
        self.assertEqual(result.tool_calls, [{"id": "call_1"}])
        self.assertEqual(result.raw["id"], "resp-1")

    def test_complete_result_supports_multi_turn_messages(self) -> None:
        completion_mock = Mock(
            return_value={
                "choices": [
                    {
                        "finish_reason": "stop",
                        "message": {"content": "final answer"},
                    }
                ]
            }
        )
        self._stub_litellm(completion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
        )

        messages = [
            {"role": "system", "content": "你是一个严谨助手"},
            {"role": "user", "content": "解释 TCP"},
            {"role": "assistant", "content": "TCP 是..."},
            {"role": "user", "content": "和 UDP 区别是什么"},
        ]
        result = client.complete_result(messages)

        self.assertEqual(result.text, "final answer")
        completion_mock.assert_called_once_with(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
            messages=messages,
        )

    def test_stream_result_returns_normalized_events(self) -> None:
        completion_mock = Mock(
            return_value=iter(
                [
                    {
                        "id": "chunk-1",
                        "choices": [
                            {
                                "delta": {
                                    "content": "Hel",
                                    "reason_content": "plan",
                                },
                                "finish_reason": None,
                            }
                        ],
                    },
                    {
                        "id": "chunk-2",
                        "choices": [
                            {
                                "delta": {
                                    "content": "lo",
                                    "tool_calls": [{"id": "call_1"}],
                                },
                                "finish_reason": "stop",
                            }
                        ],
                    },
                ]
            )
        )
        self._stub_litellm(completion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
        )

        events = list(client.stream_result("hello"))

        self.assertEqual(len(events), 2)
        self.assertEqual(events[0].text_delta, "Hel")
        self.assertEqual(events[0].reasoning_delta, "plan")
        self.assertEqual(events[0].tool_call_delta, [])
        self.assertIsNone(events[0].finish_reason)
        self.assertEqual(events[1].text_delta, "lo")
        self.assertEqual(events[1].tool_call_delta, [{"id": "call_1"}])
        self.assertEqual(events[1].finish_reason, "stop")

    def test_stream_events_supports_multi_turn_messages(self) -> None:
        completion_mock = Mock(
            return_value=iter(
                [
                    {
                        "choices": [
                            {
                                "delta": {"content": "A"},
                                "finish_reason": None,
                            }
                        ]
                    },
                    {
                        "choices": [
                            {
                                "delta": {"content": "B"},
                                "finish_reason": "stop",
                            }
                        ]
                    },
                ]
            )
        )
        self._stub_litellm(completion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
        )

        messages = [
            {"role": "user", "content": "第一问"},
            {"role": "assistant", "content": "第一答"},
            {"role": "user", "content": "第二问"},
        ]
        events = list(client.stream_events(messages))

        self.assertEqual([event.text_delta for event in events], ["A", "B"])
        completion_mock.assert_called_once_with(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
            messages=messages,
            stream=True,
        )

    def test_collect_result_aggregates_stream_events(self) -> None:
        completion_mock = Mock(
            return_value=iter(
                [
                    {
                        "choices": [
                            {
                                "delta": {"content": "Hel", "reasoning_content": "pla"},
                                "finish_reason": None,
                            }
                        ]
                    },
                    {
                        "choices": [
                            {
                                "delta": {
                                    "content": "lo",
                                    "reasoning_content": "n",
                                    "tool_calls": [{"id": "call_1"}],
                                },
                                "finish_reason": "stop",
                            }
                        ],
                        "stop_reason": "end_turn",
                    },
                ]
            )
        )
        self._stub_litellm(completion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
        )

        result = client.collect_result("hello")

        self.assertEqual(result.text, "Hello")
        self.assertEqual(result.reasoning_text, "plan")
        self.assertEqual(result.finish_reason, "stop")
        self.assertEqual(result.stop_reason, "end_turn")
        self.assertEqual(result.tool_calls, [{"id": "call_1"}])


class TestAsyncLLMClient(unittest.IsolatedAsyncioTestCase):
    @staticmethod
    def _stub_litellm(
        completion_mock: Mock | None = None,
        acompletion_mock: AsyncMock | None = None,
    ) -> None:
        litellm_module = types.ModuleType("litellm")
        setattr(litellm_module, "completion", completion_mock or Mock())
        setattr(litellm_module, "acompletion", acompletion_mock or AsyncMock())
        sys.modules["litellm"] = litellm_module

    def tearDown(self) -> None:
        sys.modules.pop("llm_client", None)
        sys.modules.pop("litellm", None)

    async def test_acomplete_calls_litellm_acompletion(self) -> None:
        acompletion_mock = AsyncMock(return_value={"choices": [{"message": {"content": "ok"}}]})
        self._stub_litellm(acompletion_mock=acompletion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
        )

        result = await client.acomplete([{"role": "user", "content": "hello"}])

        self.assertEqual(result, {"choices": [{"message": {"content": "ok"}}]})
        acompletion_mock.assert_awaited_once_with(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
            messages=[{"role": "user", "content": "hello"}],
        )

    async def test_astream_calls_litellm_acompletion_with_stream_enabled(self) -> None:
        stream_response = object()
        acompletion_mock = AsyncMock(return_value=stream_response)
        self._stub_litellm(acompletion_mock=acompletion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
        )

        result = await client.astream([{"role": "user", "content": "hello"}])

        self.assertIs(result, stream_response)
        acompletion_mock.assert_awaited_once_with(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
            messages=[{"role": "user", "content": "hello"}],
            stream=True,
        )

    async def test_acomplete_text_returns_message_content(self) -> None:
        acompletion_mock = AsyncMock(
            return_value={"choices": [{"message": {"content": "异步纯文本"}}]}
        )
        self._stub_litellm(acompletion_mock=acompletion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
        )

        result = await client.acomplete_text([{"role": "user", "content": "hello"}])

        self.assertEqual(result, "异步纯文本")

    async def test_astream_text_yields_delta_content(self) -> None:
        class FakeAsyncStream:
            def __init__(self, chunks: list[dict[str, object]]) -> None:
                self._chunks = chunks

            def __aiter__(self) -> "FakeAsyncStream":
                self._iterator = iter(self._chunks)
                return self

            async def __anext__(self) -> dict[str, object]:
                try:
                    return next(self._iterator)
                except StopIteration as exc:
                    raise StopAsyncIteration from exc

        acompletion_mock = AsyncMock(
            return_value=FakeAsyncStream(
                [
                    {"choices": [{"delta": {"content": "异"}}]},
                    {"choices": [{"delta": {"content": None}}]},
                    {"choices": [{"delta": {"content": "步"}}]},
                ]
            )
        )
        self._stub_litellm(acompletion_mock=acompletion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
        )

        result: list[str] = []
        async for chunk in client.astream_text([{"role": "user", "content": "hello"}]):
            result.append(chunk)

        self.assertEqual(result, ["异", "", "步"])

    async def test_aask_builds_single_user_message_for_acomplete_text(self) -> None:
        acompletion_mock = AsyncMock(
            return_value={"choices": [{"message": {"content": "异步你好"}}]}
        )
        self._stub_litellm(acompletion_mock=acompletion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
        )

        result = await client.aask("hello")

        self.assertEqual(result, "异步你好")
        acompletion_mock.assert_awaited_once_with(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
            messages=[{"role": "user", "content": "hello"}],
        )

    async def test_aask_stream_builds_single_user_message_for_astream_text(self) -> None:
        class FakeAsyncStream:
            def __init__(self, chunks: list[dict[str, object]]) -> None:
                self._chunks = chunks

            def __aiter__(self) -> "FakeAsyncStream":
                self._iterator = iter(self._chunks)
                return self

            async def __anext__(self) -> dict[str, object]:
                try:
                    return next(self._iterator)
                except StopIteration as exc:
                    raise StopAsyncIteration from exc

        acompletion_mock = AsyncMock(
            return_value=FakeAsyncStream(
                [
                    {"choices": [{"delta": {"content": "异"}}]},
                    {"choices": [{"delta": {"content": "步"}}]},
                ]
            )
        )
        self._stub_litellm(acompletion_mock=acompletion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
        )

        result: list[str] = []
        async for chunk in client.aask_stream("hello"):
            result.append(chunk)

        self.assertEqual(result, ["异", "步"])
        acompletion_mock.assert_awaited_once_with(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
            messages=[{"role": "user", "content": "hello"}],
            stream=True,
        )

    async def test_aask_json_parses_json_text(self) -> None:
        acompletion_mock = AsyncMock(
            return_value={"choices": [{"message": {"content": '{"name":"张三","age":18}'}}]}
        )
        self._stub_litellm(acompletion_mock=acompletion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
        )

        result = await client.aask_json("hello")

        self.assertEqual(result, {"name": "张三", "age": 18})

    async def test_aask_structured_uses_native_response_format_when_available(self) -> None:
        acompletion_mock = AsyncMock(
            return_value={
                "choices": [{"message": {"parsed": {"name": "张三", "age": 18}}}]
            }
        )
        self._stub_litellm(acompletion_mock=acompletion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
        )

        result = await client.aask_structured("hello", Person)

        self.assertEqual(result, Person(name="张三", age=18))
        acompletion_mock.assert_awaited_once_with(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
            messages=[{"role": "user", "content": "hello"}],
            response_format=Person,
        )

    async def test_aask_structured_falls_back_to_json_prompt_and_validation(self) -> None:
        acompletion_mock = AsyncMock(
            side_effect=[
                RuntimeError("native structured output not supported"),
                {"choices": [{"message": {"content": '{"name":"张三","age":18}'}}]},
            ]
        )
        self._stub_litellm(acompletion_mock=acompletion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
        )

        result = await client.aask_structured("hello", Person)

        self.assertEqual(result, Person(name="张三", age=18))
        self.assertEqual(acompletion_mock.await_count, 2)
        fallback_messages = acompletion_mock.await_args_list[1].kwargs["messages"]
        self.assertEqual(fallback_messages[0]["role"], "system")
        self.assertIn("JSON", fallback_messages[0]["content"])
        self.assertEqual(fallback_messages[1], {"role": "user", "content": "hello"})

    async def test_aask_result_returns_normalized_metadata(self) -> None:
        acompletion_mock = AsyncMock(
            return_value={
                "id": "resp-1",
                "choices": [
                    {
                        "finish_reason": "stop",
                        "message": {
                            "content": "async answer",
                            "reason_content": "async thinking",
                            "tool_calls": [{"id": "call_1"}],
                            "stop_reason": "end_turn",
                        },
                    }
                ],
            }
        )
        self._stub_litellm(acompletion_mock=acompletion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
        )

        result = await client.aask_result("hello")

        self.assertEqual(result.text, "async answer")
        self.assertEqual(result.reasoning_text, "async thinking")
        self.assertEqual(result.finish_reason, "stop")
        self.assertEqual(result.stop_reason, "end_turn")
        self.assertEqual(result.tool_calls, [{"id": "call_1"}])

    async def test_acomplete_result_supports_multi_turn_messages(self) -> None:
        acompletion_mock = AsyncMock(
            return_value={
                "choices": [
                    {
                        "finish_reason": "stop",
                        "message": {"content": "async final answer"},
                    }
                ]
            }
        )
        self._stub_litellm(acompletion_mock=acompletion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
        )

        messages = [
            {"role": "system", "content": "你是一个严谨助手"},
            {"role": "user", "content": "解释 TCP"},
            {"role": "assistant", "content": "TCP 是..."},
            {"role": "user", "content": "和 UDP 区别是什么"},
        ]
        result = await client.acomplete_result(messages)

        self.assertEqual(result.text, "async final answer")
        acompletion_mock.assert_awaited_once_with(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
            messages=messages,
        )

    async def test_astream_result_returns_normalized_events(self) -> None:
        class FakeAsyncStream:
            def __init__(self, chunks: list[dict[str, object]]) -> None:
                self._chunks = chunks

            def __aiter__(self) -> "FakeAsyncStream":
                self._iterator = iter(self._chunks)
                return self

            async def __anext__(self) -> dict[str, object]:
                try:
                    return next(self._iterator)
                except StopIteration as exc:
                    raise StopAsyncIteration from exc

        acompletion_mock = AsyncMock(
            return_value=FakeAsyncStream(
                [
                    {
                        "choices": [
                            {
                                "delta": {"content": "A", "reasoning_content": "r"},
                                "finish_reason": None,
                            }
                        ]
                    },
                    {
                        "choices": [
                            {
                                "delta": {"content": "B", "tool_calls": [{"id": "call_2"}]},
                                "finish_reason": "stop",
                            }
                        ],
                        "stop_reason": "end_turn",
                    },
                ]
            )
        )
        self._stub_litellm(acompletion_mock=acompletion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
        )

        events = []
        async for event in client.astream_result("hello"):
            events.append(event)

        self.assertEqual(len(events), 2)
        self.assertEqual(events[0].text_delta, "A")
        self.assertEqual(events[0].reasoning_delta, "r")
        self.assertEqual(events[1].tool_call_delta, [{"id": "call_2"}])
        self.assertEqual(events[1].finish_reason, "stop")
        self.assertEqual(events[1].stop_reason, "end_turn")

    async def test_astream_events_supports_multi_turn_messages(self) -> None:
        class FakeAsyncStream:
            def __init__(self, chunks: list[dict[str, object]]) -> None:
                self._chunks = chunks

            def __aiter__(self) -> "FakeAsyncStream":
                self._iterator = iter(self._chunks)
                return self

            async def __anext__(self) -> dict[str, object]:
                try:
                    return next(self._iterator)
                except StopIteration as exc:
                    raise StopAsyncIteration from exc

        acompletion_mock = AsyncMock(
            return_value=FakeAsyncStream(
                [
                    {
                        "choices": [
                            {
                                "delta": {"content": "A"},
                                "finish_reason": None,
                            }
                        ]
                    },
                    {
                        "choices": [
                            {
                                "delta": {"content": "B"},
                                "finish_reason": "stop",
                            }
                        ]
                    },
                ]
            )
        )
        self._stub_litellm(acompletion_mock=acompletion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
        )

        messages = [
            {"role": "user", "content": "第一问"},
            {"role": "assistant", "content": "第一答"},
            {"role": "user", "content": "第二问"},
        ]
        events = []
        async for event in client.astream_events(messages):
            events.append(event)

        self.assertEqual([event.text_delta for event in events], ["A", "B"])
        acompletion_mock.assert_awaited_once_with(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
            messages=messages,
            stream=True,
        )

    async def test_acollect_result_aggregates_stream_events(self) -> None:
        class FakeAsyncStream:
            def __init__(self, chunks: list[dict[str, object]]) -> None:
                self._chunks = chunks

            def __aiter__(self) -> "FakeAsyncStream":
                self._iterator = iter(self._chunks)
                return self

            async def __anext__(self) -> dict[str, object]:
                try:
                    return next(self._iterator)
                except StopIteration as exc:
                    raise StopAsyncIteration from exc

        acompletion_mock = AsyncMock(
            return_value=FakeAsyncStream(
                [
                    {
                        "choices": [
                            {
                                "delta": {"content": "Hi", "reason_content": "th"},
                                "finish_reason": None,
                            }
                        ]
                    },
                    {
                        "choices": [
                            {
                                "delta": {"content": "!", "reason_content": "ink"},
                                "finish_reason": "stop",
                            }
                        ],
                        "stop_reason": "end_turn",
                    },
                ]
            )
        )
        self._stub_litellm(acompletion_mock=acompletion_mock)
        sys.modules.pop("llm_client", None)

        module = importlib.import_module("llm_client")
        client = module.LLMClient(
            model="test-model",
            api_key="secret",
            base_url="https://example.com",
            temperature=0.2,
            timeout=30,
        )

        result = await client.acollect_result("hello")

        self.assertEqual(result.text, "Hi!")
        self.assertEqual(result.reasoning_text, "think")
        self.assertEqual(result.finish_reason, "stop")
        self.assertEqual(result.stop_reason, "end_turn")


if __name__ == "__main__":
    unittest.main()
