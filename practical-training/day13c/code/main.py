import requests
import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
base_url = 'https://dashscope.aliyuncs.com/compatible-mode/v1'

print("--- Requesting using raw requests ---")
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}
data = {
    "model": "qwen3-max",
    "messages": [
        {"role": "user", "content": "你好，请用一句话介绍自己。"}
    ]
}
response = requests.post(f"{base_url}/chat/completions", headers=headers, json=data)
if response.status_code == 200:
    print(response.json()['choices'][0]['message']['content'])
else:
    print(f"Error: {response.status_code} - {response.text}")

print("\n--- Requesting using openai SDK (stream output) ---")
client = OpenAI(api_key=api_key, base_url=base_url)

resp = client.chat.completions.create(
    model='qwen3-max',
    stream=True,
    messages=[
        {'role': 'user', 'content': '你是一个诗人，请写两句描写春天的诗。'}
    ]
)

for chunk in resp:
    print(chunk.choices[0].delta.content or '', end='', flush=True)
print("\n")
