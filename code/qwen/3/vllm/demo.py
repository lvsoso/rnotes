import requests
import json
from PIL import Image
import base64
import time
 
def encode_image(image_path):       # 编码本地图片的函数
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')
 
start = time.time()
url = 'http://127.0.0.1:6006/v1/chat/completions'
 
data = {"model": "Qwen3-8B",
        "messages": [{"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."},     # 系统命令，一般不要改
                     {"role": "user",
                      "content": "Tell me something about large language models."}],    # 用户命令，一般改这里
        "temperature": 0.7,"top_p": 0.8,"repetition_penalty": 1.05,"max_tokens": 1024}

json_payload = json.dumps(data)

headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json_payload, headers=headers) 

print(response.json().get("choices", [])[0].get("message", []).get("content", []))
print("\n总时间：", time.time()-start, "秒")