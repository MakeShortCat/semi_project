import streamlit as st
from PIL import Image

def expand(Button_name, Script, image_locaition = None):  
    if st.expander(str(Button_name)):
        st.write(f'''{Script}''')
        st.image(image_locaition)