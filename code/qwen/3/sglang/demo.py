import os
from openai import OpenAI

client = OpenAI(
   
    api_key="na", 
    base_url="http://localhost:6006/v1",
)


completion = client.chat.completions.create(
    model="na", 
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': '你是谁？'}
        ]
)
print(completion.choices[0].message.content)