import streamlit as st
import os
import url

st.set_page_config(
    page_title="whisperNoter",  # 页面标题
    page_icon=":rainbow:",  # icon
    # layout="wide",  # 页面布局
    # initial_sidebar_state="auto"  #侧边栏
)

st.markdown("# whisperNoter")

uploaded_file = st.file_uploader("选择音频文件", type="mp3", )

# 保存文件
if uploaded_file is not None:
    if uploaded_file.name.strip():
        file_path = os.path.join("uploads", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"已保存文件: {file_path}")
        url.voice2txt(file_path)
    else:
        st.error("上传失败")

    with open("./data/test.txt", "r", encoding="utf-8") as file:
        txt = file.read()
    st.caption("识别文字：")
    st.text(txt)

    st.caption("正在转换为笔记:hourglass:")
    st.markdown(url.txt2title(txt))
