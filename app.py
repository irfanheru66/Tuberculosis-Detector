import streamlit as st
from PIL import Image
from detection import process
import numpy as np
# Page settings
st.set_page_config(
    page_title="Image Detection",
    layout="wide",
    initial_sidebar_state="expanded"
 )

# Title
st.title('Tuberculosis Detection from sputum sample')

# Upload file
uploaded_file = st.file_uploader(label="Choose a file", type=['jpg', 'jpeg','png'])

sidebar = st.sidebar

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')

    col1, col2 = st.columns([0.5, 0.5])

    #Col 1
    with col1:
        st.markdown('<p style="text-align: center;">Input Image</p>', unsafe_allow_html=True)
        st.image(image,caption="Sputum sample")
       
    with col2:
        st.markdown('<p style="text-align: center;">Detected Image</p>', unsafe_allow_html=True)
        image_arr,total =  process(np.array(image))
        st.image(Image.fromarray(image_arr),caption="Tuberculosis detected")
        st.markdown(f'<p style="text-align: center;">Bacteria detected : {total}</p>', unsafe_allow_html=True)