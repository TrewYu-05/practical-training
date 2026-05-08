import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
base_url = 'https://dashscope.aliyuncs.com/compatible-mode/v1'

llm = ChatOpenAI(model='qwen3-max', openai_api_key=api_key, openai_api_base=base_url)

# Define the state graph and nodes
def call_model(state: MessagesState):
    response = llm.invoke(state["messages"])
    return {"messages": response}

workflow = StateGraph(state_schema=MessagesState)
workflow.add_node("model", call_model)
workflow.add_edge(START, "model")

memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

print("--- 线程1：张三的对话 ---")
config1 = {"configurable": {"thread_id": "zhangsan_thread"}}
query1 = "你好，我叫张三，我最喜欢的颜色是蓝色。"
print(f"张三: {query1}")
input_messages = [HumanMessage(content=query1)]
output = app.invoke({"messages": input_messages}, config1)
print(f"AI: {output['messages'][-1].content}\n")

print("--- 线程2：李四的对话 ---")
config2 = {"configurable": {"thread_id": "lisi_thread"}}
query2 = "你好，我是李四，我想知道去北京旅游穿什么？"
print(f"李四: {query2}")
input_messages = [HumanMessage(content=query2)]
output = app.invoke({"messages": input_messages}, config2)
print(f"AI: {output['messages'][-1].content}\n")

print("--- 线程1：张三的二次对话 (测试隔离记忆) ---")
query3 = "你能记住我叫什么名字，以及我喜欢的颜色吗？"
print(f"张三: {query3}")
input_messages = [HumanMessage(content=query3)]
output = app.invoke({"messages": input_messages}, config1)
print(f"AI: {output['messages'][-1].content}")
