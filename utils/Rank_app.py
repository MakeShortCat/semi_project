import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import datetime

def ranking_iapp(url):

    soup = bs(ur.urlopen(url).read(), 'html.parser')

    appstore_top = soup.find_all('p', {'dir' :"false"})
    appstore_top_company = soup.find_all('div', {'dir' :"ltr"})

    appstore_top_list = []
    appstore_top_company_list = []
    time_list = []

    for i in appstore_top:
        appstore_top_list.append(i.text)

    for i in appstore_top_company:
        appstore_top_company_list.append(i.text)

    for i in range(len(appstore_top_company_list)):
        time_list.append(datetime.datetime.today().strftime('%Y-%m-%d'))


    df_appstore = pd.DataFrame(zip(appstore_top_list, appstore_top_company_list, time_list), columns=['어플이름', '개발사', '날짜'])

    df_appstore['개발사'] = df_appstore['개발사'].apply(lambda x : x.lstrip('\n    ').rstrip('\n'))

    return df_appstore


