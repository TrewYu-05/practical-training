"""
该脚本为高级 Agent 的本地 Shell 执行及深层推理示例。
出于系统安全限制，此脚本推荐在本地安全环境中运行。
"""
import os
import subprocess
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# 载入环境变量
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
base_url = 'https://dashscope.aliyuncs.com/compatible-mode/v1'

llm = ChatOpenAI(model='qwen3-max', openai_api_key=api_key, openai_api_base=base_url)

# 定义本地 Shell 执行的技能 (Skill)
@tool
def local_shell_backend(command: str) -> str:
    """如果需要查询系统时间、目录结构、或者运行简单本地脚本来辅助分析数据，调用此命令。在Mac/Linux上执行Bash命令。"""
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"命令执行失败: {e.stderr}"

tools = [local_shell_backend]

# 设定带思维链深度推理的长篇 Prompt
system_prompt = """你是一个多功能AI助手/顶级情感与职场深度解析咨询师。
你需要针对复杂的“情感解析类”或职场疑问，产出带有：
1. 深度破局（直击问题痛点）
2. 步骤拆分（如何一步步解决）
3. 语气模拟（贴心且犀利的长篇干货分析文案）

如有必要，你可以调用 local_shell_backend 获取一些辅助信息（如当前日期辅助计算时间差等），并将思维链推演的过程清晰展现出来。
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

def main():
    print("================ Deep Agent 推理启动 ================")
    user_query = "我最近换了新工作，感觉同事很冷漠，领导每天让我做边缘打杂工作，感觉被排挤。我每天很内耗，不知道该不该辞职。请帮我深度解析并破局。"
    print(f"用户提问：{user_query}\n")

    # 启动Agent推理
    result = agent_executor.invoke({"input": user_query})

    print("\n================ Agent 最终输出 ================\n")
    print(result['output'])

if __name__ == "__main__":
    main()
