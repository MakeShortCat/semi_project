import streamlit as st
from PIL import Image
from utils import project1_desc as p1d

def app():
	st.write('''
		### 세미 프로젝트
		'''
		)

	p1d.desc()
