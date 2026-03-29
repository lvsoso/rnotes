from typing import List
import json
import re
import subprocess
from pathlib import Path

from llm_client import llm_client as lc


WORKDIR = Path.cwd()
SKILLS_DIR = WORKDIR / "skills"


class SkillLoader:
    def __init__(self, skills_dir: Path) -> None:
        self.skills_dir = skills_dir
        self.skills = {}
        self._load_all()
    
    def _load_all(self) -> None:
        if not self.skills_dir.exists():
            return
        
        for f in sorted(self.skills_dir.rglob("SKILL.md")):
            text = f.read_text()
            meta, body = self._parse_frontmatter(text)
            name = meta.get("name", f.parent.name)
            self.skills[name] = {"meta": meta, "body": body, "path": str(f)}
    
    def _parse_frontmatter(self, text: str) -> tuple:
        """Parse YAML frontmatter between --- delimiters."""
        match = re.match(r"^---\n(.*?)\n---\n(.*)", text, re.DOTALL)
        if not match:
            return {}, text
        meta = {}
        for line in match.group(1).strip().splitlines():
            if ":" in line:
                key, val = line.split(":", 1)
                meta[key.strip()] = val.strip()
        return meta, match.group(2).strip()

    def get_descriptions(self) -> str:
        """Layer 1: short descriptions for the system prompt."""
        if not self.skills:
            return "(no skills available)"
        lines = []
        for name, skill in self.skills.items():
            desc = skill["meta"].get("description", "No description")
            tags = skill["meta"].get("tags", "")
            line = f"  - {name}: {desc}"
            if tags:
                line += f" [{tags}]"
            lines.append(line)
        return "\n".join(lines)

    def get_content(self, name: str) -> str:
        """Layer 2: full skill body returned in tool_result."""
        skill = self.skills.get(name)
        if not skill:
            return f"Error: Unknown skill '{name}'. Available: {', '.join(self.skills.keys())}"
        return f"<skill name=\"{name}\">\n{skill['body']}\n</skill>"

SKILL_LOADER = SkillLoader(SKILLS_DIR)


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


SYSTEM = f"""You are a coding agent at {WORKDIR}.
Use the todo tool to plan multi-step tasks. Mark in_progress before starting, completed when done.
Prefer tools over prose.
Use the task tool to delegate exploration or subtasks.

Skills available:
{SKILL_LOADER.get_descriptions()}
"""

SUBAGENT_SYSTEM = f"""You are a coding subagent at {WORKDIR}.
Complete the given task, then summarize your findings.

Skills available:
{SKILL_LOADER.get_descriptions()}
"""




def safe_path(p: str) -> Path:
    path = (WORKDIR / p).resolve()
    if not path.is_relative_to(WORKDIR):
        raise ValueError(f"Path escapes workspace: {p}")
    return path


def run_bash(command: str) -> str:
    _BLOCKED_PATTERNS = [
        re.compile(r'\brm\s+-rf\s+/'),
        re.compile(r'\bsudo\b'),
        re.compile(r'\bshutdown\b'),
        re.compile(r'\breboot\b'),
        re.compile(r'>\s*/dev/'),
        re.compile(r'\b(curl|wget)\b.*\|\s*(ba)?sh\b'),
    ]
    for pat in _BLOCKED_PATTERNS:
        if pat.search(command):
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
    except FileNotFoundError:
        return f"Error: File not found: {path}"
    except PermissionError:
        return f"Error: Permission denied: {path}"
    except ValueError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Error: {e}"


def run_write(path: str, content: str) -> str:
    try:
        fp = safe_path(path)
        fp.parent.mkdir(parents=True, exist_ok=True)
        fp.write_text(content)
        return f"wrote {len(content)} bytes to {fp}"
    except PermissionError:
        return f"Error: Permission denied: {path}"
    except ValueError as e:
        return f"Error: {e}"
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
    except FileNotFoundError:
        return f"Error: File not found: {path}"
    except PermissionError:
        return f"Error: Permission denied: {path}"
    except ValueError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Error: {e}"


TOOL_HANDLERS = {
    "bash": lambda **kw: run_bash(kw["command"]),
    "read_file": lambda **kw: run_read(kw["path"], kw.get("limit")),
    "write_file": lambda **kw: run_write(kw["path"], kw["content"]),
    "edit_file": lambda **kw: run_edit(kw["path"], kw["old_text"], kw["new_text"]),
    "todo":       lambda **kw: TODO.update(kw["todos"]),
    "task":       lambda **kw: run_subagent(kw["prompt"]),
    "load_skill": lambda **kw: SKILL_LOADER.get_content(kw["name"])
}


# OpenAI 格式的工具定义
CHILD_TOOLS = [
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
                    "todos": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {"type": "string"},
                                "text": {"type": "string"},
                                "status": {"type": "string", "enum": ["pending", "in_progress", "completed"]}
                            },
                            "required": ["id", "text", "status"]
                        }
                    }
                },
                "required": ["todos"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "load_skill",
            "description": "Load specialized knowledge by name.",
            "parameters": {
                "type": "object",
                "properties": {"name": {"type": "string", "description": "Skill name to load"}},
                "required": ["name"],
            },
        },
    }
]


PARENT_TOOLS = CHILD_TOOLS + [
    {
        "type": "function",
        "function": {
            "name": "task",
            "description": "Spawn a subagent with fresh context. It shares the filesystem but not conversation history.",
            "parameters": {
                "type": "object",
                "properties": {
                    "prompt": {"type": "string"},
                    "description": {"type": "string", "description": "Short description of the task"},
                },
                "required": ["prompt"],
            },
        },
    }
]


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


def agent_loop(messages: list, max_rounds: int = 30):
    """Agent loop with todo reminder."""
    rounds_since_todo = 0

    for _ in range(max_rounds):
        response = lc.complete_result(messages, system=SYSTEM, tools=PARENT_TOOLS)

        # 检查本轮是否使用了 todo
        used_todo = any(
            tc.get("function", {}).get("name") == "todo"
            for tc in (response.tool_calls or [])
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

    return "Error: Max rounds exceeded"



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
