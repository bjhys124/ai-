import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="centered")
st.title("🌟 GET3D 데모 뷰어")

st.markdown("아래는 예제 3D 모델입니다 (teapot.glb from HuggingFace)")

components.iframe("/static/3dviewer.html", height=500)

