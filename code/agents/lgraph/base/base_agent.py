from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field

from dotenv import load_dotenv
import os

load_dotenv()

class WeatherReport(BaseModel):
    temperature: float = Field(description="温度，单位摄氏度")
    condition: str = Field(description="天气状况，如晴朗、多云等")

def get_weather(city: str) -> str:
    """获取城市天气"""
    return f"{city} 今天天气晴朗，温度25摄氏度"

llm = ChatOpenAI(
    model_name=os.getenv("LLM_MODEL_ID"),
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL"),
)

weather_agent = create_react_agent(
    model=llm,
    tools=[get_weather],
)

from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda

# 使用自定义 Chain 来处理结构化输出，以兼容 Thinking Model 的 <think> 标签
parser = JsonOutputParser(pydantic_object=WeatherReport)

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个信息提取助手。请从文本中提取天气信息并输出 JSON。\n{format_instructions}"),
    ("human", "{text}")
])

def clean_message(msg):
    """清洗模型输出，去除 <think> 标签"""
    if hasattr(msg, 'content'):
        msg.content = re.sub(r'<think>.*?</think>', '', msg.content, flags=re.DOTALL).strip()
        # 处理可能存在的 markdown code block
        msg.content = msg.content.replace('```json', '').replace('```', '').strip()
    return msg

# 构建提取链：Prompt -> LLM -> 清洗 -> 解析
extraction_chain = prompt.partial(format_instructions=parser.get_format_instructions()) | llm | RunnableLambda(clean_message) | parser

# 注意：invoke 需要传入字典格式的消息列表
print("Thinking...")
result = weather_agent.invoke({"messages": [HumanMessage(content="北京今天天气怎么样？")]})

import re

def clean_text(text):
    return re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL).strip()

# 获取 Agent 的最终回复文本
raw_text = result["messages"][-1].content
print(f"Agent Raw Response: {raw_text}")
final_text = clean_text(raw_text)
print(f"Cleaned Response: {final_text}")

# 将非结构化文本转换为结构化数据
print("\nConverting to structured output...")
structured_result = extraction_chain.invoke({"text": final_text})
print("Structured Output:", structured_result)