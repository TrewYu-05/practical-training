# Day18b: Ollama开源大模型本地部署与联调

## 环境要求与准备

本指南将指导您如何在本地机器上安装并运行开源的大语言模型框架 Ollama，并拉取指定的模型（例如 `qwen:1.8b`），随后使用 LangChain 进行零成本的离线文本推理调用。

**注意：此部分内容需在本地实际操作执行，不需要在此系统沙盒内运行。**

## 1. 安装 Ollama

请前往 [Ollama 官方网站](https://ollama.com/) 下载适用于您操作系统（Windows/Mac/Linux）的安装包，并按提示完成安装。

## 2. 拉取开源模型

打开终端（Terminal）或命令行工具，输入以下命令拉取并运行模型。Ollama 将自动下载模型权重文件：

```bash
# 拉取 qwen 1.8b 参数模型（或根据需要替换为 qwen:0.5b, llama3 等）
ollama run qwen:1.8b
```
出现 `>>>` 提示符说明模型已成功在本地启动。您可以直接在控制台与其对话测试。输入 `/bye` 退出对话。

## 3. 安装 Python 依赖包

确保您已安装 `langchain-openai` 库（通过 OpenAI 兼容接口调用 Ollama）：

```bash
pip install langchain-openai
```

## 4. 运行联调代码

编写 Python 脚本调用本地部署的 Ollama API，示例代码参考 `main.py`：

```python
# main.py
from langchain_openai import ChatOpenAI

# 1. 实例化 LLM 对象，指向本地 Ollama 的默认服务端口 (通常为 http://localhost:11434/v1)
# 注意：Ollama 提供了与 OpenAI 兼容的 API 接口
local_llm = ChatOpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama", # 对于本地 Ollama，API Key 可填任意值
    model="qwen:1.8b",
    temperature=0.7
)

# 2. 发起请求进行本地推理
question = "你好，请用一句话介绍一下什么是大语言模型？"
print(f"User: {question}")
response = local_llm.invoke(question)

# 3. 输出结果
print(f"Ollama: {response.content}")
```

运行上述代码，如果本地 Ollama 服务正在运行且模型已下载，则会输出大语言模型的推理结果，实现彻底离线、零成本的大模型调用。
