import streamlit as st

st.set_page_config(page_title="RAG + YOLO 中控导航", layout="wide", initial_sidebar_state="expanded")

# 侧边栏导航
st.sidebar.title("RAG + YOLO 系统导航")
page = st.sidebar.radio("请选择功能模块：", ["欢迎", "个人", "联系"])

if page == "欢迎":
    st.title("欢迎来到 RAG + YOLO 融合系统 🚀")
    st.markdown("""
    这是一个前沿的交叉领域深度开发控制台，结合了 **检索增强生成 (RAG)** 技术与 **计算机视觉 (YOLO 目标检测)** 技术。

    ### 业务目标：
    本系统旨在打造一个智能化的中控中台：
    - **YOLO 模块**：实时处理视频流或图片，检测目标物体并提取视觉特征和结构化数据。
    - **RAG 模块**：利用大模型和向量数据库，根据 YOLO 提取的物体信息和环境上下文，进行知识库检索，从而实现“看见并理解”的视觉交互问答系统。

    ### 当前状态：
    请通过左侧边栏导航到各个模块进行配置与体验。
    """)
    st.info("架构就绪，等待后端视觉推理集群和 ChromaDB 向量节点接入。")

elif page == "个人":
    st.title("个人工作台 💻")
    st.write("在这里管理您的 RAG 知识库及 YOLO 模型配置。")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📚 RAG 知识库管理")
        st.file_uploader("上传新的领域语料 (支持 PDF/TXT/CSV)", type=["pdf", "txt", "csv"])
        st.button("向量化并入库")
        st.success("当前知识库总量：128 篇文档片段。")

    with col2:
        st.subheader("👁️ YOLO 视觉模型配置")
        st.selectbox("选择目标检测模型", ["YOLOv8-Nano", "YOLOv8-Small", "YOLOv10-Base"])
        st.slider("检测置信度阈值 (Confidence)", 0.0, 1.0, 0.5)
        st.button("启动视觉推理引擎")
        st.warning("视觉节点当前处于离线状态，请配置 GPU 资源。")

elif page == "联系":
    st.title("联系与支持 📞")
    st.write("遇到问题或需要部署支持？")
    st.markdown("""
    - **技术支持邮箱**: support@rag-yolo-ai.com
    - **系统开发文档**: [查看内网文档](https://github.com/langchain-ai)
    - **在线客服**: 系统已接入 AI 客服，您可以在下方直接提问。
    """)
    user_q = st.chat_input("向系统支持助手提问...")
    if user_q:
        st.chat_message("user").write(user_q)
        st.chat_message("ai").write("由于系统正在维护，AI 支持助手暂时下线，请发送邮件联系我们。")
