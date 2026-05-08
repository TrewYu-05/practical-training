import os
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
base_url = 'https://dashscope.aliyuncs.com/compatible-mode/v1'

st.set_page_config(page_title="多功能生成助手", layout="wide")

llm = ChatOpenAI(model='qwen3-max', openai_api_key=api_key, openai_api_base=base_url)

tab1, tab2 = st.tabs(["文章生成器", "多国语言翻译助手"])

with tab1:
    st.header("科普文生成器")
    target = st.selectbox("受众群体", ["小学生", "大学生", "专业研究员"])
    word_count = st.slider("字数控制", 100, 1000, 300, 100)
    topic = st.text_input("主题", "黑洞是怎么形成的？")

    if st.button("生成科普文", key="btn1"):
        prompt = PromptTemplate.from_template(
            "你是一个科普作家。请针对【{target}】写一篇关于【{topic}】的科普文章。字数控制在约{word_count}字。语言风格要符合受众特征。"
        )
        chain = prompt | llm | StrOutputParser()
        with st.spinner("生成中..."):
            result = chain.invoke({"target": target, "word_count": word_count, "topic": topic})
        st.write(result)

with tab2:
    st.header("多国语言翻译助手")
    target_lang = st.selectbox("目标语言", ["英语", "日语", "法语", "俄语"])
    text_to_translate = st.text_area("需要翻译的文本")

    if st.button("开始翻译", key="btn2"):
        prompt = PromptTemplate.from_template("请将以下文本翻译为【{target_lang}】：\n{text}")
        chain = prompt | llm | StrOutputParser()
        with st.spinner("翻译中..."):
            result = chain.invoke({"target_lang": target_lang, "text": text_to_translate})
        st.write(result)
