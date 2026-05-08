from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, FewShotPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')
llm = ChatTongyi(model='qwen3-max', dashscope_api_key=api_key)

print("--- 1. 基础提示词模版 ---")
format_template = PromptTemplate.from_template("""
任务：{task}
时间：{time}
地点：{location}
根据上面的格式（信息）生成一段话
""")
prompt1 = format_template.format(task='开会', time='明天下午3点钟', location='二楼会议室')
print(f"生成的Prompt:\n{prompt1}")
result1 = llm.invoke(prompt1)
print(f"模型输出:\n{result1.content}\n{'-'*30}")

print("--- 2. 聊天型提示词模版 ---")
chat_template = ChatPromptTemplate.from_messages([
    ('system', '你是一个资深的python工程师，请认真回答我提出的问题，并确保回答没有错误'),
    ('human', '写一个python程序，关于{question}')
])
chat_prompt = chat_template.format_messages(question='冒泡排序')
result2 = llm.invoke(chat_prompt)
print(f"模型输出 (开头100字):\n{result2.content[:100]}...\n{'-'*30}")

print("--- 3. 小样本提示词模版 (FewShotPromptTemplate) ---")
examples = [
    {"comment": "这绝对是今年我用过最棒的耳机，音质清晰，降噪无敌！", "sentiment": "正面"},
    {"comment": "太差劲了，才用了一周就坏了，客服也联系不上。", "sentiment": "负面"},
    {"comment": "包裹已经收到了，外包装有点磨损。", "sentiment": "中立"}
]
examples_template = PromptTemplate.from_template('评论：{comment}\n情感：{sentiment}')

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=examples_template,
    prefix='请根据以下示例，判断评论的情感（正面、负面、中立）',
    suffix='评论：{comment}\n情感：',
    input_variables=['comment'],
)
final_prompt = few_shot_prompt.format(comment='手机收到了，系统非常流畅')
print(f"生成的FewShot Prompt:\n{final_prompt}")
result3 = llm.invoke(final_prompt)
print(f"模型输出: {result3.content}")
