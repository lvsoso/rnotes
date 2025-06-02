import os
from typing import List, Dict, Any
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
        # 模拟搜索功能
        if "天气" in query.lower():
            return "搜索结果：今天天气晴朗，温度：25"  # 直接返回数字，方便后续计算
        elif "新闻" in query.lower():
            return "搜索结果：最新科技新闻：AI技术持续发展。"
        return f"搜索结果：找到关于 '{query}' 的一般信息。"

class CalculatorTool(Tool):
    def __init__(self):
        super().__init__(
            name="Calculator",
            description="用于执行基本的数学计算。输入应该是一个数学表达式字符串。"
        )

    def run(self, expression: str) -> str:
        try:
            # 警告：在实际应用中应该使用更安全的计算方法
            result = eval(expression)
            return f"计算结果：{result}"
        except Exception as e:
            return f"计算错误：{str(e)}"

class PlanAndExecuteAgent:
    def __init__(self, tools: List[Tool], max_retries: int = 3, max_plan_attempts: int = 10):
        self.tools = {tool.name: tool for tool in tools}
        self.plan = []
        self.max_retries = max_retries          # 每个步骤的最大重试次数
        self.max_plan_attempts = max_plan_attempts  # 计划失败后的最大重新规划次数
        
    def _create_planning_prompt(self, task: str, failed_plan: str = "", failed_reason: str = "") -> str:
        tools_desc = "\n".join([
            f"- {tool.name}: {tool.description}" 
            for tool in self.tools.values()
        ])
        
        additional_context = ""
        if failed_plan and failed_reason:
            additional_context = f"""
之前的计划执行失败：
{failed_plan}
失败原因：{failed_reason}
请基于上述失败经验，生成一个更好的计划。
"""
        
        return f"""作为一个计划制定者，请为完成以下任务制定详细的执行计划。

可用工具：
{tools_desc}

任务：{task}

{additional_context}
请按照以下格式列出完成任务所需的步骤：
1. [步骤描述] => [使用的工具/Finish]
2. [步骤描述] => [使用的工具/Finish]
...

确保每个步骤都清晰具体，并指明使用哪个工具或是完成标记(Finish)。
要求步骤之间要有明确的依赖关系，后面的步骤要使用前面步骤的结果。
"""

    def _create_execution_prompt(self, step: str, step_num: int, 
                               prev_results: List[str], retry_count: int = 0) -> str:
        context = "\n".join([
            f"步骤 {i+1} 结果: {result}" 
            for i, result in enumerate(prev_results)
        ])
        
        tools_desc = "\n".join([
            f"- {tool.name}: {tool.description}" 
            for tool in self.tools.values()
        ])
        
        retry_context = ""
        if retry_count > 0:
            retry_context = f"\n这是第 {retry_count + 1} 次尝试执行此步骤。请调整策略，避免重复之前的错误。"
        
        return f"""作为一个执行者，请执行以下步骤：

可用工具：
{tools_desc}

当前步骤 {step_num}: {step}{retry_context}

之前步骤的结果：
{context}

请提供：
1. 要使用的工具名称（或 Finish 表示完成）
2. 工具的具体输入内容（或最终答案）

请严格按以下格式回复：
选择工具: [工具名称/Finish]
执行输入: [输入内容/最终答案]"""

    def _get_plan(self, task: str, failed_plan: str = "", failed_reason: str = "") -> List[str]:
        """生成执行计划，支持基于失败经验重新规划"""
        prompt = self._create_planning_prompt(task, failed_plan, failed_reason)
        try:
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "你是一个善于计划和学习经验的 AI 助手。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
            )
            plan_text = response.choices[0].message.content.strip()
            # 解析计划
            steps = []
            for line in plan_text.split('\n'):
                if line.strip() and '=>' in line:
                    step = line.strip().split('=>')[0].strip()
                    steps.append(step)
            return steps
        except Exception as e:
            print(f"生成计划时出错：{e}")
            return ["无法生成计划"]

    def _execute_step(self, step: str, step_num: int, 
                     prev_results: List[str], retry_count: int = 0) -> tuple[str, bool, bool]:
        """
        执行单个步骤，支持重试
        返回值：(结果, 是否是Finish步骤, 是否执行成功)
        """
        prompt = self._create_execution_prompt(step, step_num, prev_results, retry_count)
        try:
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "你是一个执行任务的 AI 助手。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
            )
            execution = response.choices[0].message.content.strip()
            
            # 解析执行结果
            lines = execution.split('\n')
            selected_tool = ""
            execution_input = ""
            
            for line in lines:
                if line.startswith("选择工具:"):
                    selected_tool = line.replace("选择工具:", "").strip()
                elif line.startswith("执行输入:"):
                    execution_input = line.replace("执行输入:", "").strip()
            
            if not selected_tool or not execution_input:
                if retry_count < self.max_retries:
                    print(f"响应格式不正确，准备重试...")
                    return self._execute_step(step, step_num, prev_results, retry_count + 1)
                return "无法解析响应格式", False, False
            
            # 处理最终答案
            if selected_tool.lower() == "finish":
                return execution_input, True, True
            
            # 执行工具调用
            if selected_tool in self.tools:
                try:
                    result = self.tools[selected_tool].run(execution_input)
                    # 验证结果是否有效
                    if "错误" in result or "失败" in result:
                        raise ValueError(f"工具执行失败: {result}")
                    return result, False, True
                except Exception as e:
                    if retry_count < self.max_retries:
                        print(f"步骤执行失败，准备重试: {e}")
                        return self._execute_step(step, step_num, prev_results, retry_count + 1)
                    raise
            
            return f"未知的工具: {selected_tool}", False, False
            
        except Exception as e:
            print(f"执行步骤时出错：{e}")
            if retry_count < self.max_retries:
                print(f"准备第 {retry_count + 1} 次重试...")
                return self._execute_step(step, step_num, prev_results, retry_count + 1)
            return f"执行出错：{str(e)}", False, False

    def run(self, task: str) -> str:
        """运行整个规划和执行过程，支持失败重试和计划修正"""
        print(f"\n=== 开始任务: {task} ===")
        
        failed_plan = ""
        failed_reason = ""
        plan_attempts = 0
        
        while plan_attempts < self.max_plan_attempts:
            # 1. 生成计划
            print(f"\n--- 生成执行计划 (尝试 {plan_attempts + 1}) ---")
            self.plan = self._get_plan(task, failed_plan, failed_reason)
            for i, step in enumerate(self.plan, 1):
                print(f"步骤 {i}: {step}")
            
            # 2. 执行计划
            print("\n--- 开始执行计划 ---")
            results = []
            execution_failed = False
            
            for i, step in enumerate(self.plan, 1):
                print(f"\n执行步骤 {i}: {step}")
                try:
                    result, is_finish, success = self._execute_step(step, i, results)
                    print(f"结果: {result}")
                    
                    if not success:
                        raise ValueError(f"步骤 {i} 执行失败: {result}")
                    
                    # 处理搜索结果中的数字
                    if "温度" in result:
                        try:
                            # 尝试提取数字
                            import re
                            numbers = re.findall(r'\d+', result)
                            if numbers:
                                result = numbers[0]  # 使用第一个找到的数字
                        except Exception as e:
                            print(f"提取数字时出错: {e}")
                    
                    results.append(result)
                except Exception as e:
                    execution_failed = True
                    failed_plan = "\n".join([f"{j+1}. {s}" for j, s in enumerate(self.plan)])
                    failed_reason = f"在步骤 {i} 失败: {str(e)}"
                    print(f"\n计划执行失败: {failed_reason}")
                    break
            
            # 如果执行没有失败，但也没有得到最终答案（没有遇到Finish），继续尝试新计划
            if not execution_failed:
                return "计划执行完毕。"

            
            # 如果执行失败了，尝试新的计划
            plan_attempts += 1
            if plan_attempts < self.max_plan_attempts:
                print(f"\n准备尝试新的执行计划 ({plan_attempts + 1}/{self.max_plan_attempts})...")
                continue
            
        return f"在 {self.max_plan_attempts} 次尝试后仍未能完成任务。最后的错误: {failed_reason}"

if __name__ == "__main__":
    # 初始化工具和代理
    tools = [SearchTool(), CalculatorTool()]
    agent = PlanAndExecuteAgent(
        tools=tools,
        max_retries=3,        # 每个步骤最多重试3次
        max_plan_attempts=10   # 整体计划最多重试2次
    )
    
    # 测试任务
    tasks = [
        "查询今天的天气，并计算目前气温加10度是多少"
    ]
    
    for task in tasks:
        print("\n" + "="*50)
        result = agent.run(task)
        print(f"\n最终结果: {result}")
        print("="*50)
