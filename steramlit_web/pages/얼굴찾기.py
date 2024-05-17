import streamlit as st
from PIL import Image

import numpy as np
import pandas as pd
import os 
from deepface import DeepFace
backends = [
  'opencv', 
  'ssd', 
  'dlib', 
  'mtcnn', 
  'fastmtcnn',
  'retinaface', 
  'mediapipe',
  'yolov8',
  'yunet',
  'centerface',
]

# Setting page layout
st.set_page_config(
    page_title="vichart",  # Setting page title
    page_icon="🤖",     # Setting page icon
    layout="wide",      # Setting layout to wide
    initial_sidebar_state="expanded"    # Expanding sidebar by default
)


# Creating main page heading
st.title("얼굴찾기 페이지")
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
    if st.button("찾기"):
        face_objs = DeepFace.extract_faces(
        img_path = database_root+option, 
        detector_backend = backends[1],)
        for faces in face_objs:
            st.write("정확도"+str(100*faces["confidence"])+"%")
            st.write(faces["facial_area"])

        # 찾은 정보 중에 원하는 정보 2점 찾기! 
        # face_points = []
        # box_image = cvt_image.copy()
        # for i in range(len(face_objs)):
        #     pt1=(face_objs[i]["facial_area"]["x"],face_objs[i]["facial_area"]["y"])
        #     pt2=(face_objs[i]["facial_area"]["x"]+face_objs[i]["facial_area"]["w"],face_objs[i]["facial_area"]["y"]+face_objs[i]["facial_area"]["h"])
        #     color=(255,0,0)
        #     box_image=cv.rectangle(box_image, pt1, pt2, color,5) 