import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')

print("=== 专业领域大模型语料知识库研发 ===")

# 1. 载入语料目录
current_dir = os.path.dirname(__file__)
loader = DirectoryLoader(current_dir, glob="**/*.txt", loader_cls=TextLoader, loader_kwargs={'encoding': 'utf-8'})
docs = loader.load()

print(f"成功加载 {len(docs)} 个语料文件。")
for d in docs:
    print(f" - {os.path.basename(d.metadata['source'])}")

# 2. 文本清洗与分割
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50,
    separators=["\n\n", "\n", "。", "！", "？", " ", ""]
)
split_docs = text_splitter.split_documents(docs)
print(f"\n文档已清洗并切分为 {len(split_docs)} 个标准语义块 (Chunks)。")

# 3. 向量化并注入 Chroma 数据库
db_path = os.path.join(current_dir, "domain_knowledge_db")
embeddings = DashScopeEmbeddings(model='text-embedding-v1', dashscope_api_key=api_key)

print("\n正在调用大模型将文本转化为高维向量，并注入本地向量数据库...")
vectorstore = Chroma.from_documents(documents=split_docs, embedding=embeddings, persist_directory=db_path)
print(f"知识库构建完成！已成功持久化到: {db_path}")

# 4. 检索测试
query = "智能手表续航短或者无法开机怎么处理？"
print(f"\n--- 检索测试 ---")
print(f"模拟工单问题: {query}")
search_results = vectorstore.similarity_search(query, k=2)

print("检索到的相关知识库条款:")
for i, res in enumerate(search_results, 1):
    source = os.path.basename(res.metadata['source'])
    print(f"[{i}] (来源: {source}): {res.page_content[:150]}...")
