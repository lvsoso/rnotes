import os
from openai import OpenAI


client = OpenAI(
   
    api_key="na", 
    base_url="http://localhost:6006/v1",
)


completion = client.chat.completions.create(
    model="Qwen3-8B", 
    messages=[
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': 'If $x^2 + 100x + c$ can be expressed as the square of a binomial, what is the value of the constant $c$?'}
        ]
)
print(completion.choices[0].message.content)