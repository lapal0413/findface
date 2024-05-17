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
st.title("얼굴분석 페이지")
database_root = "database/"
image = os.listdir("database")

col1, col2 = st.columns(2)
with col1:
    option = st.selectbox(
        "누굴 분석해볼까",
        image)

    st.write("You selected:", option)
    if option:
        uploaded_image = Image.open(database_root+option)
        # Adding the uploaded image to the page with a caption
        st.image(uploaded_image,
                    caption="Uploaded Image",
                    use_column_width=True)

with col2:
    if st.button("분석"):
        objs = DeepFace.analyze(
                img_path = database_root+option, 
                actions = ['age', 'gender', 'race', 'emotion'],
                )
        st.write("나이는:"+str(objs[0]["age"]))
        st.write("성별은:"+str(objs[0]["gender"]))
        
        st.write("인종은",str(objs[0]["race"]))
        st.write("표정은",str(objs[0]["emotion"]))