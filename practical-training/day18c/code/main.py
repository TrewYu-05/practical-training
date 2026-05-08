import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
base_url = 'https://dashscope.aliyuncs.com/compatible-mode/v1'

llm = ChatOpenAI(model='qwen3-max', openai_api_key=api_key, openai_api_base=base_url)

# Prompts
summary_prompt = PromptTemplate.from_template("请对以下内容进行全文总结，控制在50字以内：\n{text}")
translation_prompt = PromptTemplate.from_template("请将以下内容翻译成英文：\n{text}")
title_prompt = PromptTemplate.from_template("请为以下内容提炼一个简短的英文标题：\n{text}")

# Chains
summary_chain = summary_prompt | llm | StrOutputParser()
translation_chain = translation_prompt | llm | StrOutputParser()
title_chain = title_prompt | llm | StrOutputParser()

# Parallel Pipeline
parallel_pipeline = RunnableParallel(
    summary=summary_chain,
    translation=translation_chain,
    english_title=title_chain
)

long_text = """
人工智能（Artificial Intelligence, AI）是指由人制造出来的机器所表现出来的智能。
通常，人工智能是指通过普通计算机程序来呈现人类智能的技术。
该词也指出研究这样的智能系统是否能够实现，以及如何实现。
人工智能的应用领域包括机器人、语言识别、图像识别、自然语言处理和专家系统等。
随着深度学习和大数据技术的发展，AI在医疗、自动驾驶、金融分析等诸多领域取得了突破性进展。
"""

print("开始并发执行流水线...")
result = parallel_pipeline.invoke({"text": long_text})

print("\n=== 全文总结 ===")
print(result['summary'])
print("\n=== 英文翻译 ===")
print(result['translation'])
print("\n=== 英文标题 ===")
print(result['english_title'])
