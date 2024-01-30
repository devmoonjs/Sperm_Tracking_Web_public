import streamlit as st

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://github.com/devmoonjs/git-practice/blob/main/GOQBA_logo.png?raw=true);
                background-repeat: no-repeat;
                background-size: 80%;
                padding-top: 30px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                # content: "ASMIT";
                margin-left: 20px;
                margin-top: px;
                font-size: 30px;
                # font-weight: bold;
                position: relative;
                top: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )