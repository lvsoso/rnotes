# Repository Guidelines

## Project Structure & Module Organization
This repository is a minimal Python agent demo for cake booking. [`main.py`](/Users/Zhuanz/lvsoso/rnotes/code/agents/cake-booking/main.py) contains the full workflow: Pydantic models, mock booking tools, LangGraph nodes, graph assembly, and the CLI loop. [`requirements.txt`](/Users/Zhuanz/lvsoso/rnotes/code/agents/cake-booking/requirements.txt) defines runtime dependencies. Use [`.env.example`](/Users/Zhuanz/lvsoso/rnotes/code/agents/cake-booking/.env.example) as the template for local configuration and keep secrets only in `.env`.

## Build, Test, and Development Commands
Create an isolated environment before installing packages:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run the CLI agent locally with `python main.py`. Do a quick syntax check with `python -m py_compile main.py`. If you add tests, prefer `pytest` and run them with `pytest -q`.

## Coding Style & Naming Conventions
Follow PEP 8 with 4-space indentation and keep imports grouped by standard library, third-party, then local code. Use `snake_case` for functions and variables, `PascalCase` for classes such as `SlotInfo`, and concise verb-based names for node functions like `tool_call_node`. Keep validation rules explicit and close to the schema they protect. When extending the workflow, add new business logic as focused functions instead of enlarging the CLI loop.

## Testing Guidelines
There is no committed test suite yet, so new features should add targeted tests under a future `tests/` directory, for example `tests/test_booking_flow.py`. Prioritize slot validation, order lifecycle actions, and error branches around time or phone parsing. For changes that do not justify full tests, at minimum run `python -m py_compile main.py` and manually verify one booking and one failure path.

## Commit & Pull Request Guidelines
Recent history mixes short subjects and Conventional Commit style, for example `fix: workflows node 版本` and `feat(agents): 添加 LangGraph Agent 基础示例代码集`. Prefer concise messages in that style: `feat(agent): 支持订单取消校验`. Keep each commit focused on one behavior change. PRs should include a short summary, impacted files, manual test notes, required `.env` changes, and terminal screenshots only when CLI behavior changes materially.

## Security & Configuration Tips
Do not commit real API keys or provider endpoints. Copy [`.env.example`](/Users/Zhuanz/lvsoso/rnotes/code/agents/cake-booking/.env.example) to `.env`, set `OPENAI_API_KEY`, and optionally `OPENAI_BASE_URL` for proxy access. Treat mock order data as in-memory only; if persistence is introduced later, document migration and data-handling rules in the same PR.
