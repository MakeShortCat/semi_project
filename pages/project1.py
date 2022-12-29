import streamlit as st
from PIL import Image
from utils import project1_program as p1p
st.set_page_config(layout="wide")
def app():
    st.write('''##세미프로젝트
             ''')
    
    Names = ['개발 환경 구축 정보 및 매뉴얼', 'Streamlit을 활용한 웹서버 구축 및 Diagram', 
             'Streamlit 매뉴얼', '자료 수집 과정', '자료 처리 Diagram']
    
    p1p.program_manual(Names[0])
    p1p.Streamlit_Diagram(Names[1])