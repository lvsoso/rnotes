"""子代理功能"""
import json

from config import WORKDIR
from llm_client import llm_client as lc
from skills import SKILL_LOADER
from tools import CHILD_TOOLS, run_bash, run_read, run_write, run_edit
from todos import TODO

SUBAGENT_SYSTEM = f"""You are a coding subagent at {WORKDIR}.
Complete the given task, then summarize your findings.

Skills available:
{SKILL_LOADER.get_descriptions()}
"""


TOOL_HANDLERS = {
    "bash": lambda **kw: run_bash(kw["command"]),
    "read_file": lambda **kw: run_read(kw["path"], kw.get("limit")),
    "write_file": lambda **kw: run_write(kw["path"], kw["content"]),
    "edit_file": lambda **kw: run_edit(kw["path"], kw["old_text"], kw["new_text"]),
    "todo": lambda **kw: TODO.update(kw["todos"]),
    "load_skill": lambda **kw: SKILL_LOADER.get_content(kw["name"])
}


def run_subagent(prompt: str) -> str:
    sub_messages = [{"role": "user", "content": prompt}]
    for _ in range(30):
        response = lc.complete_result(sub_messages, system=SUBAGENT_SYSTEM, tools=CHILD_TOOLS)
        sub_messages.append({"role": "assistant", "content": response.text})
        if not response.tool_calls:
            break
        for tc in response.tool_calls or []:
            func = tc.get("function", {})
            name = func.get("name")
            args_str = func.get("arguments", "{}")

            try:
                args = json.loads(args_str) if isinstance(args_str, str) else args_str
            except json.JSONDecodeError as e:
                output = f"Error: Invalid arguments JSON - {e}"
            else:
                handler = TOOL_HANDLERS.get(name)
                try:
                    output = handler(**args) if handler else f"Unknown tool: {name}"
                except Exception as e:
                    output = f"Error executing {name}: {e}"
            sub_messages.append({"role": "tool", "tool_call_id": tc.get("id"), "content": output})

    for m in reversed(sub_messages):
        if m["role"] == "assistant":
            return m["content"]
    return ""
