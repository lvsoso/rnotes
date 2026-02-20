import os
from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_core.prompts import FewShotChatMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser


llm = ChatOpenAI(
    model_name=os.getenv("LLM_MODEL_ID"),
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL"),
)


parser = JsonOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system", "请以 JSON 格式输出，必须包含 'title' 和 'summary' 字段"),
    ("human", "总结这段文章：{article}")
])

chain = prompt | llm | parser

result = chain.invoke({
    "article": "LangChain 是一个强化大语言模型应用的框架，提供了模型调用、提示词工程、工具集成等核心功能"
})

print(type(result))  # <class 'dict'>
print(result)

