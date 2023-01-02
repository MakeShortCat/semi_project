#웹서버 설치 : streamlit
#가상환경 설치 : anaconda
#conda create -n prj python=3.7.4 ipython numpy matplotlib pandas scipy
#ls : 파일 혹은 디렉토리 이름 확인 명령어
#cd : 디렉토리 변경 명령어
#상위 디텍고리로 : cd..
#pwd : 현재 폴더 확인 하는 명령어
#exit() : 빠져나오기
#streamlit run app.py
#라이브러리 목록 얻어내기 / 동일한 가상환경 conda env export > base_enviroment.yml
#conda env export -n prj > prj_enviroment.yml
#conda env create -f base_enviroment.yml
#conda activate prj
from os import name
import xml.etree.ElementTree as et
import pandas as pd
import bs4
from lxml import html
from urllib.parse import urlencode, quote_plus, unquote
import requests
import pprint
from geopy.geocoders import Nominatim
import folium
import streamlit as st
import streamlit.components.v1 as components

#인증키 입력
encoding = 'WDXRcaSqoBE1NSpfEeDrqFksgq6aV7XCzcP4k%2Bcekh34vup83u8dKF%2FZL9iabX8wvt9G09fCarklwHqPWVxknA%3D%3D'
decoding = 'WDXRcaSqoBE1NSpfEeDrqFksgq6aV7XCzcP4k+cekh34vup83u8dKF/ZL9iabX8wvt9G09fCarklwHqPWVxknA=='

#url 입력
url = 'http://openapi.elevator.go.kr/openapi/service/ElevatorOperationService/getOperationInfoList'

params ={'serviceKey' : decoding , 
'pageNo' : '1', 
'numOfRows' : '10',
'buld_address' : '천호동'}

response = requests.get(url, params=params)

print(response.content)

# xml 내용
content = response.text

# 깔끔한 출력 위한 코드
pp = pprint.PrettyPrinter(indent=4)

xml_obj = bs4.BeautifulSoup(content,'lxml-xml')
rows = xml_obj.findAll('item')
rows
len(rows)

row_list = [] # 행값
name_list = [] # 열이름값
value_list = [] #데이터값


for i in range(0, len(rows)):
    columns = []
    columns = rows[i].find_all()
    #첫째 행 데이터 수집
    for j in range(0,len(columns)):
        if i ==0:
            # 컬럼 이름 값 저장
            name_list.append(columns[j].name)
        # 컬럼의 각 데이터 값 저장 
        value_list.append(columns[j].text)
    # 각 행의 value값 전체 저장
    row_list.append(value_list)
    # 데이터 리스트 값 초기화
    value_list=[]

try:
    elv_df = pd.DataFrame(row_list, columns=name_list)
    
except:
    name_list.append('temp')
    elv_df = pd.DataFrame(row_list, columns=name_list)

#주소 좌표 변환
geo_local = Nominatim(user_agent='South Korea')

def geocoding(address):
    try:
        geo = geo_local.geocode(address)
        x_y = [geo.latitude, geo.longitude]
        return x_y

    except:
        return [0,0]
    
loc_x_y = []

for i in elv_df['address1']:
    loc_x_y.append(geocoding(i))

len(elv_df)
##좌표로 변환하여 folium에 표시

address_df = pd.DataFrame({'주소':elv_df['address1'],'승강기 구분': elv_df['elvtrDiv'],'승강기 상태':elv_df['elvtrSttsNm'], '좌표' : loc_x_y})

for i in range(len(address_df['주소'])):
    if address_df.좌표[i] == [0, 0]:
        address_df.drop(i, inplace=True)

Map = folium.Map(location=[37.541, 126.986],
               zoom_start=11, 
               width=750, 
               height=500
              )

for i in range(0 ,len(address_df['좌표'])):
    folium.Marker(address_df['좌표'].iloc[i],
                popup=elv_df['address1'].iloc[i],
                tooltip=(elv_df['elvtrDiv'].iloc[i], elv_df['elvtrSttsNm'].iloc[i])).add_to(Map)

Map._repr_html_()

