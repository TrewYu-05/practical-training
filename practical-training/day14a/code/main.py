from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(base_url='https://dashscope.aliyuncs.com/compatible-mode/v1', api_key=api_key)

user_input = "空间够大，但是避震太硬了，过个减速带颠得要命，考虑退车。" # Mocking user input for the screenshot script

messages = [
    {'role': 'system', 'content': '你是一个文档分类器。请根据我提供的示例，严格判断用户输入的情感倾向。只输出一个词，正面、负面或中性。不要输出任何解释' },
    {'role': 'user', 'content': '换电池报价8万2！二手车商都不敢收，所谓终身质保条款藏着无数套路，新能源韭菜真不是白叫的。'},
    {'role': 'assistant', 'content': '负面'},
    {'role': 'user', 'content': '驾乘体验非常舒服，增程式没有续航焦虑，月均油电费才300块，国产新能源神车当之无愧。'},
    {'role': 'assistant', 'content': '正面'},
    {'role': 'user', 'content': '驾驶质感不错，但车机逻辑混乱需要适应，价格是否合理建议先试驾后再评判，仁者见仁智者见智。'},
    {'role': 'assistant', 'content': '中性'},
    {'role': 'user', 'content': user_input},
]

resp = client.chat.completions.create(
    model='qwen3-max',
    stream=True,
    messages=messages
)

print(f"用户评价: {user_input}")
print("情感分析结果: ", end="")
for chunk in resp:
    print(chunk.choices[0].delta.content or '', end='')
print("\n")
