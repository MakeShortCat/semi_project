import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from utils import address_transform as at1
from geopy.geocoders import Nominatim
from PIL import Image
from os import name
import xml.etree.ElementTree as et
import bs4
from lxml import html
from urllib.parse import urlencode, quote_plus, unquote
import requests
import folium


def program_manual(names):
    Script1 = '''Anaconda의 가상환경을 사용하였다 설치한 라이브러리로는 ipython, numpy, matplotlib, pandas, scipy, PIL, os,
    xml, bs4, requests, folium이 있다.

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
    project1.py에 있는 app()에서 해당 프로젝트 전체 설명과 각 주제의 이름을 관리하고 주제의 내용은 project1_program.py에서
    함수를 불러오는 형태로 받아온다.
    project1_program.py 에서 각 항목별로 함수를 만들어, 각 항목에대한 설명은 Script에 담겨있고 이미지는 pic_loc에 있다
    '''
    pic_loc = 'https://lh3.googleusercontent.com/fife/AAbDypDrIy7PKLTyHGfCY1HEywNpjSGXlT9sLln5FH413swN4jODLBZWpsRCbATKN5Jf1uN23aGu_QE6SzqPJIf00PiGANRcLvrNTtA1_nSfxSuD15DRVHmMjq3EJtC4wrYlnqQChB0FTx3_GaI0WumJCrUReSRkLClFVVMV9lPM9DEg6m86tVVNMbtjorwEXvrOPLlt5vIJ_B7005ksAz9Ecnft-iq_ECknqlNVOtJ7wVHhW_1w0YklNrJb0rZw46qgc4KCFWAWFRWX1f6dakCrBtFpn6wuIGtrO15SsH8dWJrf_r4vQ3FCEqesxXeo0auz_FnfLVvZRVIJiUQ5kflEO0nhXevckY78HxAR4SZ2UegTf0K0Q6tQD_xUbjfBz8kUT0_GP3OBXSjDUT_jWw3n-nonPpzVzvFzpEivnxK0Ljq0BnMx4zHV3iT2nwcQWL9pVn_kvwIJqUkJvBxrFWOEacdS-LJr5CltBQDm4TDBZ66TGRLuo8M0f7hXY2FqgXQdPwTTYFUw-dv2KSbjHEl1hSTtwIGZSoltGGuw7LBvjF2k_Pyu5Vv4G4H6EZsAf84M158v6bHoDjnTg8XXc2xxuqcxim4D32JsOIa15zAtPBO2Wx_Pa2733dqKGBG0ECLHJEjbkt4CMZI5leNOr0ExDKryZL24-PRPxZrqMVfDZ0L5OAoFre4C3MMnKVOKoLVJRhHWBR2ZvW-rh9QJuhaALWlajutslMKLUC2Awfxu4dxgsvJM-ZaQ09T_Vy106_Pl_wndvg4UbFQAv4T1THTmPN16Ai9KxiylFm29tc5ngvQAtR5ZkYay3QwPln8S_9bi-wcD_W7OKTCxQdlxjbcz26l-dOIw5MLfcPpLMejuKUdnl4gD8KDUPLG2wqGezMqFpERp5-vGDCfNIRDa50wLj_C5CAOcomGba60EBmZ90_lJ_HdPWWHQjvRN1sL_k0FG_RT3gxHfByhERq7QZ5C2hgYEQTqWjHq8XMZ3FUhdVNC5fJuFmt-8aNO0Z56bLSI0t_cbAB23IYp4r1c9LWVdq7iPkpobDTTi0mvn2rW9c6EUCyb3Cbv-aq-FHDSyf2rr3f9KS-GrtTzt_rxHUpoRKGojrMHWoX_S8EPC0IHm88sJEW8eTWSUBV_8xgh3Il4512d0gFfEEiqrtUMMpBrvw-LAaM46QQvaA5o5X1cnFhzHG2kSidowS8jIF_lBnW9XlJQPl48mPHeAHhKs7IlDWbCoAyABVJA4s46kTlreKFf6s2MLqLwMrElkXEVDu4UtEDeqN3iNkvRZ1X9i3w_m6QZ6u49zvosIa3JHSWx5RXkSBzG-uMeP-zywdAW7m8PPJlqRCrEY3p-fpM29rmglKu86aSUqM4Y393xD11Dk_GYKbiGfo9IuGXgdC1zzO4OkP6o8gSb3_3g8o6WWIAP1JcPkG6bIhQW05pHObADLnr1aFrcXri_NxMqeCxUKG2Ku59Tm_nXMbyCwcI05wl0=w2560-h1190'
    
    with st.expander(names):
        st.image(pic_loc, width=1100)
        st.write(Script2)

def Streamlit_Manual(names):
    Script3 = '''Streamlit 명령어와 그 사용법이다'''
    inst_Dict = {'title' : '제목 입력', 'sidebar' : '본문 옆에 사이드바 생성',
                 'selectbox' : '여러개중에서 하나를 선택할 수 있는 박스 생성',
                 'write' : '글자를 적을 수 있음', 'expander' : '문서를 열고 닫을수 있는 박스 생성',
                 'image' : 'url이나 로컬 저장소 위치에 있는 이미지 파일 삽입',
                 'dataframe' : '데이터 프레임 삽입'}
    df3 = pd.DataFrame(inst_Dict, index=['설명'])
    with st.expander(names):
        st.write(Script3)
        st.dataframe(df3)
#주소를 좌표로 변경        


def Data_Handle(names):

    Script4 = '''공공데이터 포털의 엘리베이터API를 활용하여 지역명을 입력하면 그 지역의 엘리베이터를 표시합니다.'''
    
    with st.expander(names):
        st.write(Script4)
        location = st.text_input(label="지역을 입력하세요", value="지역명")
        page = st.number_input(label = '페이지를 입력하세요', min_value=1, max_value=9999)
    
        if st.button("검색"):
            con1 = st.container()
            con1.caption(f"{location}에 있는 엘리베이터 입니다.")
            address_return_result = at1.address_trans(location, int(page))
            st.components.v1.html(address_return_result[0],width = 800 ,height=700)
            st.dataframe(address_return_result[1])
        
        ascii_trans = st.text_input(label="문자를 입력하세요")
        
        if st.button('변환'):
            con2 = st.container()
            con2.caption(f"{ascii_trans}의 변환값입니다.")
            ascii_temp = []
            for i in ascii_trans:
                ascii_temp.append(str(ord(i)))
            ascii_com = ' '.join(ascii_temp)
            st.write(f'{ascii_com}')
            
def Data_Diagram(names):
    pic_loc = 'https://lh3.googleusercontent.com/fife/AAbDypAv7PnMjlcKTzuKgRUCez4R3U3UF_VUslmELnlPw0i-zXZa_WitYApmFBhZh8RxN0N-LLy2zPTPHGIYuW_Wz0X_S5KBwqX7a-aLBzef8FpIPbhQ2NhMk_jtqkQe7auZJrUk4DLTq7-gM9vrzXnYf9Om91Is-JSHtmCjoBW98LtZgvw3_pzSjj0pJaOymITyjJXiJ-JNcrkgn6jSU2Bu-JEUGBDIKfP_u1em83JpDf4VR2Up6B4OHqA0EixEbOjcMHSe5JONe-KDqXpmA5EgfNlMLr0DhOhq682LPPmroMZYg7OkLHM8Wnasu8FmuO6fFo9UhpcoQSKTNX2hCIoGobKSQIJ94aWZfeYWTHV3iTAyIRB6vG6I339U_pnNUoS3fHNvVCH-g3nMsxCQ8w9OP9befe_my82A_BwcMahjg3I9oWR_e3kJHsKCU13ieySRgjiob8xf2D4f5KZXrPhKgZPLBYuTgVJnKR7CJBWWEr6T0xhogGACc8590bttj-JqJqV2Pm9fvMuj8L6s7MISWLfUAQIAwZn6wYnD16GLufhyGjlhsv3-hCSWASUbIf2YM7oyEQY44u-uNzKKOdFUX8iqxICgbGIcbBUvNf5DbbiF45gCyZae_9LUb0ygb6zd_zsd5qXq7vSoNqujr8tE9hf03Pod514sH9ZymRm7gluB1UDQksMsUJ5kaNiSDkE4PQT8lGWTksTMzcus0dlyT0YyKxyfTtOfSZvpC0M05ru2qErxljojdboyHzOVqoNglix-20E4nl14Jz4QVWqs7pIEre-ZZTpUxyi-hjvwNRQZBZuA6t1Kwq4pWMlcvFuV66IBgyJdlkrWiA9q3FrZLX0LJhRZHP8aCOsfj6jFD7q-_T0T6IloR4omnNZ2H2KmsHZRTVxMBmHvvGwz20aIwn5HxLX-MCHLgGkdvHsp1Jc6gnHsHztyByiJTUF5asRHfErN_ewdBFR4Npk8NgwD7-qyRnGrbWZnlVQLoBxeKNA-MYs0W1o58hqRhNpDZMNhF1vd28VVrMLCSowrBsitbOxlDSQk9BdtZQWV0-lZ8coFSFQZOa-oVqa8U3Ux5CZWKwMfCETiOritL5XPY9J43FNXvI7Hjt1JH5eo-Pv4i9j813DaE44CDAJqtsu4iTHL3DnlaYXQPohqZe3C3j92zSXwJmgdxZDH1Ia3VKzKL9byWNYWnzsiNMUOVqkKK3Zapjd6n-76bYwxDnQcDbqtfTFO8JEJYfNT65zif-jJrOSXS9QfR10HnxYgrvyL86LhMRDYQKjYAJibDut6jYqX-rZEfqTwH0j0E0peKScPNFm68XNPEvefd8ITLDTkMj-Uq1RNitrBlSQ8lmOdlJdVzMpbO547tIBERC2n6hzyLwjIQG6NTptZBy_F_0DsNCPqkfrCx75P4i0BTQKPqy6_hX0-7h_uCbCfEeWVwQNU-uq5em0I3gRlsQwFM2m6Mf-i7z6n9vb4z3w4pC_ey95SjFM=w7000-h5000'
    Script5 = '''데이터의 흐름을 표시한 Diagram 입니다. 지역명과 페이지를 입력받으면
    공공데이터 포털의 API에서 자료를 받아온 뒤에 folium에 맞게 가공하여 웹 페이지 내부에 지도와 데이터프레임으로 표시합니다'''
    with st.expander(names):
        st.image(pic_loc, width=1800)
        st.write(Script5)
            
            