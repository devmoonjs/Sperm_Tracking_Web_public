import streamlit as st
from logo import add_logo
import requests
import json
import os

st.set_page_config(
    page_icon="images/GOQBA_logo.png",
    page_title="ASMIT TEST WEB",
    layout="centered",
)

add_logo()

# Site Header
st.header("Welcome To ASMIT")
st.subheader("Upload your sperm video.")
st.write("- 640*480 size mp4 is recommended.")

uploaded_file = st.file_uploader("파일을 선택해주세요.", type=["mp4"])
SERVER_IP = st.secrets["SERVER_IP"]

if st.button('Start analysis'):
    if uploaded_file is not None:
        with st.spinner('Processing ...'):

            json_data = json.dumps({"file_name" : uploaded_file.name})
            files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
            response = requests.post(f"{SERVER_IP}/upload", files=files)
            response2 = requests.post(f"{SERVER_IP}/run", data=json_data, headers={'Content-Type': 'application/json'})

            file_name_without_extension = os.path.splitext(uploaded_file.name)[0]
            request_file_name = f'{file_name_without_extension}_resultImage.jpg'

            # Flask 서버로 임시 URL 생성 요청 보내기
            response = requests.get(f"{SERVER_IP}/generate_url/{request_file_name}")

        if response.ok:
            # 임시 URL 받기
            temp_url = response.text
            # Streamlit에서 영상 표시
            st.image(temp_url)

        else:
            st.error("영상을 불러오는 데 실패했습니다.")

        if response.ok:
            st.success("Tracking Success")

        else:
            st.error("업로드 실패")


            