import streamlit as st

st.set_page_config(page_title="Streamlit带状态的多页面跳转架构", layout="wide")

st.title("首页: Streamlit状态与跳转架构")

# 分列布局
st.header("1. 分列布局演示")
col1, col2, col3 = st.columns(3)
with col1:
    st.write('这是第一列')
with col2:
    st.write('这是第二列')
with col3:
    st.write('这是第三列')

st.divider()
col1, col2, col3 = st.columns(3)
with col1:
    st.text_input('请输入你的用户名')
with col2:
    st.text_area('请输入自我介绍')
with col3:
    st.text_input('请输入密码', type='password')

st.divider()
# 选项卡
st.header("2. 选项卡演示")
tab1, tab2, tab3 = st.tabs(['姓名', '联系方式', '你的兴趣爱好'])
with tab1:
    name = st.text_input(label='姓名', placeholder='请输入你的姓名:')
    if name:
        st.write(f'欢迎：{name}')
with tab2:
    contact = st.selectbox('你希望我们通过什么方式来联系你', ['电话', '邮件', '微信'])
    st.write(f'好的，我们会通过{contact}方式来联系你')
with tab3:
    likes = st.multiselect('你的兴趣是什么？', ['篮球', 'rap', '唱跳'])
    for it in likes:
        st.write(it)

st.divider()
# 数据持久化
st.header("3. 数据持久化演示 (st.session_state)")
if 'a' not in st.session_state:
    st.session_state['a'] = 0

click_btn = st.button('加1')
if click_btn:
    st.session_state['a'] += 1
st.write(f"当前数值: {st.session_state['a']}")

st.divider()
st.header("4. 页面跳转演示")
st.page_link("pages/02_about.py", label="跳转到关于页面", icon="🏠")
