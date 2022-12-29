import streamlit as st
from PIL import Image

def program_manual(names):
    Script1 = '''Anaconda의 가상환경을 사용하였다 설치한 라이브러리로는 ipython, numpy, matplotlib, pandas, scipy가 있다.

환경은 Anaconda powershell prompt에서
conda create -n prj python=3.7.4 ipython numpy matplotlib pandas scipy을
사용하여 파이썬 3.7.4 버전과 ipython numpy matplotlib pandas scipy 라이브러리를
사용하는 가상환경을 생성 prj이라는 환경으로 실행하였다.

실행방법 : Anaconda powershell prompt에서 conda activate prj로 가상환경을 작동시키고
(ls : 현재 폴더 파일명 보이기, cd : 해당 폴더로 이동, cd.. : 상위 폴더로) 등을 활용하여
streamlit run app.py를 실행시킨다'''


    with st.expander(names):
        st.write(Script1)

def Streamlit_Diagram(names):
    Script2 = '''이 Diagram과 같이 기본 카테고리를 선택하는 기능을 app.py에서 구현했다.
    item = 세미프로젝트가 되어 project1.py에 있는 p1.app()이 실행된다
    project1.py에 있는 app()에서 해당 프로젝트 전체 설명과 각 주제의 이름을 관리하고 주제의 내용은 project1_program.py에서 받아온다.
    project1_program.py 에서 각 항목별로 함수를 만들어, 각 항목에대한 설명은 Script에 담겨있고 이미지는 pic_loc에 있다
    '''
    pic_loc = 'https://lh3.googleusercontent.com/fife/AAbDypDrIy7PKLTyHGfCY1HEywNpjSGXlT9sLln5FH413swN4jODLBZWpsRCbATKN5Jf1uN23aGu_QE6SzqPJIf00PiGANRcLvrNTtA1_nSfxSuD15DRVHmMjq3EJtC4wrYlnqQChB0FTx3_GaI0WumJCrUReSRkLClFVVMV9lPM9DEg6m86tVVNMbtjorwEXvrOPLlt5vIJ_B7005ksAz9Ecnft-iq_ECknqlNVOtJ7wVHhW_1w0YklNrJb0rZw46qgc4KCFWAWFRWX1f6dakCrBtFpn6wuIGtrO15SsH8dWJrf_r4vQ3FCEqesxXeo0auz_FnfLVvZRVIJiUQ5kflEO0nhXevckY78HxAR4SZ2UegTf0K0Q6tQD_xUbjfBz8kUT0_GP3OBXSjDUT_jWw3n-nonPpzVzvFzpEivnxK0Ljq0BnMx4zHV3iT2nwcQWL9pVn_kvwIJqUkJvBxrFWOEacdS-LJr5CltBQDm4TDBZ66TGRLuo8M0f7hXY2FqgXQdPwTTYFUw-dv2KSbjHEl1hSTtwIGZSoltGGuw7LBvjF2k_Pyu5Vv4G4H6EZsAf84M158v6bHoDjnTg8XXc2xxuqcxim4D32JsOIa15zAtPBO2Wx_Pa2733dqKGBG0ECLHJEjbkt4CMZI5leNOr0ExDKryZL24-PRPxZrqMVfDZ0L5OAoFre4C3MMnKVOKoLVJRhHWBR2ZvW-rh9QJuhaALWlajutslMKLUC2Awfxu4dxgsvJM-ZaQ09T_Vy106_Pl_wndvg4UbFQAv4T1THTmPN16Ai9KxiylFm29tc5ngvQAtR5ZkYay3QwPln8S_9bi-wcD_W7OKTCxQdlxjbcz26l-dOIw5MLfcPpLMejuKUdnl4gD8KDUPLG2wqGezMqFpERp5-vGDCfNIRDa50wLj_C5CAOcomGba60EBmZ90_lJ_HdPWWHQjvRN1sL_k0FG_RT3gxHfByhERq7QZ5C2hgYEQTqWjHq8XMZ3FUhdVNC5fJuFmt-8aNO0Z56bLSI0t_cbAB23IYp4r1c9LWVdq7iPkpobDTTi0mvn2rW9c6EUCyb3Cbv-aq-FHDSyf2rr3f9KS-GrtTzt_rxHUpoRKGojrMHWoX_S8EPC0IHm88sJEW8eTWSUBV_8xgh3Il4512d0gFfEEiqrtUMMpBrvw-LAaM46QQvaA5o5X1cnFhzHG2kSidowS8jIF_lBnW9XlJQPl48mPHeAHhKs7IlDWbCoAyABVJA4s46kTlreKFf6s2MLqLwMrElkXEVDu4UtEDeqN3iNkvRZ1X9i3w_m6QZ6u49zvosIa3JHSWx5RXkSBzG-uMeP-zywdAW7m8PPJlqRCrEY3p-fpM29rmglKu86aSUqM4Y393xD11Dk_GYKbiGfo9IuGXgdC1zzO4OkP6o8gSb3_3g8o6WWIAP1JcPkG6bIhQW05pHObADLnr1aFrcXri_NxMqeCxUKG2Ku59Tm_nXMbyCwcI05wl0=w2560-h1190'
    
    with st.expander(names):
        st.image(pic_loc, width=1100)
        st.write(Script2)

    def Streamlit_Manual(names):
        Script3 = '''여기에 쓰인 Streamlit 명령어들을 데이터프레임 혹은 테이블로 제작'''
    