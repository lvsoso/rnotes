import os
from openai import OpenAI

client = OpenAI(
   
    api_key="na", 
    base_url="http://127.0.0.1:6006/v1",
)


completion = client.chat.completions.create(
    model="midori", 
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': '说一下什么是大模型'}
        ]
)
print(completion.choices[0].message.content)