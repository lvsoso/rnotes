"""Coding Agent 入口"""
import json
import uuid

from config import TASKS_DIR, WORKDIR, THRESHOLD
from llm_client import llm_client as lc
from skills import SKILL_LOADER
from tools import TOOL_HANDLERS
from teams import BUS, TEAM
from tools import PARENT_TOOLS
from compacts import estimate_tokens, micro_compact, auto_compact
from background import BG


SYSTEM = f"""You are a coding agent at {WORKDIR}.
Prefer task_create/task_update/task_list for multi-step work. Use TodoWrite for short checklists.
Use task for subagent delegation. Use load_skill for specialized knowledge.
Skills available:
{SKILL_LOADER.get_descriptions()}
"""



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

        inbox = BUS.read_inbox("lead")
        if inbox:
            messages.append({
                "role": "user",
                "content": f"<inbox>{json.dumps(inbox, indent=2)}</inbox>",
            })

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
        if query.strip() == "/tasks":
            TASKS_DIR.mkdir(exist_ok=True)
            for f in sorted(TASKS_DIR.glob("task_*.json"), 
                            key=lambda f: int(f.stem.split("_")[1])):
                t = json.loads(f.read_text())
                marker = {"pending": "[ ]", "in_progress": "[>]", "completed": "[x]"}.get(t["status"], "[?]")
                owner = f" @{t['owner']}" if t.get("owner") else ""
                print(f"  {marker} #{t['id']}: {t['subject']}{owner}")
            continue
        history.append({"role": "user", "content": query})
        result = agent_loop(history)
        print()
