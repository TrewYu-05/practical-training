import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
base_url = 'https://dashscope.aliyuncs.com/compatible-mode/v1'

class PersonInfo(BaseModel):
    name: str = Field(description="人员姓名")
    age: int = Field(description="人员年龄")
    skills: list[str] = Field(description="技能列表，如['Python', 'Java']")

llm = ChatOpenAI(model='qwen3-max', openai_api_key=api_key, openai_api_base=base_url)
structured_llm = llm.with_structured_output(PersonInfo)

user_input = "大家好，我叫张三，今年25岁。我大学学的是计算机科学，目前精通Python和Go语言开发，平时也写一些前端代码，熟悉React和Vue框架。"
print(f"输入文本: {user_input}\n")

result = structured_llm.invoke(user_input)
print("结构化提取结果:")
print(result.model_dump_json(indent=2))
