import streamlit as st
from PIL import Image

import numpy as np
import pandas as pd
import os 
from deepface import DeepFace


# Setting page layout
st.set_page_config(
    page_title="vichart",  # Setting page title
    page_icon="🤖",     # Setting page icon
    layout="wide",      # Setting layout to wide
    initial_sidebar_state="expanded"    # Expanding sidebar by default
)


# Creating main page heading
st.title("비슷한 사람찾기 페이지")
database_root = "database/"
image = os.listdir("database")


with st.sidebar:
    st.header("Image/Video Config")     # Adding header to sidebar
    # Adding file uploader to sidebar for selecting images
    source_img = st.sidebar.file_uploader(
        "누군가요?", type=("jpg", "jpeg", "png", 'bmp', 'webp'))

col1, col2 = st.columns(2)



with col1:

    if source_img:
        uploaded_image = Image.open(source_img)
        # Adding the uploaded image to the page with a caption
        st.image(uploaded_image,
                    caption="Uploaded Image",
                    use_column_width=True)
        uploaded_image.save("temp.png")

with col2:
    if st.button("같은/비슷한 사람은??"):
        dfs = DeepFace.find(
        img_path = "temp.png", 
        db_path = database_root, 
        distance_metric ="cosine",
        )
        if "Empty " in str(dfs):
            st.write("없음")
        else:
            st.write(dfs[0]["identity"])
            for each in dfs[0]["identity"]:
                st.image(each)
