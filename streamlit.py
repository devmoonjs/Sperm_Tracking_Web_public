import streamlit as st
from logo import add_logo
import requests
import json

st.set_page_config(
    page_icon="images/GOQBA_logo.png",
    page_title="ASMIT TEST WEB",
    layout="wide",
)

add_logo()

# Site Header
st.header("Welcome To ASMIT")
st.subheader("Upload your sperm video.")
st.write("- 640*480 size mp4 is recommended.")

uploaded_file = st.file_uploader("파일을 선택해주세요.", type=["mp4"])

if st.button('영상 업로드'):
    if uploaded_file is not None:
        json_data = json.dumps({"file_name" : uploaded_file.name})
        files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
        response = requests.post("http://127.0.0.1:5001/upload", files=files)
        response2 = requests.post("http://127.0.0.1:5001/run", data=json_data, headers={'Content-Type': 'application/json'})

        if response.ok:
            st.success("영상이 성공적으로 업로드되었습니다.")
        else:
            st.error("업로드 실패")


            