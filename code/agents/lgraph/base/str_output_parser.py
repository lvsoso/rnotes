import os
from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_core.prompts import FewShotChatMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser


llm = ChatOpenAI(
    model_name=os.getenv("LLM_MODEL_ID"),
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL"),
)


prompt = ChatPromptTemplate.from_messages([
    ("human", "请写一首关于 {topic} 的诗 ")
])

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

result = chain.invoke({"topic": "秋天"})
print(type(result))  # <class 'str'>
print(result)

