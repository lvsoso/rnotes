import os
import json
from openai import OpenAI

# 设置 API key 和基础 URL
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "YOUR_DEEPSEEK_API_KEY")
if DEEPSEEK_API_KEY == "YOUR_DEEPSEEK_API_KEY":
    print("警告: 请设置你的 DEEPSEEK_API_KEY 环境变量或直接在代码中替换。")
    exit()

# 初始化 OpenAI 客户端，设置为 DeepSeek 的 API
client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com/v1"  # DeepSeek API 的基础 URL
)

class SearchTool:
    def __init__(self):
        self.name = "Search"
        self.description = "用于在网络上搜索信息。输入应该是一个搜索查询字符串。"

    def run(self, query: str) -> str:
        # 这是一个模拟的搜索功能
        if "你好" in query.lower():
            return "搜索结果：你好，世界！"
        elif "deepseek" in query.lower():
            return "搜索结果：DeepSeek 是一个由深度求索公司开发的人工智能模型。"
        elif "react" in query.lower() and "agent" in query.lower():
            return "搜索结果：ReAct Agent 是一种结合了推理 (Reasoning) 和行动 (Acting) 的 AI 代理模式。"
        return f"搜索结果：抱歉，没有找到关于 '{query}' 的确切信息。"

class SimpleReActAgent:
    def __init__(self, tools, max_iterations=5):
        self.tools = {tool.name: tool for tool in tools}
        self.max_iterations = max_iterations
        self.history = []

    def _build_prompt(self, task: str) -> str:
        # 构建 ReAct 风格的提示
        tool_descriptions = "\n".join(
            [f"- {name}: {tool.description}" for name, tool in self.tools.items()]
        )

        prompt = f"""你是一个助手，通过思考和行动来完成任务。

可用工具：
{tool_descriptions}

请严格按照以下格式回复：
Thought: [你的思考过程]
Action: [行动，可以是 {', '.join(self.tools.keys())} 或 Finish]
Action Input: [行动的输入，如果是 Finish 则是最终答案]

任务: {task}
"""
        # 添加历史记录
        for entry in self.history:
            prompt += f"\nThought: {entry['thought']}"
            prompt += f"\nAction: {entry['action']}"
            prompt += f"\nAction Input: {entry['action_input']}"
            prompt += f"\nObservation: {entry['observation']}\n"

        return prompt

    def _call_llm(self, prompt: str) -> str:
        try:
            # 使用 OpenAI 风格的接口调用 DeepSeek
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "你是一个遵循 ReAct 模式的 AI 助手。"},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.1,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"调用 API 出错: {e}")
            return "Action: Finish\nAction Input: API 调用失败"

    def _parse_response(self, response: str) -> tuple[str, str, str]:
        thought = action = action_input = ""
        
        for line in response.split('\n'):
            if line.startswith("Thought:"):
                thought = line.replace("Thought:", "").strip()
            elif line.startswith("Action:"):
                action = line.replace("Action:", "").strip()
            elif line.startswith("Action Input:"):
                action_input = line.replace("Action Input:", "").strip()

        if not thought:
            thought = "未提供思考过程"
        if not action:
            action = "Finish"
            action_input = "无法解析行动"

        return thought, action, action_input

    def run(self, task: str) -> str:
        self.history = []
        print(f"\n开始任务: {task}")

        for i in range(self.max_iterations):
            print(f"\n--- 迭代 {i + 1} ---")
            
            # 1. 构建提示
            prompt = self._build_prompt(task)
            
            # 2. 调用 LLM
            response = self._call_llm(prompt)
            print(f"LLM 响应:\n{response}")
            
            # 3. 解析响应
            thought, action, action_input = self._parse_response(response)
            print(f"解析响应:")
            print(f"思考: {thought}")
            print(f"行动: {action}")
            print(f"输入: {action_input}")

            # 4. 处理行动
            if action.lower() == "finish":
                print(f"完成任务: {action_input}")
                return action_input

            # 5. 执行工具调用
            if action in self.tools:
                tool = self.tools[action]
                try:
                    observation = tool.run(action_input)
                    print(f"观察: \n {observation}")
                    self.history.append({
                        "thought": thought,
                        "action": action,
                        "action_input": action_input,
                        "observation": observation
                    })
                except Exception as e:
                    print(f"工具执行错误: {e}")
                    return f"工具执行失败: {str(e)}"
            else:
                print(f"未知行动: {action}")
                return f"错误：未知的行动 '{action}'"

        return "达到最大迭代次数，任务未完成"

if __name__ == "__main__":
    # 初始化工具和代理
    search_tool = SearchTool()
    agent = SimpleReActAgent(tools=[search_tool])

    # 测试任务
    tasks = [
        "什么是 ReAct Agent？",
        "搜索一下关于你好的信息",
    ]

    for task in tasks:
        print("\n" + "="*50)
        print(f"执行任务: {task}")
        result = agent.run(task)
        print(f"\n最终答案: {result}")
        print("="*50)
