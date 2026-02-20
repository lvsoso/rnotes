import os
from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_core.prompts import FewShotChatMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field


llm = ChatOpenAI(
    model_name=os.getenv("LLM_MODEL_ID"),
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL"),
)



class Person(BaseModel):
    name: str = Field(description="人物姓名")
    age: int = Field(description="年龄")
    occupation: str = Field(description="职业")
    skills: list[str] = Field(description="技能列表")

parser = PydanticOutputParser(pydantic_object=Person)

prompt = ChatPromptTemplate.from_messages([
    ("system", "从文本中提取人物信息并输出\n{format_instructions}"),
    ("human", "{text}")
])

chain = prompt | llm | parser

result = chain.invoke({
    "text": "小明是一位 35 岁的资深算法工程师，精通 Python、机器学习、深度学习",
    "format_instructions": parser.get_format_instructions()
})

print(type(result))  # <class '__main__.Person'>
print(f"姓名：{result.name}")
print(f"年龄：{result.age}")
print(f"职业：{result.occupation}")
print(f"技能：{', '.join(result.skills)}")
