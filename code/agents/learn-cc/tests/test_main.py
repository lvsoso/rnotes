import importlib
import io
import json
import sys
import types
import unittest
from contextlib import redirect_stdout
from unittest.mock import AsyncMock, Mock

from pydantic import BaseModel


class DemoAnswer(BaseModel):
    answer: str
    confidence: float


class TestMain(unittest.TestCase):
    def tearDown(self) -> None:
        sys.modules.pop("main", None)
        sys.modules.pop("llm_client", None)

    @staticmethod
    def _stub_llm_client(client: object) -> None:
        llm_client_module = types.ModuleType("llm_client")
        setattr(llm_client_module, "llm_client", client)
        sys.modules["llm_client"] = llm_client_module

    def test_run_complete_example_prints_model_response(self) -> None:
        client = Mock()
        client.ask.return_value = "你好，我是测试模型。"
        self._stub_llm_client(client)

        module = importlib.import_module("main")
        output = io.StringIO()

        with redirect_stdout(output):
            module.run_complete_example("你好")

        self.assertEqual(output.getvalue(), "你好，我是测试模型。\n")
        client.ask.assert_called_once_with("你好")

    def test_run_stream_example_prints_stream_chunks(self) -> None:
        client = Mock()
        client.ask_stream.return_value = iter(["你", "好", ""])
        self._stub_llm_client(client)

        module = importlib.import_module("main")
        output = io.StringIO()

        with redirect_stdout(output):
            module.run_stream_example("你好")

        self.assertEqual(output.getvalue(), "你好\n")
        client.ask_stream.assert_called_once_with("你好")

    def test_main_dispatches_stream_mode(self) -> None:
        client = Mock()
        client.ask_stream.return_value = iter(["ok"])
        self._stub_llm_client(client)

        module = importlib.import_module("main")
        output = io.StringIO()

        with redirect_stdout(output):
            module.main(["stream", "--prompt", "测试"])

        self.assertEqual(output.getvalue(), "ok\n")
        client.ask_stream.assert_called_once_with("测试")

    def test_run_json_example_prints_pretty_json(self) -> None:
        client = Mock()
        client.ask_json.return_value = {"answer": "你好", "confidence": 0.9}
        self._stub_llm_client(client)

        module = importlib.import_module("main")
        output = io.StringIO()

        with redirect_stdout(output):
            module.run_json_example("你好")

        self.assertEqual(
            output.getvalue(),
            json.dumps({"answer": "你好", "confidence": 0.9}, ensure_ascii=False, indent=2) + "\n",
        )
        client.ask_json.assert_called_once_with("你好")

    def test_main_dispatches_json_mode(self) -> None:
        client = Mock()
        client.ask_json.return_value = {"answer": "ok", "confidence": 1.0}
        self._stub_llm_client(client)

        module = importlib.import_module("main")
        output = io.StringIO()

        with redirect_stdout(output):
            module.main(["json", "--prompt", "测试"])

        self.assertIn('"answer": "ok"', output.getvalue())
        client.ask_json.assert_called_once_with("测试")

    def test_run_structured_example_prints_schema_json(self) -> None:
        client = Mock()
        client.ask_structured.return_value = DemoAnswer(answer="你好", confidence=0.8)
        self._stub_llm_client(client)

        module = importlib.import_module("main")
        output = io.StringIO()

        with redirect_stdout(output):
            module.run_structured_example("你好")

        self.assertEqual(
            output.getvalue(),
            DemoAnswer(answer="你好", confidence=0.8).model_dump_json(indent=2) + "\n",
        )
        client.ask_structured.assert_called_once_with("你好", module.DemoStructuredAnswer)

    def test_main_dispatches_structured_mode(self) -> None:
        client = Mock()
        client.ask_structured.return_value = DemoAnswer(answer="ok", confidence=1.0)
        self._stub_llm_client(client)

        module = importlib.import_module("main")
        output = io.StringIO()

        with redirect_stdout(output):
            module.main(["structured", "--prompt", "测试"])

        self.assertIn('"answer": "ok"', output.getvalue())
        client.ask_structured.assert_called_once_with("测试", module.DemoStructuredAnswer)


class TestAsyncMain(unittest.IsolatedAsyncioTestCase):
    def tearDown(self) -> None:
        sys.modules.pop("main", None)
        sys.modules.pop("llm_client", None)

    @staticmethod
    def _stub_llm_client(client: object) -> None:
        llm_client_module = types.ModuleType("llm_client")
        setattr(llm_client_module, "llm_client", client)
        sys.modules["llm_client"] = llm_client_module

    async def test_run_acomplete_example_prints_model_response(self) -> None:
        client = Mock()
        client.aask = AsyncMock(return_value="异步响应")
        self._stub_llm_client(client)

        module = importlib.import_module("main")
        output = io.StringIO()

        with redirect_stdout(output):
            await module.run_acomplete_example("你好")

        self.assertEqual(output.getvalue(), "异步响应\n")
        client.aask.assert_awaited_once_with("你好")

    async def test_run_astream_example_prints_stream_chunks(self) -> None:
        class FakeAsyncStream:
            def __init__(self, chunks: list[str]) -> None:
                self._chunks = chunks

            def __aiter__(self) -> "FakeAsyncStream":
                self._iterator = iter(self._chunks)
                return self

            async def __anext__(self) -> str:
                try:
                    return next(self._iterator)
                except StopIteration as exc:
                    raise StopAsyncIteration from exc

        client = Mock()
        client.aask_stream = Mock(return_value=FakeAsyncStream(["异", "步", ""]))
        self._stub_llm_client(client)

        module = importlib.import_module("main")
        output = io.StringIO()

        with redirect_stdout(output):
            await module.run_astream_example("你好")

        self.assertEqual(output.getvalue(), "异步\n")
        client.aask_stream.assert_called_once_with("你好")

    async def test_main_dispatches_astream_mode(self) -> None:
        class FakeAsyncStream:
            def __aiter__(self) -> "FakeAsyncStream":
                self._done = False
                return self

            async def __anext__(self) -> str:
                if self._done:
                    raise StopAsyncIteration
                self._done = True
                return "ok"

        client = Mock()
        client.aask_stream = Mock(return_value=FakeAsyncStream())
        self._stub_llm_client(client)

        module = importlib.import_module("main")
        output = io.StringIO()

        with redirect_stdout(output):
            await module.amain(["astream", "--prompt", "测试"])

        self.assertEqual(output.getvalue(), "ok\n")
        client.aask_stream.assert_called_once_with("测试")

    async def test_amain_dispatches_json_mode(self) -> None:
        client = Mock()
        client.ask_json.return_value = {"answer": "ok", "confidence": 1.0}
        self._stub_llm_client(client)

        module = importlib.import_module("main")
        output = io.StringIO()

        with redirect_stdout(output):
            await module.amain(["json", "--prompt", "测试"])

        self.assertIn('"answer": "ok"', output.getvalue())
        client.ask_json.assert_called_once_with("测试")

    async def test_amain_dispatches_structured_mode(self) -> None:
        client = Mock()
        client.ask_structured.return_value = DemoAnswer(answer="ok", confidence=1.0)
        self._stub_llm_client(client)

        module = importlib.import_module("main")
        output = io.StringIO()

        with redirect_stdout(output):
            await module.amain(["structured", "--prompt", "测试"])

        self.assertIn('"answer": "ok"', output.getvalue())
        client.ask_structured.assert_called_once_with("测试", module.DemoStructuredAnswer)


if __name__ == "__main__":
    unittest.main()
