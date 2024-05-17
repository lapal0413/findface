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
    source_img2 = st.sidebar.file_uploader(
        "Choose an image2...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))

@st.cache_data(show_spinner="loading...")
def get_model_result(source_img):
    final_number,legend_list,strings=model(source_img)
    return final_number,legend_list,strings

@st.cache_data(show_spinner="loading...")
def get_table(final_number,legend_list,strings):
    final_number_np=np.array(final_number)
    table = model.data_to_table([final_number_np,legend_list,strings])
    return table


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

# Creating two columns on the main page
# col1, col2, col3 = st.columns(3)


# # Adding image to the first column if image is uploaded
# with col1:
#     if source_img:
#         st.header("input image")
#         # Opening the uploaded image
#         uploaded_image = Image.open(source_img)
#         # Adding the uploaded image to the page with a caption
#         st.image(source_img,
#                     caption="Uploaded Image",
#                     use_column_width=True)

# with col2:
#     st.header("col2")
#     if source_img2:
#         st.image(source_img2,
#                 caption="Uploaded Image",
#                 use_column_width=True)

# with col3:
#     st.header("col3")