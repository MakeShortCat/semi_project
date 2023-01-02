from os import name
import xml.etree.ElementTree as et
import pandas as pd
import bs4
from lxml import html
from urllib.parse import urlencode, quote_plus, unquote
import requests
from geopy.geocoders import Nominatim
import folium
import streamlit as st
import streamlit.components.v1 as components

def address_trans(location, PageNo):
    encoding = 'WDXRcaSqoBE1NSpfEeDrqFksgq6aV7XCzcP4k%2Bcekh34vup83u8dKF%2FZL9iabX8wvt9G09fCarklwHqPWVxknA%3D%3D'
    decoding = 'WDXRcaSqoBE1NSpfEeDrqFksgq6aV7XCzcP4k+cekh34vup83u8dKF/ZL9iabX8wvt9G09fCarklwHqPWVxknA=='

    #url 입력
    url = 'http://openapi.elevator.go.kr/openapi/service/ElevatorOperationService/getOperationInfoList'

    params ={'serviceKey' : decoding , 
    'pageNo' : f'{PageNo}', 
    'numOfRows' : '20',
    'buld_address' : f'{location}'}

    response = requests.get(url, params=params)

    # xml 내용
    content = response.text

    xml_obj = bs4.BeautifulSoup(content,'lxml-xml')
    rows = xml_obj.findAll('item')

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

    ##좌표로 변환하여 folium에 표시
    address_df = pd.DataFrame({'주소':elv_df['address1'],'승강기 구분': elv_df['elvtrDiv'],'승강기 상태':elv_df['elvtrSttsNm'], '좌표' : loc_x_y})

    for i in range(len(address_df['주소'])):
        if address_df.좌표[i] == [0, 0]:
            address_df.drop(i, inplace=True)
    

    Map = folium.Map(location=[37.541, 126.986],
                zoom_start=9, 
                width=750, 
                height=500
                )

    for i in range(0 ,len(address_df['좌표'])):
        folium.Marker(address_df['좌표'].iloc[i],
                    popup=elv_df['address1'].iloc[i],
                    tooltip=(elv_df['elvtrDiv'].iloc[i], elv_df['elvtrSttsNm'].iloc[i])).add_to(Map)

    return [Map._repr_html_(), address_df]


