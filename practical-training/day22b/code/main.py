import os
import subprocess
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

from langchain.agents import create_agent

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')
base_url = 'https://dashscope.aliyuncs.com/compatible-mode/v1'

llm = ChatOpenAI(model='qwen-max', api_key=api_key, base_url=base_url)

@tool
def local_shell_backend(command: str) -> str:
    """如果需要查询系统时间、目录结构、或者运行简单本地脚本来辅助分析数据，调用此命令。在Windows/Mac/Linux上执行命令。"""
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"命令执行失败: {e.stderr}"

tools = [local_shell_backend]

system_prompt = """你是一个多功能AI助手/顶级情感与职场深度解析咨询师。
你需要针对复杂的“情感解析类”或职场疑问，产出带有：
1. 深度破局（直击问题痛点）
2. 步骤拆分（如何一步步解决）
3. 语气模拟（贴心且犀利的长篇干货分析文案）

如有必要，你可以调用 local_shell_backend 获取一些辅助信息（如当前日期辅助计算时间差等），并将思维链推演的过程清晰展现出来。
"""

agent_executor = create_agent(llm, tools)

def main():
    print("================ Deep Agent 推理启动 ================")
    user_query = "我最近换了新工作，感觉同事很冷漠，领导每天让我做边缘打杂工作，感觉被排挤。我每天很内耗，不知道该不该辞职。请帮我深度解析并破局。"
    print(f"用户提问：{user_query}\n")

    result = agent_executor.invoke({
        "messages": [
            ("system", system_prompt),
            ("user", user_query)
        ]
    })

    print("\n================ Agent 最终输出 ================\n")
    print(result["messages"][-1].content)

if __name__ == "__main__":
    main()