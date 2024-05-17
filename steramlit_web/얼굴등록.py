import streamlit as st
from PIL import Image

import numpy as np
import pandas as pd
import re
import json

# Setting page layout
st.set_page_config(
    page_title="vichart",  # Setting page title
    page_icon="🤖",     # Setting page icon
    layout="wide",      # Setting layout to wide
    initial_sidebar_state="expanded"    # Expanding sidebar by default
)

# Creating sidebar
with st.sidebar:
    st.header("Image/Video Config")     # Adding header to sidebar
    # Adding file uploader to sidebar for selecting images
    source_img = st.sidebar.file_uploader(
        "얼굴등록", type=("jpg", "jpeg", "png", 'bmp', 'webp'))

# Creating main page heading
st.title("얼굴등록 페이지")


if source_img:
    st.header("input image")
    # Opening the uploaded image
    uploaded_image = Image.open(source_img)
    # Adding the uploaded image to the page with a caption
    st.image(source_img,
                caption="Uploaded Image",
                use_column_width=True)

if source_img:
    image_name = st.text_input("등록 이름")
    if image_name:
        if st.button("등록"):
            uploaded_image.save("database/"+image_name+".png")
            st.write(image_name+"등록왈료")

