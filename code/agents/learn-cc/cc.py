import json
import os
import subprocess

from llm_client import llm_client as lc

SYSTEM = f"You are a coding agent at {os.getcwd()}. Use bash to solve tasks. Act, don't explain."

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
    }
]


def run_bash(command: str) -> str:
    dangerous = ["rm -rf /", "sudo", "shutdown", "reboot", "> /dev/"]
    if any(d in command for d in dangerous):
        return "Error: Dangerous command blocked"
    try:
        r = subprocess.run(
            command, shell=True, cwd=os.getcwd(), capture_output=True, text=True, timeout=120
        )
        out = (r.stdout + r.stderr).strip()
        return out[:50000] if out else "(no output)"
    except subprocess.TimeoutExpired:
        return "Error: Timeout (120s)"


def agent_loop(messages: list):
    while True:
        response = lc.complete_result(messages, system=SYSTEM, tools=TOOLS)

        # 查看原始响应
        print(f"DEBUG: tool_calls={response.tool_calls}")
        print(f"DEBUG: raw message={response.raw['choices'][0]['message']}")

        # 如果没有 tool_calls，添加回复并结束
        if not response.tool_calls:
            print(response.text)
            messages.append({"role": "assistant", "content": response.text})
            return response.text

        # 添加 assistant 消息（包含 tool_calls）
        messages.append(
            {"role": "assistant", "content": response.text, "tool_calls": response.tool_calls}
        )

        # 执行每个 tool call
        for tc in response.tool_calls:
            func = tc["function"]
            name, args = func["name"], json.loads(func["arguments"])

            if name == "bash":
                cmd = args["command"]
                print(f"\033[33m$ {cmd}\033[0m")
                output = run_bash(cmd)
                print(output[:200] if len(output) > 200 else output)

                # 添加 tool 返回结果
                messages.append({"role": "tool", "tool_call_id": tc["id"], "content": output})
        # 循环继续，让 LLM 基于 tool 结果生成回复


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
