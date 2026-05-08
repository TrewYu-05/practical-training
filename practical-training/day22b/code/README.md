# Day22b: Deep Agent与本地技能（Skills）深度推理智能体

## 项目介绍

本项目旨在演示如何利用高级 `deep_agent` 并配置强大的 `LocalShellBackend`（本地 Shell 执行权限），从而允许大模型在本地计算机上执行命令行脚本、进行复杂的检索计算、或通过“思维链”（Chain of Thought）进行拆分推理，最终给用户产出深度、长篇的分析文案。

**⚠️ 警告：该代码涉及授予 AI 直接操作本地 Shell (终端) 的能力。为了安全起见，请仅在您完全控制的、安全的开发机或虚拟机环境中运行此代码！不要在系统沙盒中直接运行！**

## 环境准备

1. 确保已安装所需的依赖库（请在您本地执行）：
   ```bash
   pip install langchain langchain-openai python-dotenv
   ```
2. 需要配置环境变量 `.env`，填入您的 API Key：
   ```env
   OPENAI_API_KEY="sk-xxxxxxxxxxx"
   DASHSCOPE_API_KEY="sk-xxxxxxxxxxx"
   ```

## 代码实现逻辑

在实际业务开发中，`LocalShellBackend` 或 `BashTool` 是通过给 Agent 绑定执行终端命令的工具来实现的。
以下是一个概念性的实现步骤：

1. **载入环境变量与模型**: 初始化 Ali DashScope 的 `ChatOpenAI` 接口。
2. **定义 Tools (Skills)**: 定义一个能执行本地 Bash/Shell 命令的工具（利用 LangChain 的 `@tool` 装饰器或直接使用原生的 `ShellTool`）。
3. **编写深度破局 Prompt**: 赋予 Agent "资深咨询师/深度破局专家" 角色，要求其：
   - 拆分用户问题（步骤拆分）。
   - 针对复杂的情感或技术难题进行思维链（CoT）推演。
   - 在必要时调用本地执行脚本去查询数据（模拟）。
   - 输出语气模拟、长篇干货分析文案。
4. **组装 AgentExecutor 并执行**: 将模型、提示词、Shell工具组装并开始推理。

## 运行方式

请在您的**本地安全环境**中运行 `main.py` 文件：

```bash
python main.py
```
模型将会在终端输出大段的深度分析文字及思维链步骤。
