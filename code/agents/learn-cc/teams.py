import json
import time
from pathlib import Path
import threading
import uuid
from config import INBOX_DIR, TEAM_DIR, WORKDIR, VALID_MSG_TYPES, MAX_TEAMMATE_TURNS
from llm_client import llm_client as lc
from state import shutdown_requests, plan_requests, tracker_lock


class MessageBus:
    def __init__(self, inbox_dir: Path = None):
        self.inbox_dir = inbox_dir or INBOX_DIR
        self.inbox_dir.mkdir(parents=True, exist_ok=True)

    def send(
        self,
        sender: str,
        to: str,
        content: str,
        msg_type: str = "message",
        extra: dict = None,
    ) -> str:
        if msg_type not in VALID_MSG_TYPES:
            return f"Error: Invalid type '{msg_type}'. Valid: {VALID_MSG_TYPES}"
        msg = {
            "type": msg_type,
            "from": sender,
            "content": content,
            "timestamp": time.time(),
        }
        if extra:
            msg.update(extra)
        with open(self.inbox_dir / f"{to}.jsonl", "a") as f:
            f.write(json.dumps(msg) + "\n")
        return f"Sent {msg_type} to {to}"

    def read_inbox(self, name: str) -> list:
        path = self.inbox_dir / f"{name}.jsonl"
        if not path.exists():
            return []
        msgs = [json.loads(l) for l in path.read_text().strip().splitlines() if l]
        path.write_text("")
        return msgs

    def broadcast(self, sender: str, content: str, names: list) -> str:
        count = 0
        for n in names:
            if n != sender:
                self.send(sender, n, content, "broadcast")
                count += 1
        return f"Broadcast to {count} teammates"


class TeammateManager:

    def __init__(self, team_dir: Path) -> None:
        self.dir = team_dir
        self.dir.mkdir(exist_ok=True, parents=True)
        self.config_path = self.dir / "config.json"
        self.config = self._load_config()
        self.threads = {}

    def _load_config(self) -> dict:
        if self.config_path.exists():
            return json.loads(self.config_path.read_text())
        return {"team_name": "default", "members": []}

    def _save_config(self):
        self.config_path.write_text(json.dumps(self.config, indent=2))

    def _find_member(self, name: str) -> dict:
        for m in self.config["members"]:
            if m["name"] == name:
                return m
        return None

    def spawn(self, name: str, role: str, prompt: str) -> str:
        member = self._find_member(name)
        if member:
            if member["status"] not in ("idle", "shutdown"):
                return f"Error: '{name}' is currently {member['status']}"
            member["status"] = "working"
            member["role"] = role
        else:
            member = {"name": name, "role": role, "status": "working"}
            self.config["members"].append(member)
        self._save_config()
        thread = threading.Thread(
            target=self._teammate_loop,
            args=(name, role, prompt),
            daemon=True,
        )
        self.threads[name] = thread
        thread.start()
        return f"Spawned '{name}' (role: {role})"

    def _teammate_loop(self, name: str, role: str, prompt: str):
        sys_prompt = (
            f"You are '{name}', role: {role}, at {WORKDIR}. "
            f"Submit plans via plan_approval before major work. "
            f"Respond to shutdown_request with shutdown_response."
        )
        messages = [{"role": "user", "content": prompt}]
        tools = self._teammate_tools()
        should_exit = False
        waiting_plan_request_id = None
        llm_turns = 0
        while llm_turns < MAX_TEAMMATE_TURNS:
            inbox = BUS.read_inbox(name)
            for msg in inbox:
                messages.append({"role": "user", "content": json.dumps(msg)})
                if (
                    waiting_plan_request_id
                    and msg.get("type") == "plan_approval_response"
                    and msg.get("request_id") == waiting_plan_request_id
                ):
                    waiting_plan_request_id = None

            if should_exit:
                break

            if waiting_plan_request_id:
                time.sleep(0.05)
                continue

            try:
                response = lc.complete_result(messages, system=sys_prompt, tools=tools)
            except Exception as e:
                print(f"[ERROR] {name}: LLM error - {e}")
                break
            llm_turns += 1

            if not response.tool_calls:
                print(response.text)
                messages.append({"role": "assistant", "content": response.text})
                break

            tool_calls_for_msg = []
            for tc in response.tool_calls:
                tool_calls_for_msg.append(
                    {
                        "id": tc.get("id"),
                        "type": "function",
                        "function": {
                            "name": tc.get("function", {}).get("name"),
                            "arguments": tc.get("function", {}).get("arguments", "{}"),
                        },
                    }
                )

            messages.append(
                {
                    "role": "assistant",
                    "content": response.text or "",
                    "tool_calls": tool_calls_for_msg,
                }
            )

            for tc in response.tool_calls or []:
                func = tc.get("function", {})
                func_name = func.get("name")
                args_str = func.get("arguments", "{}")

                try:
                    args = (
                        json.loads(args_str) if isinstance(args_str, str) else args_str
                    )
                except json.JSONDecodeError as e:
                    output = f"Error: Invalid arguments JSON - {e}"
                else:
                    try:
                        output = self._exec(name, func_name, args)
                    except Exception as e:
                        output = f"Error executing {func_name}: {e}"

                if func_name == "plan_approval" and not output.startswith("Error:"):
                    try:
                        waiting_plan_request_id = json.loads(output)["request_id"]
                    except (json.JSONDecodeError, KeyError, TypeError):
                        output = "Error: Invalid plan approval response payload"

                if func_name == "shutdown_response" and args.get("approve"):
                    should_exit = True

                messages.append(
                    {"role": "tool", "tool_call_id": tc.get("id"), "content": output}
                )

        member = self._find_member(name)
        if member and member["status"] != "shutdown":
            member["status"] = "idle"
            self._save_config()

    def _exec(self, sender: str, tool_name: str, args: dict) -> str:
        from tools import run_bash, run_edit, run_read, run_write
        if tool_name == "bash":
            return run_bash(args["command"])
        if tool_name == "read_file":
            return run_read(args["path"])
        if tool_name == "write_file":
            return run_write(args["path"], args["content"])
        if tool_name == "edit_file":
            return run_edit(args["path"], args["old_text"], args["new_text"])
        if tool_name == "send_message":
            return BUS.send(
                sender, args["to"], args["content"], args.get("msg_type", "message")
            )
        if tool_name == "read_inbox":
            return json.dumps(BUS.read_inbox(sender), indent=2)

        if tool_name == "shutdown_response":
            req_id = args["request_id"]
            approve = args["approve"]
            with tracker_lock:
                if req_id in shutdown_requests:
                    shutdown_requests[req_id]["status"] = "approved" if approve else "rejected"
            BUS.send(
                sender, "lead", args.get("reason", ""),
                "shutdown_response", {"request_id": req_id, "approve": approve},
            )
            return f"Shutdown {'approved' if approve else 'rejected'}"

        if tool_name == "plan_approval":
            plan_text = args.get("plan", "")
            req_id = str(uuid.uuid4())[:8]
            with tracker_lock:
                plan_requests[req_id] = {"from": sender, "plan": plan_text, "status": "pending"}
            BUS.send(
                sender, "lead", plan_text, "plan_approval_request",
                {"request_id": req_id, "plan": plan_text},
            )
            return json.dumps(
                {
                    "request_id": req_id,
                    "status": "pending",
                    "message": "Plan submitted. Waiting for lead approval.",
                }
            )
        return f"Unknown tool: {tool_name}"

    def _teammate_tools(self) -> list:
        return [
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
                    "name": "spawn_teammate",
                    "description": "Spawn a persistent teammate that runs in its own thread.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "role": {"type": "string"},
                            "prompt": {"type": "string"},
                        },
                        "required": ["name", "role", "prompt"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "list_teammates",
                    "description": "List all teammates with name, role, status.",
                    "parameters": {"type": "object", "properties": {}},
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "send_message",
                    "description": "Send a message to a teammate's inbox.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "to": {"type": "string"},
                            "content": {"type": "string"},
                            "msg_type": {
                                "type": "string",
                                "enum": list(VALID_MSG_TYPES),
                            },
                        },
                        "required": ["to", "content"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "read_inbox",
                    "description": "Read and drain your inbox.",
                    "parameters": {"type": "object", "properties": {}},
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "broadcast",
                    "description": "Send a message to all teammates.",
                    "parameters": {
                        "type": "object",
                        "properties": {"content": {"type": "string"}},
                        "required": ["content"],
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "shutdown_response",
                    "description": "Respond to a shutdown request. Approve to shut down, reject to keep working.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "request_id": {"type": "string"},
                            "approve": {"type": "boolean"},
                            "reason": {"type": "string"},
                        },
                        "required": ["request_id", "approve"],
                    },
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "plan_approval",
                    "description": "Submit a plan for lead approval. Provide plan text.",
                    "parameters": {
                        "type": "object",
                        "properties": {"plan": {"type": "string"}},
                        "required": ["plan"],
                    },
                },
            }
        ]

    def list_all(self) -> str:
        if not self.config["members"]:
            return "No teammates."
        lines = [f"Team: {self.config['team_name']}"]
        for m in self.config["members"]:
            lines.append(f"  {m['name']} ({m['role']}): {m['status']}")
        return "\n".join(lines)

    def member_names(self) -> list:
        return [m["name"] for m in self.config["members"]]


BUS = MessageBus(INBOX_DIR)
TEAM = TeammateManager(TEAM_DIR)
