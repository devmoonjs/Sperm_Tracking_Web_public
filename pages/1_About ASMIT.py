import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 
from time import sleep
from pathlib import Path
from logo import add_logo

img = "images/SpermTracking.png"
img2 = "images/ExampleTracking.png"

st.set_page_config(
    page_icon="images/Logo.png",
    page_title="Sperm Trackin AI",
    layout="centered",
)

add_logo()
st.title("AI Sperm Motility Analysis Tool")


st.write("""
## AI-Powered Sperm Analysis

Our cutting-edge artificial intelligence system is expertly designed for the detailed tracking and analysis of sperm motility as observed through a microscope. This innovative tool is a crucial ally in the diagnosis of male infertility, offering a deep insight into the dynamics and vigor of individual sperm activity.
""")

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image(img2, caption="Sperm tracking result", width=350)

st.write("""
### Key Features:
- **Precision Tracking**: Utilizes advanced algorithms to accurately trace sperm movement.
- **Detailed Analysis**: Provides comprehensive insights into sperm motility and behavior.
- **User-Friendly Interface**: Easy to navigate for both professionals and individuals.
- **Confidential and Secure**: Ensures the utmost privacy and security of user data.

Embracing the power of AI, our system opens new doors to understanding male reproductive health, offering a reliable, non-invasive method for assessing sperm functionality. Whether you are a healthcare professional or an individual seeking insights into personal health, our AI tool provides invaluable support in the journey towards understanding and managing male fertility.
""")

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image(img, width=350, caption="Sperm motility type")