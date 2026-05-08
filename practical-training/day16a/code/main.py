import os
from openai import OpenAI
from dotenv import load_dotenv
from common import get_llm_response
import streamlit as st

load_dotenv()
default_api_key = os.getenv('OPENAI_API_KEY', '')

def get_answer(question: str, base_url, api_key, model_name):
    client = OpenAI(base_url=base_url, api_key=api_key)
    stream = get_llm_response(client, model=model_name, user_prompt=question, stream=True)
    for chunk in stream:
        yield chunk.choices[0].delta.content or ''

with st.sidebar:
    api_vendor = st.radio(label='请选择模型服务器商', options=['ChatTongyi', 'DeepSeek'])
    if api_vendor == 'ChatTongyi':
        base_url = 'https://dashscope.aliyuncs.com/compatible-mode/v1'
        model_options = ['qwen-plus', 'qwen-max', 'qwen-turbo', 'qwen3-max']
    elif api_vendor == 'DeepSeek':
        base_url = 'https://api.deepseek.com'
        model_options = ['deepseek-chat', 'deepseek-reasoner']

    model_name = st.selectbox(label='请选择你要使用的模型', options=model_options)
    api_key = st.text_input(label='请输入你的key:', type='password', value=default_api_key)

if 'messages' not in st.session_state:
    st.session_state['messages'] = [('ai', '你好，我是你的个人小助理，我叫小美')]

st.write('## 我的个人聊天机器人')
st.divider()

if not api_key:
    st.error('请提供你的大模型的api_key')
    st.stop()

for role, content in st.session_state['messages']:
    st.chat_message(role).write(content)

user_input = st.chat_input(placeholder='请输入')
if user_input:
    _, history = st.session_state['messages'][-1]
    st.chat_message('human').write(user_input)
    st.session_state['messages'].append(('human', user_input))

    with st.spinner('思考中...'):
        answer = get_answer(f'{history}, {user_input}', base_url, api_key, model_name)
        result = st.chat_message('ai').write_stream(answer)
        st.session_state['messages'].append(('ai', result))
