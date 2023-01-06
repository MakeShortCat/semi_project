import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from utils import address_transform as at1
from utils import Rank_app as ra1
from geopy.geocoders import Nominatim
from PIL import Image
from os import name
import xml.etree.ElementTree as et
import bs4
from lxml import html
from urllib.parse import urlencode, quote_plus, unquote
import requests
import folium
import time
import datetime
import urllib.request as ur

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
    item = item1이 되어 project1.py에 있는 p1.app()이 실행된다
    project1.py에 있는 app()에서 해당 프로젝트 전체 설명과 각 주제의 이름을 관리하고 주제의 내용은 project1_program.py에서
    함수를 불러오는 형태로 받아온다.
    project1_program.py 에서 각 항목별로 함수를 만들어, 각 항목에대한 설명은 Script에 담겨있고 이미지는 pic_loc에 있다
    '''
    pic_loc = 'https://lh3.googleusercontent.com/fife/AAbDypCTRQnHPcUQR3pC4HjaFL4vLI3XkQhrRMkX42hbhcGenQ8GN2zx3VaWAioGreEgDbHZ0NlF4PyslbRZTtbK-Q0Xe6M7Ielq_ulnXqyuf_VPWxa1Z0ULstH_LaIEjXj1TSaDeFVUaG2370y3aMGuNcDDgI0QC4lcVKtTtLSxFL6IAfMmqgL3iTgC0kxnQ9HjlqoEjfryM9RR6R9UmboVe-rMhTV8U8LLhz7_2yR_8auwOr_uykxOKKty28xQ8irD3ia1ypXcw5IHhYxtoXeXmO-HzeQxIPub8PH5nVzmCm8Jps0vP5Sv9cPzI9ntbKajZenzoZctBPJV7s1XRIMOKisBOXxb1BuoeDRxEsZZlB-6r-P5J-OFOZaUWhRVuEqjbY1AV6yBaJW3SBQsdaaX3Qs57Cu83wUaAVv9QZdcTqrCgyTwhnDYj72WRb-rK5NFYtDVDO08Gt0oTd03nJK9QSvRqGuSr1D1BnXZm7Dz77omkGJ2rS7OjF7RMUK9fwta6pEUi9BEWhdQBGSuFjEevBmECV80ZI5LL7y_heiIV6S251uY6S6yMtiJvdSY5eUCcHxxwFndy9RlZKaeN52fvOfrjneNflyYfvHZcWCzCf2JqCycDUxjJU67faOiFsOTteCtzNIx8hHkJ09dijZH0yMgJ8C6nXywazaqcsgPSoDueeRxP1cAeFxG2QRj1VEkU09Ov98WvXoMFJWjidX1B7lvH1QLs1Rn7d5gTu8J8OoiXun-OBUKl1PDby0Rmtd5UJ2M6T3eMzcezZKPPr4UfxNOBst8Ki9hIsiwH5s_UeThKA2GeNIMUGEj134bwuciuXdKbWk3YTfftPb5mGNPGbeOm8erUH61YxJh0xFn3LXKaa_Qz4C6KrzIpExVBh8JWfcOdNIYkbdwco5kBPEVw2cIu1Bx4m0tayQIlfbqMCVWz7X8tqYCaqJGroDIeZiutqQIvstd5UUAejY6zX7DBhXqa71IkrwRWoN2eYygah21NPLyCCnzboiRGIwPpjngNlOH9sMrZ03NStgTz6bKnscl6X6idqCf3xzCYtN8xg2sbmmt2GAdEXxUqP_TJUsYY6gmJIOyqj-bZ2aGqO23YnSLmkSNvk_AEmbANJdN7AgI0jsySWFKNbIkuXnSk1S1cL7gHHnF73GUJYz4qo3e2yEd0ZMI5cavQF3GA4sKTUFb94bh2-oN1g9Yi3hEFd6enZZKrLqtBM26Dlu38CVH7kLcAdaBriUDOIfLc7L5h_MySEnx8E_0RLx1KFcvhVkFdu9wD8hDSSXqYlpmGosFy4n7bH0Jh8TNu4s2FRN6_G-rVW5Rp0ECq1TCbqF6GaU0QyB1mtY2xeqrTb5XXFtgN1Utq5hnuTQu0ti-ApmPHmhqjAQdz4gUe7Rj5qMSpgppQpLnBhfMn9Cg2phQKme-MItha9CHQMjPS2qpP9zFuIngIouI1Pd3b-hjwhbmblgTiDBsu1WNFA6Nc72f3Qo=w3000-h3000'
    
    with st.expander(names):
        st.image(pic_loc, width=1000)
        st.write(Script2)

def Streamlit_Manual(names):
    Script3 = '''Streamlit 명령어와 그 사용법이다 이 웹 페이지를 만드는데 사용된 구조는 본문 옆에 사이드바의
    셀렉트 박스에서 item_list에 있는 항목들 중 하나를 고른다 이때 item_list는 그대로 표시되지 않고 format_func = FIL에 의하여
    FIL함수에 의해 바뀌어서 표시되게 된다. 항목중 하나를 고르면 p1.app, p2.app, intro.app중 하나가 실행된다.'''
    inst_Dict = {'title' : '제목 입력', 'sidebar' : '본문 옆에 사이드바 생성',
                 'selectbox' : '여러개중에서 하나를 선택할 수 있는 박스 생성',
                 'write' : '글자를 적을 수 있음', 'expander' : '문서를 열고 닫을수 있는 박스 생성',
                 'image' : 'url이나 로컬 저장소 위치에 있는 이미지 파일 삽입',
                 'dataframe' : '데이터 프레임 삽입'}
    Parameters = ['사용한 Parameter', 'body : 내용 삽입', '', 'label : 제목 정하기 \n\noptions : 선택지 \n\nformat_func : 선택지를 정해진 함수대로 표시함',
                  'args : 내용 적는곳', 'label : 문서 여닫이 박스 제목', 'image : 이미지 파일 지정 \n\nwidth : 이미지 폭',
                  'data : 데이터 지정 \n\nwidth : 데이터프레임 폭 지정 \n\nheight : 데이터프레임 높이 지정']
    Parameters = pd.DataFrame(Parameters)
    Parameters = Parameters.rename(columns=Parameters.iloc[0]).drop(Parameters.index[0]).reset_index(drop = True)
    df3 = pd.DataFrame(inst_Dict, index=['설명'])
    df3 = df3.T.reset_index(drop=False).rename(columns={'index':'명령어'})
    df3 = pd.concat([df3,Parameters],axis=1)
    
    with st.expander(names):
        st.write(Script3)
        st.dataframe(df3)
#주소를 좌표로 변경        


def Data_Handle_map(names):

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
                
def Data_Handle_apps(names):
    Script5 = '''앱스토어 홈페이지에서 오늘날짜의 어플 순위를 가져옵니다.'''
    free_url = 'https://apps.apple.com/kr/charts/iphone/top-free-apps/36'
    paid_url = 'https://apps.apple.com/kr/charts/iphone/top-paid-apps/36'
    
    with st.expander(names):
        st.write(Script5)
        if st.button("어플 순위 검색"):
            st.dataframe(ra1.ranking_iapp(free_url), width = 900, height = 600)
            st.dataframe(ra1.ranking_iapp(paid_url), width = 900, height = 600)


def Data_Diagram(names):
    pic_loc = 'https://lh3.googleusercontent.com/fife/AAbDypAv7PnMjlcKTzuKgRUCez4R3U3UF_VUslmELnlPw0i-zXZa_WitYApmFBhZh8RxN0N-LLy2zPTPHGIYuW_Wz0X_S5KBwqX7a-aLBzef8FpIPbhQ2NhMk_jtqkQe7auZJrUk4DLTq7-gM9vrzXnYf9Om91Is-JSHtmCjoBW98LtZgvw3_pzSjj0pJaOymITyjJXiJ-JNcrkgn6jSU2Bu-JEUGBDIKfP_u1em83JpDf4VR2Up6B4OHqA0EixEbOjcMHSe5JONe-KDqXpmA5EgfNlMLr0DhOhq682LPPmroMZYg7OkLHM8Wnasu8FmuO6fFo9UhpcoQSKTNX2hCIoGobKSQIJ94aWZfeYWTHV3iTAyIRB6vG6I339U_pnNUoS3fHNvVCH-g3nMsxCQ8w9OP9befe_my82A_BwcMahjg3I9oWR_e3kJHsKCU13ieySRgjiob8xf2D4f5KZXrPhKgZPLBYuTgVJnKR7CJBWWEr6T0xhogGACc8590bttj-JqJqV2Pm9fvMuj8L6s7MISWLfUAQIAwZn6wYnD16GLufhyGjlhsv3-hCSWASUbIf2YM7oyEQY44u-uNzKKOdFUX8iqxICgbGIcbBUvNf5DbbiF45gCyZae_9LUb0ygb6zd_zsd5qXq7vSoNqujr8tE9hf03Pod514sH9ZymRm7gluB1UDQksMsUJ5kaNiSDkE4PQT8lGWTksTMzcus0dlyT0YyKxyfTtOfSZvpC0M05ru2qErxljojdboyHzOVqoNglix-20E4nl14Jz4QVWqs7pIEre-ZZTpUxyi-hjvwNRQZBZuA6t1Kwq4pWMlcvFuV66IBgyJdlkrWiA9q3FrZLX0LJhRZHP8aCOsfj6jFD7q-_T0T6IloR4omnNZ2H2KmsHZRTVxMBmHvvGwz20aIwn5HxLX-MCHLgGkdvHsp1Jc6gnHsHztyByiJTUF5asRHfErN_ewdBFR4Npk8NgwD7-qyRnGrbWZnlVQLoBxeKNA-MYs0W1o58hqRhNpDZMNhF1vd28VVrMLCSowrBsitbOxlDSQk9BdtZQWV0-lZ8coFSFQZOa-oVqa8U3Ux5CZWKwMfCETiOritL5XPY9J43FNXvI7Hjt1JH5eo-Pv4i9j813DaE44CDAJqtsu4iTHL3DnlaYXQPohqZe3C3j92zSXwJmgdxZDH1Ia3VKzKL9byWNYWnzsiNMUOVqkKK3Zapjd6n-76bYwxDnQcDbqtfTFO8JEJYfNT65zif-jJrOSXS9QfR10HnxYgrvyL86LhMRDYQKjYAJibDut6jYqX-rZEfqTwH0j0E0peKScPNFm68XNPEvefd8ITLDTkMj-Uq1RNitrBlSQ8lmOdlJdVzMpbO547tIBERC2n6hzyLwjIQG6NTptZBy_F_0DsNCPqkfrCx75P4i0BTQKPqy6_hX0-7h_uCbCfEeWVwQNU-uq5em0I3gRlsQwFM2m6Mf-i7z6n9vb4z3w4pC_ey95SjFM=w3000-h3000'
    Script6 = '''데이터의 흐름을 표시한 Diagram 입니다. 지역명과 페이지를 입력받으면
    공공데이터 포털의 API에서 자료를 받아온 뒤에 folium에 맞게 가공하여 웹 페이지 내부에 지도와 데이터프레임으로 표시합니다'''
    with st.expander(names):
        st.image(pic_loc, width=1000)
        st.write(Script6)
        
