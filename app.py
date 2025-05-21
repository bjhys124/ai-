import streamlit as st
import requests
from PIL import Image
import io

# 서버 URL (로컬 GPU 서버의 public IP 또는 ngrok URL 사용)
FASTAPI_URL = "http://110.11.235.106:9999/generate_3d"

st.set_page_config(page_title="AI 성형 3D 시뮬레이터", layout="centered")

st.title("📸 얼굴 업로드로 3D 성형 시뮬레이션")
st.write("정면 얼굴 사진을 업로드하면 AI가 3D 얼굴 모델을 생성합니다.")

uploaded_file = st.file_uploader("정면 얼굴 사진 업로드 (JPG, PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="업로드한 이미지", use_column_width=True)

    if st.button("3D 얼굴 생성 요청"):
        with st.spinner("AI가 3D 얼굴을 생성 중입니다..."):
            # 파일 전송
            files = {"file": uploaded_file.getvalue()}
            try:
                response = requests.post(FASTAPI_URL, files=files)
                if response.status_code == 200:
                    result_image = Image.open(io.BytesIO(response.content))
                    st.success("✅ 3D 얼굴 생성 완료!")
                    st.image(result_image, caption="3D 얼굴 이미지", use_column_width=True)
                else:
                    st.error(f"서버 오류 발생: {response.status_code}")
            except Exception as e:
                st.error(f"연결 실패: {e}")
