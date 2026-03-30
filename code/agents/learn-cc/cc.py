"""Coding Agent 入口"""
import json

from config import WORKDIR, THRESHOLD
from llm_client import llm_client as lc
from skills import SKILL_LOADER
from teams import BUS, TEAM
from todos import TODO
from tools import PARENT_TOOLS, run_bash, run_read, run_write, run_edit
from subagent import run_subagent
from compacts import micro_compact, auto_compact, estimate_tokens
from tasks import TASKS
from background import BG


SYSTEM = f"""You are a coding agent at {WORKDIR}.
Prefer task_create/task_update/task_list for multi-step work. Use TodoWrite for short checklists.
Use task for subagent delegation. Use load_skill for specialized knowledge.
Skills available:
{SKILL_LOADER.get_descriptions()}
"""


TOOL_HANDLERS = {
    "bash": lambda **kw: run_bash(kw["command"]),
    "read_file": lambda **kw: run_read(kw["path"], kw.get("limit")),
    "write_file": lambda **kw: run_write(kw["path"], kw["content"]),
    "edit_file": lambda **kw: run_edit(kw["path"], kw["old_text"], kw["new_text"]),
    "todo": lambda **kw: TODO.update(kw["todos"]),
    "task": lambda **kw: run_subagent(kw["prompt"]),
    "load_skill": lambda **kw: SKILL_LOADER.get_content(kw["name"]),
    "compact":    lambda **kw: "Manual compression requested.",
    "task_create": lambda **kw: TASKS.create(kw["subject"], kw.get("description", "")),
    "task_update": lambda **kw: TASKS.update(kw["task_id"], kw.get("status"), kw.get("add_blocked_by"), kw.get("add_blocks")),
    "task_list":   lambda **kw: TASKS.list_all(),
    "task_get":    lambda **kw: TASKS.get(kw["task_id"]),
    "background_run":   lambda **kw: BG.run(kw["command"]),
    "check_background": lambda **kw: BG.check(kw.get("task_id")),
    "spawn_teammate":  lambda **kw: TEAM.spawn(kw["name"], kw["role"], kw["prompt"]),
    "list_teammates":  lambda **kw: TEAM.list_all(),
    "send_message":    lambda **kw: BUS.send("lead", kw["to"], kw["content"], kw.get("msg_type", "message")),
    "read_inbox":      lambda **kw: json.dumps(BUS.read_inbox("lead"), indent=2),
    "broadcast":       lambda **kw: BUS.broadcast("lead", kw["content"], TEAM.member_names()),
}


def agent_loop(messages: list, max_rounds: int = 30):
    """Agent loop with todo reminder."""
    rounds_since_todo = 0

    for _ in range(max_rounds):
        micro_compact(messages)
        if estimate_tokens(messages) > THRESHOLD:
            print("[auto_compact triggered]")
            messages[:] = auto_compact(messages)
        manual_compact = False

        notifs = BG.drain_notifications()
        if notifs and messages:
            notif_text = "\n".join(
                f"[bg:{n['task_id']}] {n['status']}: {n['result']}" for n in notifs
            )
            messages.append({"role": "user", "content": f"<background-results>\n{notif_text}\n</background-results>"})

        response = lc.complete_result(messages, system=SYSTEM, tools=PARENT_TOOLS)

        used_todo = any(
            tc.get("function", {}).get("name") == "todo"
            for tc in (response.tool_calls or [])
        )

        if used_todo:
            rounds_since_todo = 0
        else:
            rounds_since_todo += 1

        if not response.tool_calls:
            print(response.text)
            messages.append({"role": "assistant", "content": response.text})
            return response.text

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

            if name == "compact":
                manual_compact = True

            print(f"\033[33m$ {name}\033[0m")
            print(output[:200] if len(output) > 200 else output)

            messages.append({"role": "tool", "tool_call_id": tc.get("id"), "content": output})
        
        if manual_compact:
            print("[manual compact]")
            messages[:] = auto_compact(messages)

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
        if query.strip() == "/team":
            print(TEAM.list_all())
            continue
        if query.strip() == "/inbox":
            print(json.dumps(BUS.read_inbox("lead"), indent=2))
            continue
        history.append({"role": "user", "content": query})
        result = agent_loop(history)
        print()
