from langchain_community.document_loaders import TextLoader, WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1. TextLoader
text_content = """人工智能（Artificial Intelligence, AI）是指由人制造出来的机器所表现出来的智能。
通常，人工智能是指通过普通计算机程序来呈现人类智能的技术。
该词也指出研究这样的智能系统是否能够实现，以及如何实现。
人工智能的应用领域包括机器人、语言识别、图像识别、自然语言处理和专家系统等。
随着深度学习和大数据技术的发展，AI在医疗、自动驾驶、金融分析等诸多领域取得了突破性进展。"""

with open("sample.txt", "w", encoding="utf-8") as f:
    f.write(text_content)

loader = TextLoader("sample.txt", encoding="utf-8")
docs = loader.load()
print(f"Loaded {len(docs)} document from TextLoader. Content length: {len(docs[0].page_content)}")

# 2. WebBaseLoader
web_loader = WebBaseLoader("https://example.com")
web_docs = web_loader.load()
print(f"Loaded {len(web_docs)} document from WebBaseLoader. Title: {web_docs[0].metadata.get('title')}")

# 3. Text Splitting
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False,
)

split_docs = text_splitter.split_documents(docs)
print(f"\nOriginal document split into {len(split_docs)} chunks.")
for i, chunk in enumerate(split_docs):
    print(f"Chunk {i+1}: {chunk.page_content} (Length: {len(chunk.page_content)})")
