import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
base_url = 'https://dashscope.aliyuncs.com/compatible-mode/v1'

llm = ChatOpenAI(model='qwen3-max', openai_api_key=api_key, openai_api_base=base_url)

title_chain = PromptTemplate.from_template("请为主题【{topic}】写一个爆款自媒体标题，只输出标题内容：") | llm | StrOutputParser()
outline_chain = PromptTemplate.from_template("根据标题【{title}】，规划一个简短的三段式文章大纲：") | llm | StrOutputParser()
content_chain = PromptTemplate.from_template("根据标题【{title}】和大纲【{outline}】，撰写一篇约300字的正文：") | llm | StrOutputParser()
summary_chain = PromptTemplate.from_template("请提炼以下文章的核心摘要（50字以内）：\n{content}") | llm | StrOutputParser()

long_chain = (
    {"title": title_chain}
    | RunnablePassthrough.assign(outline=outline_chain)
    | RunnablePassthrough.assign(content=content_chain)
    | RunnablePassthrough.assign(summary=summary_chain)
)

print("正在执行长链式文章创作流水线...")
result = long_chain.invoke({"topic": "早起的好处"})

print(f"\n=== 提炼标题 ===\n{result['title']}")
print(f"\n=== 规划大纲 ===\n{result['outline']}")
print(f"\n=== 撰写正文 ===\n{result['content']}")
print(f"\n=== 凝练摘要 ===\n{result['summary']}")
