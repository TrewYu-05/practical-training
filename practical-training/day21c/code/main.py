import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.tools import tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
dashscope_key = os.getenv('DASHSCOPE_API_KEY')
base_url = 'https://dashscope.aliyuncs.com/compatible-mode/v1'

llm = ChatOpenAI(model='qwen3-max', openai_api_key=api_key, openai_api_base=base_url)

# 1. 载入极长篇幅的《颐和园.txt》建立知识库
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
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个智能导游系统。遇到景区（尤其是颐和园）具体问题时，请必须调用工具 summer_palace_guide。如果查不到或超出范围，依托你本身的知识回答或者承认不知道。"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 4. 提问测试
print("--- 智能体问答测试 ---")
q1 = "长廊上有什么特别的画吗？"
print(f"用户提问: {q1}")
res1 = agent_executor.invoke({"input": q1})
print(f"Agent回答: {res1['output']}\n")

q2 = "颐和园的开放时间是几点？（假设文本里没有）"
print(f"用户提问: {q2}")
res2 = agent_executor.invoke({"input": q2})
print(f"Agent回答: {res2['output']}\n")
