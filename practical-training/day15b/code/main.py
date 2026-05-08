import json
import os
from openai import OpenAI
from dotenv import load_dotenv
from common import get_llm_response
import streamlit as st

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(base_url='https://dashscope.aliyuncs.com/compatible-mode/v1', api_key=api_key)

demo = [
    {'role': 'user', 'content': '换电池报价8万2！二手车商都不敢收，所谓终身质保条款藏着无数套路，新能源韭菜真不是白叫的。'},
    {'role': 'assistant', 'content': '负面'},
    {'role': 'user', 'content': '驾乘体验非常舒服，增程式没有续航焦虑，月均油电费才300块，国产新能源神车当之无愧。'},
    {'role': 'assistant', 'content': '正面'},
    {'role': 'user', 'content': '驾驶质感不错，但车机逻辑混乱需要适应，价格是否合理建议先试驾后再评判，仁者见仁智者见智。'},
    {'role': 'assistant', 'content': '中性'}
]

st.write('## 用户情感分析助手')

result = ''
col1, col2 = st.columns([3, 1])
with col1:
    comment = st.text_area(label='请输入用户评价', height=120)
    button = st.button('确定', type='primary')
    if button and comment.strip():
        with st.spinner("分析中..."):
            result = get_llm_response(
                client,
                system_prompt='你是专业的用户评论情感分析助手，你需要回答：正面、负面或者中性。不要给出其他的解释',
                few_shot_prompt=json.dumps(demo),
                user_prompt=comment.strip()
            )
with col2:
    if result:
        st.write(f'> 分析结果：**{result}**')
