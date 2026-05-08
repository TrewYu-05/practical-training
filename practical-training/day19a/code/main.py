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

# Chain 1: Generate Title
title_prompt = PromptTemplate.from_template("请为一个关于【{topic}】的童话故事想一个吸引人的标题，只输出标题内容：")
title_chain = title_prompt | llm | StrOutputParser()

# Chain 2: Generate Story
story_prompt = PromptTemplate.from_template("你是一个童话作家。请根据标题【{title}】写一个大约200字的简短童话故事：")
story_chain = story_prompt | llm | StrOutputParser()

# Chain 3: Extract Moral
moral_prompt = PromptTemplate.from_template("请用一句话总结下面这个童话故事的核心寓意：\n\n{story}")
moral_chain = moral_prompt | llm | StrOutputParser()

# Constructing Sequential Chain (using LCEL to pass variables)
print("开始生成故事流水线...")

sequential_chain = (
    {"title": title_chain}
    | RunnablePassthrough.assign(story=story_chain)
    | RunnablePassthrough.assign(moral=moral_chain)
)

result = sequential_chain.invoke({"topic": "一只想飞翔的小猪"})

print(f"\n【故事标题】: {result['title']}")
print(f"\n【故事正文】:\n{result['story']}")
print(f"\n【核心寓意】: {result['moral']}")
