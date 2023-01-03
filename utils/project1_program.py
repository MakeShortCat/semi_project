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
    pic_loc = 'https://lh3.googleusercontent.com/fife/AAbDypDrUOMvWqppUAxxj27-6V0XcLni4J_66ksNWpyvIO2WavXoxdiWZlUQxPJ99XBvYvNfQZ-grde-fBFge5_ABCzYaRG_mbeTgrL3YvMU6DY-rGLmzPGXfu1eiUemcxoTYxYVmaXMEXus6asecRKH3FRwO_WSW7vWae1BEHWCESEkrkjjRbGf0yzVcBBMIVXnrFLR0mjq5kZD1IW9YJGDzPEGDywk603MpMK_LjNzQi5kwM-b_ssb51WmVs59QZktppl_97N9Tq_7jiKUHZNArZEQRo-soMLHDXwlnYFwyW436cBWzHtx69c3AuKHgbw7pjoCTbi34OQsEj8zn2Ya_cJMhp7JuDNi9FhsEuOdiGU6HClFFylPK99nNtsA4w-w0YVofTD8JZg7Bs_Bpok38sFhxR-xFlSlGog0G6MqC0hMNYHnEmX7GcbMK0uocdgKETzCqQ5t7bFoVo0aS1qFR10DF7KgWBNCGt14QBDaRPBZ7fjBeo3rsbh1R2w3N5iMTkLl6VuVezUawX1GE1qKy9rxNrBFOlpfQOlbu0SkVKw4Gy0G_CclhqJRI-l5-WS8S63UsPyfXLevxkUddPT5-RtqYtELiyXa6BouP-VVVpizOcMD6qpn2Zr7leIj4gMMOGpbDDYzy5QZ3Jrr5KDjHtc2xqHkXQtNllkeBX6S0dLoQWM1wX-0VMtu-GkMu25vy7vw5eOTT4MQ65ShI_IAciA-ecb9ZKQCaaXOVlXOo883mxZMC6ggyblZoyRDJosg2cp2Jp09C9ssd8ph4UmvcwF3StmLbw5i3xt2LhDwgjVbUAVse8GHwJqwgZPYd9H-AyytvYLJTq_HOYDdRfWGG9CFOdnp1oT-YQc2DupIXY3mKC0OItmQzQ_UOgrVbpNIth-rWBgOgjk7azzi0qWidmePsbWNQyBeubuqHH39dIMeT6OFmauJkjVFnfhlQp4IseuTB8Qhuif8z2llZw6dVK3II1svcu14Gvygf4OkQ6hD9vyPgzeN3T-dv3naQken2kfwpZJUZ1_38tdoQquzKwsf05JKZT1_V6kV-Z3x08AfTkStfJDYepUkre3zqzDXQdWhgDHnZtqWJ_HXTK-WDHmkO2qEUnMcyZAFEVU-dxTPUyNLng2ICy4etQ2BXX7InWd0MrIw6N0OEnfnJqDM9vqui3VlcqYe0Dj5qInlVjiNQzMSAHQpOQmE6B8TNdUcqoLUfSPGCRLJq6FYf56-BsTsFDWLMAP6GdBaOcZJ5eG5h9Bn2d-gm9Q0nm-9drcrF8clRT4cTnHPNMcuTyCBRlnqEdOmH9UkqROeVWiTLz4B3p6XASf6UottPZZacV5yETSl-opXHRf55J-jeKP0wE-RxcjMYT_A3ACcwVRhSHxAI9HyF46zIO-FPQhp3PKvTff-fFLfQbWSArZmZJtwSViU2UGZaeeIhtHbpPGs5yTcGxUjabXdlewjZHXRlkc5GjZB1dntWQzmsdAXdNU=w5000-h3000'
    
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
    df3 = df3.T.reset_index(drop=False).rename(columns={'index':'명령어'})

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
            col1, col2 = st.columns([30,27])
            with col1:
                col1.subheader("지도로 표시된 위치")
                st.components.v1.html(address_return_result[0],width = 700 ,height=900)
            with col2:
                col2.subheader("엘리베이터 정보")
                st.dataframe(address_return_result[1] , height=600)
        
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
        st.image(pic_loc, width=1300)
        st.write(Script5)
            
            