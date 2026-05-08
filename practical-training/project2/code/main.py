import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
base_url = 'https://dashscope.aliyuncs.com/compatible-mode/v1'

st.set_page_config(page_title="AI智能简历助手", layout="centered")

st.title("AI智能简历助手 📄")
st.write("根据您的基本信息和简短的实习经历，AI将自动使用STAR法则扩写为您生成专业求职简历！")

name = st.text_input("姓名", "张三")
education = st.text_input("教育背景及专业", "北京大学 数据科学与大数据技术专业")
intern_desc = st.text_area("极其简短的实习经历口语描述", "上个月去互联网公司实习了，主要帮他们整理Excel表格，有时候爬一些网站的数据，最后写了个Python脚本自动处理，帮大家省了挺多时间。")

sys_prompt = """你是一个专业的AI简历优化专家。
请根据用户提供的基本信息、教育背景以及口语化的简短实习经历，使用STAR法则（情境 Situation、任务 Task、行动 Action、成果 Result）对实习经历进行专业化、书面化的扩写，并量化其中的指标。
最后输出一份结构清晰、排版美观的Markdown格式求职简历。"""

if st.button("一键生成简历", type="primary"):
    client = OpenAI(api_key=api_key, base_url=base_url)
    user_prompt = f"姓名：{name}\n教育背景：{education}\n实习经历描述：{intern_desc}"

    with st.spinner("AI正在思考和优化您的简历..."):
        response = client.chat.completions.create(
            model='qwen3-max',
            messages=[
                {'role': 'system', 'content': sys_prompt},
                {'role': 'user', 'content': user_prompt}
            ]
        )
        result = response.choices[0].message.content
        st.session_state['resume_markdown'] = result

if 'resume_markdown' in st.session_state:
    st.markdown("### 生成的专业简历：")
    st.markdown(st.session_state['resume_markdown'])

    st.download_button(
        label="下载简历 (Markdown)",
        data=st.session_state['resume_markdown'],
        file_name=f"{name}_resume.md",
        mime="text/markdown"
    )
