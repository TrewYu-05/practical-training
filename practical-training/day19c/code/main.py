import os
import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
base_url = 'https://dashscope.aliyuncs.com/compatible-mode/v1'

llm = ChatOpenAI(model='qwen3-max', openai_api_key=api_key, openai_api_base=base_url)

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个拥有记忆的助手。"),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
])

chain = prompt | llm

# Simple JSON based memory implementation mimicking FileChatMessageHistory
class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self, file_path: str):
        self.file_path = file_path
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump([], f)

    @property
    def messages(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        msgs = []
        for item in data:
            if item['type'] == 'human':
                msgs.append(HumanMessage(content=item['content']))
            elif item['type'] == 'ai':
                msgs.append(AIMessage(content=item['content']))
        return msgs

    def add_messages(self, messages):
        current_messages = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding='utf-8') as f:
                current_messages = json.load(f)

        for msg in messages:
            if isinstance(msg, HumanMessage):
                current_messages.append({'type': 'human', 'content': msg.content})
            elif isinstance(msg, AIMessage):
                current_messages.append({'type': 'ai', 'content': msg.content})

        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(current_messages, f, ensure_ascii=False, indent=2)

    def clear(self):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump([], f)

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        file_path = os.path.join(os.path.dirname(__file__), f"{session_id}.json")
        store[session_id] = FileChatMessageHistory(file_path)
    return store[session_id]

chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

print("--- 第一轮对话 ---")
print("User: 我的名字叫李雷，我喜欢打篮球。")
resp1 = chain_with_history.invoke(
    {"input": "我的名字叫李雷，我喜欢打篮球。"},
    config={"configurable": {"session_id": "session_lilei"}}
)
print(f"AI: {resp1.content}")

print("\n--- 第二轮对话 ---")
print("User: 请问我叫什么名字，我喜欢干什么？")
resp2 = chain_with_history.invoke(
    {"input": "请问我叫什么名字，我喜欢干什么？"},
    config={"configurable": {"session_id": "session_lilei"}}
)
print(f"AI: {resp2.content}")

print("\n检查离线持久化 JSON 记录:")
with open("practical-training/day19c/code/session_lilei.json", "r") as f:
    print(f.read())
