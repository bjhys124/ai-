# 1. app.py - Streamlit 메인 앱
import streamlit as st
import os
import time
import streamlit.components.v1 as components
from get3d_runner import generate_3d_model

st.set_page_config(layout="wide")
st.title("📷 GET3D 기반 AI 성형 시뮬레이터")

uploaded_file = st.file_uploader("정면 얼굴 사진을 업로드하세요", type=["jpg", "jpeg", "png"])

if uploaded_file:
    filename = "input.jpg"
    with open(filename, "wb") as f:
        f.write(uploaded_file.read())
    st.image(filename, caption="업로드된 사진", use_column_width=True)

    if st.button("3D 얼굴 생성하기"):
        with st.spinner("3D 얼굴 생성 중... (최대 수십 초) "):
            generate_3d_model()  # face.glb 생성
            time.sleep(2)  # 렌더링 준비 시간 (optional)

        st.success("3D 얼굴 생성 완료 ✅")

        # 렌더링 표시
        st.markdown("### 🧠 실시간 3D 얼굴 확인 (터치 회전 가능)")
        components.iframe("/static/3dviewer.html", height=500)
