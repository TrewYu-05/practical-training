from langchain_community.embeddings import DashScopeEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')

embed_model = DashScopeEmbeddings(model='text-embedding-v1', dashscope_api_key=api_key)

print("--- 批量转换文本向量 ---")
result3 = embed_model.embed_documents(['人工智能', '机器学习', '西红柿炒鸡蛋', '大模型是如何工作的', 'LLM的原理是什么'])
for i, embedding in enumerate(result3):
    print(f"Text {i+1} embedding preview: {embedding[:5]}... (Length: {len(embedding)})")
