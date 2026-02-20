import os
from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_core.prompts import FewShotChatMessagePromptTemplate



llm = ChatOpenAI(
    model_name=os.getenv("LLM_MODEL_ID"),
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL"),
)


# 定义示例
examples = [
    {"input": "开心", "output": "😊"},
    {"input": "难过", "output": "😢"},
    {"input": "愤怒", "output": "😠"},
]

example_prompt = ChatPromptTemplate.from_messages([
    ("human", "{input}"),
    ("ai", "{output}"),
])

few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)

final_prompt = ChatPromptTemplate.from_messages([
    ("system", "你需要将情绪词转换为对应的 emoji"),
    few_shot_prompt,
    ("human", "{input}"),
])

chain = final_prompt | llm
response = chain.invoke({"input": "兴奋"})
print(response.content)