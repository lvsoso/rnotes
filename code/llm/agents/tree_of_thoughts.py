import os
from typing import List, Dict, Any, Tuple
from dataclasses import dataclass
from queue import PriorityQueue
import heapq
from openai import OpenAI

# 设置 API key 和基础 URL
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "YOUR_DEEPSEEK_API_KEY")
if DEEPSEEK_API_KEY == "YOUR_DEEPSEEK_API_KEY":
    print("警告: 请设置你的 DEEPSEEK_API_KEY 环境变量或直接在代码中替换。")
    exit()

# 初始化 OpenAI 客户端，设置为 DeepSeek 的 API
client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com/v1"
)

@dataclass
class ThoughtNode:
    """思维节点，表示思维树中的一个节点"""
    thought: str                # 思维内容
    tool_name: str             # 使用的工具名称
    tool_input: str            # 工具输入
    evaluation_score: float    # 评估分数
    depth: int                 # 在树中的深度
    parent: Any                # 父节点
    result: str = ""           # 执行结果
    
    def __lt__(self, other):
        # 用于优先队列的比较，分数越高优先级越高
        return self.evaluation_score > other.evaluation_score

class Tool:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def run(self, input_str: str) -> str:
        raise NotImplementedError("工具必须实现 run 方法")

class SearchTool(Tool):
    def __init__(self):
        super().__init__(
            name="Search",
            description="用于在网络上搜索信息。输入应该是一个搜索查询字符串。"
        )

    def run(self, query: str) -> str:
        if "天气" in query.lower():
            return "搜索结果：今天天气晴朗，温度25度。"
        elif "新闻" in query.lower():
            return "搜索结果：最新科技新闻：AI技术持续发展。"
        elif "股市" in query.lower():
            return "搜索结果：今日股市上涨2%。"
        return f"搜索结果：找到关于 '{query}' 的一般信息。"

class CalculatorTool(Tool):
    def __init__(self):
        super().__init__(
            name="Calculator",
            description="用于执行基本的数学计算。输入应该是一个数学表达式字符串。"
        )

    def run(self, expression: str) -> str:
        try:
            result = eval(expression)
            return f"计算结果：{result}"
        except Exception as e:
            return f"计算错误：{str(e)}"

class TreeOfThoughtsAgent:
    def __init__(self, tools: List[Tool], max_depth: int = 3, beam_width: int = 3):
        self.tools = {tool.name: tool for tool in tools}
        self.max_depth = max_depth        # 最大搜索深度
        self.beam_width = beam_width      # 每层保留的最佳节点数
        
    def _generate_thoughts(self, task: str, context: str = "") -> List[ThoughtNode]:
        """生成多个思维选项"""
        prompt = f"""作为一个思维生成器，请为完成以下任务生成 {self.beam_width} 个不同的思维方向。

可用工具：
{self._format_tools()}

当前任务：{task}

上下文：
{context}

请为每个思维方向指定：
1. 思维内容
2. 要使用的工具
3. 工具的具体输入

请按照以下格式回复 {self.beam_width} 个方案：
1. 思维: [思维内容]
工具: [工具名称]
输入: [工具输入]

2. 思维: [思维内容]
工具: [工具名称]
输入: [工具输入]

...（共 {self.beam_width} 个）
"""
        try:
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "你是一个善于全面思考的 AI 助手。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,  # 使用较高的温度以获得更多样的思维
            )
            
            thoughts = []
            content = response.choices[0].message.content.strip()
            
            # 解析返回的思维
            sections = content.split('\n\n')
            for section in sections:
                if not section.strip():
                    continue
                
                lines = section.strip().split('\n')
                thought = tool = tool_input = ""
                
                for line in lines:
                    if line.startswith("思维:"):
                        thought = line.replace("思维:", "").strip()
                    elif line.startswith("工具:"):
                        tool = line.replace("工具:", "").strip()
                    elif line.startswith("输入:"):
                        tool_input = line.replace("输入:", "").strip()
                
                if thought and tool and tool_input:
                    thoughts.append(ThoughtNode(
                        thought=thought,
                        tool_name=tool,
                        tool_input=tool_input,
                        evaluation_score=0.0,  # 初始分数为0
                        depth=0,
                        parent=None
                    ))
            
            return thoughts
        except Exception as e:
            print(f"生成思维时出错：{e}")
            return []

    def _evaluate_thought(self, thought: ThoughtNode, task: str) -> float:
        """评估思维的质量"""
        prompt = f"""请评估以下思维方案对于完成任务的可能效果。

任务：{task}

思维方案：
{thought.thought}
将使用工具：{thought.tool_name}
工具输入：{thought.tool_input}

如果有执行结果：
{thought.result}

请给出 0-1 之间的评分，其中：
0 表示完全无法帮助解决任务
1 表示非常有助于解决任务

请只回复一个数字，例如：0.75
"""
        try:
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "你是一个公正的评估者。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
            )
            score_str = response.choices[0].message.content.strip()
            return float(score_str)
        except Exception as e:
            print(f"评估思维时出错：{e}")
            return 0.0

    def _format_tools(self) -> str:
        """格式化工具描述"""
        return "\n".join([
            f"- {name}: {tool.description}"
            for name, tool in self.tools.items()
        ])

    def _get_thought_context(self, thought: ThoughtNode) -> str:
        """获取思维的上下文（包括父节点的历史）"""
        context = []
        current = thought
        while current.parent:
            context.append(f"思维: {current.thought}")
            context.append(f"执行: {current.tool_name} - {current.tool_input}")
            context.append(f"结果: {current.result}")
            context.append("---")
            current = current.parent
        return "\n".join(reversed(context))

    def run(self, task: str) -> str:
        """运行 ToT 求解过程"""
        print(f"\n=== 开始任务: {task} ===\n")
        
        # 使用优先队列来管理待扩展的节点
        frontier = PriorityQueue()
        
        # 生成初始思维
        initial_thoughts = self._generate_thoughts(task)
        
        # 评估初始思维并加入队列
        for thought in initial_thoughts:
            # 执行工具调用
            if thought.tool_name in self.tools:
                tool = self.tools[thought.tool_name]
                thought.result = tool.run(thought.tool_input)
            
            # 评估结果
            thought.evaluation_score = self._evaluate_thought(thought, task)
            frontier.put(thought)
            
            print(f"初始思维: {thought.thought}")
            print(f"评分: {thought.evaluation_score}")
            print(f"结果: {thought.result}\n")

        # 追踪最佳解决方案
        best_solution = None
        best_score = 0.0

        # 进行思维树搜索
        while not frontier.empty():
            current = frontier.get()
            
            # 如果当前节点比已知最佳解更好，更新最佳解
            if current.evaluation_score > best_score:
                best_solution = current
                best_score = current.evaluation_score
            
            # 如果达到最大深度，继续处理下一个节点
            if current.depth >= self.max_depth:
                continue
            
            # 生成下一层思维
            context = self._get_thought_context(current)
            next_thoughts = self._generate_thoughts(task, context)
            
            # 评估和扩展新思维
            for thought in next_thoughts:
                thought.depth = current.depth + 1
                thought.parent = current
                
                # 执行工具调用
                if thought.tool_name in self.tools:
                    tool = self.tools[thought.tool_name]
                    thought.result = tool.run(thought.tool_input)
                
                # 评估结果
                thought.evaluation_score = self._evaluate_thought(thought, task)
                frontier.put(thought)
                
                print(f"深度 {thought.depth} 思维: {thought.thought}")
                print(f"评分: {thought.evaluation_score}")
                print(f"结果: {thought.result}\n")

        # 构建最终答案
        if best_solution:
            path = []
            current = best_solution
            while current:
                path.append(f"思维: {current.thought}\n结果: {current.result}")
                current = current.parent
            
            path.reverse()
            final_answer = "\n\n".join(path)
            return f"最终解决方案 (评分 {best_score}):\n\n{final_answer}"
        
        return "未能找到有效的解决方案"

if __name__ == "__main__":
    # 初始化工具和代理
    tools = [SearchTool(), CalculatorTool()]
    agent = TreeOfThoughtsAgent(tools=tools, max_depth=3, beam_width=3)
    
    # 测试任务
    tasks = [
        "分析今天的天气和股市表现，并计算股市涨幅的两倍是多少",
        "搜索最新科技新闻并分析其影响"
    ]
    
    for task in tasks:
        print("\n" + "="*50)
        result = agent.run(task)
        print("\n最终结果:")
        print(result)
        print("="*50)
