from typing import List
import json
import os
import subprocess
from pathlib import Path

from llm_client import llm_client as lc


WORKDIR = Path.cwd()
SYSTEM = f"""You are a coding agent at {WORKDIR}.
Use the todo tool to plan multi-step tasks. Mark in_progress before starting, completed when done.
Prefer tools over prose."""


class TodoManager:
    def __init__(self):
        self.todos = []
    
    def update(self, todos: List) -> str:
        if len(todos) > 20:
            raise ValueError("Max 20 todos allowed")
        
        validated = []
        in_progress_count = 0
        for i, todo in enumerate(todos):
            text = str(todo.get("text", "")).strip()
            status = str(todo.get("status", "pending")).strip().lower()
            todo_id = str(todo.get("id", str(i+1)))
            if not text:
                raise ValueError(f"Todo {todo_id} text cannot be empty")
            if status not in ["pending", "in_progress", "completed"]:
                raise ValueError(f"Todo {todo_id} status must be pending, in_progress, or completed")
            if status == "in_progress":
                in_progress_count += 1
            validated.append({"text": text, "status": status, "id": todo_id})
        if in_progress_count > 1:
            raise ValueError("Only one todo can be in_progress")
        self.todos = validated
        return self.render()
    
    def render(self) -> str:
        if not self.todos:
            return "No todos."
        lines = []
        for todo in self.todos:
            marker = {"pending": "[ ]", "in_progress": "[>]", "completed": "[x]"}[todo["status"]]
            lines.append(f"{marker} #{todo['id']}: {todo['text']}")
        done = sum(1 for t in self.todos if t["status"] == "completed")
        lines.append(f"\n({done}/{len(self.todos)} completed)")
        return "\n".join(lines)

TODO = TodoManager()



def safe_path(p: str) -> Path:
    path = (WORKDIR / p).resolve()
    if not path.is_relative_to(WORKDIR):
        raise ValueError(f"Path escapes workspace: {p}")
    return path


def run_bash(command: str) -> str:
    dangerous = ["rm -rf /", "sudo", "shutdown", "reboot", "> /dev/"]
    if any(d in command for d in dangerous):
        return "Error: Dangerous command blocked"
    try:
        r = subprocess.run(
            command, shell=True, cwd=WORKDIR, capture_output=True, text=True, timeout=120
        )
        out = (r.stdout + r.stderr).strip()
        return out[:50000] if out else "(no output)"
    except subprocess.TimeoutExpired:
        return "Error: Timeout (120s)"


def run_read(path: str, limit: int = None) -> str:
    try:
        text = safe_path(path).read_text()
        lines = text.splitlines()
        if limit and limit < len(lines):
            lines = lines[:limit] + [f"... ({len(lines) - limit} more lines)"]
        return "\n".join(lines)[:50000]
    except Exception as e:
        return f"Error: {e}"


def run_write(path: str, content: str) -> str:
    try:
        fp = safe_path(path)
        fp.parent.mkdir(parents=True, exist_ok=True)
        fp.write_text(content)
        return f"wrote {len(content)} bytes to {fp}"
    except Exception as e:
        return f"Error: {e}"


def run_edit(path: str, old_text: str, new_text: str) -> str:
    try:
        fp = safe_path(path)
        content = fp.read_text()
        if old_text not in content:
            return f"Error: {old_text!r} not found in {path}"
        fp.write_text(content.replace(old_text, new_text, 1))
        return f"edited {path}"
    except Exception as e:
        return f"Error: {e}"


TOOL_HANDLERS = {
    "bash": lambda **kw: run_bash(kw["command"]),
    "read_file": lambda **kw: run_read(kw["path"], kw.get("limit")),
    "write_file": lambda **kw: run_write(kw["path"], kw["content"]),
    "edit_file": lambda **kw: run_edit(kw["path"], kw["old_text"], kw["new_text"]),
    "todo":       lambda **kw: TODO.update(kw["todos"]),
}


# OpenAI 格式的工具定义
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "bash",
            "description": "Run a shell command.",
            "parameters": {
                "type": "object",
                "properties": {"command": {"type": "string"}},
                "required": ["command"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read file contents.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "limit": {"type": "integer"},
                },
                "required": ["path"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "Write content to file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "content": {"type": "string"},
                },
                "required": ["path", "content"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "edit_file",
            "description": "Replace exact text in file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {"type": "string"},
                    "old_text": {"type": "string"},
                    "new_text": {"type": "string"},
                },
                "required": ["path", "old_text", "new_text"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "todo",
            "description": "Update task list. Track progress on multi-step tasks.",
            "parameters": {
                "type": "object",
                "properties": {
                    "todos": {"type": "array", "items": {"type": "object", "properties": {"id": {"type": "string"}, "text": {"type": "string"}, "status": {"type": "string", "enum": ["pending", "in_progress", "completed"]}}, "required": ["id", "text", "status"]}}}
                },
                "required": ["todos"],
            },
    }
]

def agent_loop(messages: list):
    """Agent loop with todo reminder."""
    rounds_since_todo = 0

    while True:
        response = lc.complete_result(messages, system=SYSTEM, tools=TOOLS)

        # 检查本轮是否使用了 todo
        used_todo = any(
            tc.get("function", {}).get("name") == "todo"
            for tc in response.tool_calls
        )

        if used_todo:
            rounds_since_todo = 0
        else:
            rounds_since_todo += 1

        # 如果没有 tool_calls，添加回复并结束
        if not response.tool_calls:
            print(response.text)
            messages.append({"role": "assistant", "content": response.text})
            return response.text

        # 添加 assistant 消息（包含 tool_calls）
        tool_calls_for_msg = []
        for tc in response.tool_calls:
            tool_calls_for_msg.append({
                "id": tc.get("id"),
                "type": "function",
                "function": {
                    "name": tc.get("function", {}).get("name"),
                    "arguments": tc.get("function", {}).get("arguments", "{}"),
                },
            })

        messages.append({
            "role": "assistant",
            "content": response.text or "",
            "tool_calls": tool_calls_for_msg,
        })

        # 执行每个 tool call
        for tc in response.tool_calls:
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

            print(f"\033[33m$ {name}\033[0m")
            print(output[:200] if len(output) > 200 else output)

            # 添加 tool 返回结果
            messages.append({"role": "tool", "tool_call_id": tc.get("id"), "content": output})

        # 如果连续3轮没用 todo，提醒更新
        if rounds_since_todo >= 3:
            messages.append({
                "role": "user",
                "content": "<reminder>Remember to update your todos to track progress.</reminder>"
            })



if __name__ == "__main__":
    history = []
    while True:
        try:
            query = input("\033[36ms01 >> \033[0m")
        except (EOFError, KeyboardInterrupt):
            break
        if query.strip().lower() in ("q", "exit", "quit"):
            break
        history.append({"role": "user", "content": query})
        result = agent_loop(history)
        print()
