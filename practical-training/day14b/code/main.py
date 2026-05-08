from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(base_url='https://dashscope.aliyuncs.com/compatible-mode/v1', api_key=api_key)

print("--- Initial chat without memory ---")
resp = client.chat.completions.create(
    model='qwen3-max',
    messages=[
        {'role': 'user', 'content': '我的叫丁致宇，是一名python工程师'},
    ]
)
print("用户: 我的叫丁致宇，是一名python工程师")
answer = resp.choices[0].message.content
print(f"AI: {answer}")

resp = client.chat.completions.create(
    model='qwen3-max',
    messages= [
        {'role': 'user', 'content': '我叫什么名字？'},
    ]
)
print("用户: 我叫什么名字？")
print(f"AI: {resp.choices[0].message.content}")

print("\n--- Chat with manually injected context memory ---")
messages = [
    {'role': 'user', 'content': '我的叫丁致宇，是一名python工程师'}
]
print("用户: 我的叫丁致宇，是一名python工程师")
resp = client.chat.completions.create(
    model='qwen3-max',
    messages=messages
)
answer = resp.choices[0].message.content
print(f"AI: {answer}")

# Injecting history
messages.append({'role': 'assistant', 'content': answer})
messages.append({'role': 'user', 'content': '我叫什么名字？'})

print("用户: 我叫什么名字？")
resp = client.chat.completions.create(
    model='qwen3-max',
    messages=messages
)
print(f"AI: {resp.choices[0].message.content}")
