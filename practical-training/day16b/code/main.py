import os
from openai import OpenAI
from dotenv import load_dotenv
from common import fetch_page, get_llm_response
import streamlit as st

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

user_prompt_template = '''
你是一个根据网页标题和内容生成摘要的优秀助手，请你根据我提供的标题和内容生成markdown格式的网页摘要。
注意：摘要中不要包含```markdown和```标签，将内容控制在1000个字符以内，尽可能用列表的形式呈现内容。
### 输出格式 ###
```markdown
## <标题>
### <第一部分>t
- <内容1>
- <内容2>
- <内容3>
### <第二部分>
- <内容1>
- <内容2>
- <内容3>
### ...
### 总结
<总结内容>
```
### 网页标题和内容如下所示 ###
网页标题：{0}
主体内容：{1}
'''

def generate_summary(url):
    client = OpenAI(base_url='https://dashscope.aliyuncs.com/compatible-mode/v1', api_key=api_key)
    web_title, web_body = fetch_page(url)
    user_prompt = user_prompt_template.format(web_title, web_body)
    stream = get_llm_response(client, user_prompt=user_prompt, stream=True)
    for chunk in stream:
        yield chunk.choices[0].delta.content or ''

st.write('## 网页摘要生成助手')
st.divider()

result = ''
col1, _, col2 = st.columns([3, 1, 6])
with col1:
    url_input = st.text_input(label='要生成摘要网址', placeholder='请输入完整的网址')
    button = st.button('确定', type='primary')

if button and url_input.strip():
    result = generate_summary(url_input)

with col2:
    if result:
        st.write('网页摘要:')
        st.write_stream(result)
