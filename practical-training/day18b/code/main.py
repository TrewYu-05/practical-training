"""
该脚本为本地联调 Ollama 模型的示例代码。
请确保本地已经安装了 Ollama 并在运行中 (例如：ollama run qwen:1.8b)
此脚本不需要在沙盒环境中执行。
"""
from langchain_openai import ChatOpenAI

def main():
    # 初始化 ChatOpenAI 客户端，通过兼容接口连接本地 Ollama 服务
    local_llm = ChatOpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama", # 本地调用不需要真实的 API Key
        model="qwen:1.8b",
        temperature=0.7
    )

    question = "你好，请用通俗的语言解释什么是人工智能？"
    print(f"User: {question}")
    print("Ollama is thinking...")

    try:
        response = local_llm.invoke(question)
        print(f"Ollama: {response.content}")
    except Exception as e:
        print(f"Error connecting to local Ollama service: {e}")
        print("Please ensure Ollama is installed and running ('ollama run qwen:1.8b').")

if __name__ == "__main__":
    main()
