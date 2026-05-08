import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')

# Create sample knowledge base
knowledge_text = """如何办理退款？
如果商品满足7天无理由退货规则，请在订单页面点击申请退款。

配送费怎么计算？
普通商品订单满99元免邮，不满99元收10元配送费。

商品保修期多久？
所有电子产品享有1年国家法定保修。"""

with open("kb.txt", "w", encoding="utf-8") as f:
    f.write(knowledge_text)

loader = TextLoader("kb.txt", encoding="utf-8")
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=10)
split_docs = text_splitter.split_documents(docs)

embeddings = DashScopeEmbeddings(model='text-embedding-v1', dashscope_api_key=api_key)

# Initialize Chroma vector store
db_path = os.path.join(os.path.dirname(__file__), "chroma_db")
vectorstore = Chroma.from_documents(documents=split_docs, embedding=embeddings, persist_directory=db_path)

print("Vectors stored in ChromaDB.")

# Similarity Search
query = "运费是怎么收的？"
print(f"\n用户提问: {query}")

docs = vectorstore.similarity_search(query, k=1)
if docs:
    print(f"最匹配的解答块: {docs[0].page_content}")
