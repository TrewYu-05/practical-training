from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')

llm = ChatTongyi(model='qwen3-max', dashscope_api_key=api_key)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
])

chain = prompt | llm

chat_history = InMemoryChatMessageHistory()

chain_with_history = RunnableWithMessageHistory(
    chain,
    lambda session_id: chat_history,
    input_messages_key="input",
    history_messages_key="history",
)

print("用户: 我喜欢吃苹果")
result1 = chain_with_history.invoke({"input": "我喜欢吃苹果"}, config={"configurable": {"session_id": "1"}})
print(f"AI: {result1.content}\n{'-' * 20}")

print("用户: 我喜欢吃什么水果")
result2 = chain_with_history.invoke({"input": "我喜欢吃什么水果"}, config={"configurable": {"session_id": "1"}})
print(f"AI: {result2.content}\n{'-' * 20}")

print("内存变量:")
print(chat_history.messages)
