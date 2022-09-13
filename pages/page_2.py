import streamlit as st
from PIL import Image
from detection import process
import numpy as np
from torchdetect import process
import os

st.set_page_config(
    page_title="Image Detection",
    layout="wide",
    initial_sidebar_state="expanded"
 )
st.title('Tuberculosis Detection from sputum sample')
st.markdown("## inference using torch.hub")

uploaded_file = st.file_uploader(label="Choose a file", type=['jpg', 'jpeg','png'])

idebar = st.sidebar
conf_level = st.sidebar.slider("conf_level", min_value=0.0, max_value=1.0, value=0.55)
IoU = st.sidebar.slider("IoU", min_value=0.0, max_value=1.0, value=0.45)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')

    col1, col2 = st.columns([0.5, 0.5])
    

    #Col 1
    with col1:
        st.markdown('<p style="text-align: center;">Input Image</p>', unsafe_allow_html=True)
        st.image(image,caption="Sputum sample")
        imgpath = os.path.join('data/uploads', uploaded_file.name)
        
        with open(imgpath, mode="wb") as f:
            f.write(uploaded_file.getbuffer())

    with col2:
        st.markdown('<p style="text-align: center;">Detected Image</p>', unsafe_allow_html=True)
        img,total,runtime = process(imgpath,conf_level,IoU)
        st.image(img,caption="Tuberculosis detected")
        st.markdown(f'<p style="text-align: center;">Bacteria detected : {total}</p>', unsafe_allow_html=True)
        st.markdown(f'<p style="text-align: center;">{runtime}</p>', unsafe_allow_html=True)

       
    # with col2:
    #     st.markdown('<p style="text-align: center;">Detected Image</p>', unsafe_allow_html=True)
    #     image_arr,total =  process(np.array(image))
    #     st.image(Image.fromarray(image_arr),caption="Tuberculosis detected")
    #     st.markdown(f'<p style="text-align: center;">Bacteria detected : {total}</p>', unsafe_allow_html=True)
