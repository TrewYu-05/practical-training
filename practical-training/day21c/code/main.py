import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.tools import tool

# 1. 引入最新的稳定版 Agent 创建方法
from langchain.agents import create_agent

# 载入环境变量
load_dotenv()
# 统一使用千问的 API Key
dashscope_key = os.getenv('DASHSCOPE_API_KEY')
base_url = 'https://dashscope.aliyuncs.com/compatible-mode/v1'

# 更新为推荐的参数名 api_key 和 base_url，避免 pydantic 警告
llm = ChatOpenAI(model='qwen-max', api_key=dashscope_key, base_url=base_url)

# --- 知识库构建部分保持不变 ---
# 注意：运行前请确保当前目录下有《颐和园.txt》文件
txt_path = os.path.join(os.path.dirname(__file__), "颐和园.txt")
loader = TextLoader(txt_path, encoding="utf-8")
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)
split_docs = text_splitter.split_documents(docs)

embeddings = DashScopeEmbeddings(model='text-embedding-v1', dashscope_api_key=dashscope_key)
vectorstore = Chroma.from_documents(documents=split_docs, embedding=embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})


# 2. 封装自定义检索工具
@tool
def summer_palace_guide(query: str) -> str:
    """如果用户问到任何关于颐和园景区具体的问题（如景点介绍、历史、路线），必须调用这个工具来查找内部知识库。"""
    docs = retriever.invoke(query)
    if docs:
        return "\n".join([d.page_content for d in docs])
    return "没有在颐和园的知识库中找到相关信息。"

tools = [summer_palace_guide]


# 3. 创建指导智能体 Agent
# 放弃使用复杂的 ChatPromptTemplate，直接定义纯文本 System Prompt
system_prompt = "你是一个智能导游系统。遇到景区（尤其是颐和园）具体问题时，请必须调用工具 summer_palace_guide。如果查不到或超出范围，依托你本身的知识回答或者承认不知道。"

# 直接使用 create_agent，底层通过图结构稳定调用工具
agent_executor = create_agent(llm, tools)


# 4. 提问测试
def main():
    print("--- 智能体问答测试 ---")
    
    q1 = "长廊上有什么特别的画吗？"
    print(f"用户提问: {q1}")
    # 通过 messages 列表传入系统设定和用户问题
    res1 = agent_executor.invoke({
        "messages": [
            ("system", system_prompt),
            ("user", q1)
        ]
    })
    print(f"Agent回答: {res1['messages'][-1].content}\n")

    q2 = "颐和园的开放时间是几点？（假设文本里没有）"
    print(f"用户提问: {q2}")
    res2 = agent_executor.invoke({
        "messages": [
            ("system", system_prompt),
            ("user", q2)
        ]
    })
    print(f"Agent回答: {res2['messages'][-1].content}\n")

if __name__ == "__main__":
    main()