# 주변지역 버스노선, 지하철

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import requests

uni_df = pd.read_csv('./data/location.csv', index_col = 0)
uni_lst = list(uni_df['대학교'])
x = list(uni_df['x좌표'])
y = list(uni_df['y좌표'])

def search_subway(university, radius):
    global uni_lst, x, y
    index = uni_lst.index(university)
    url = 'https://dapi.kakao.com/v2/local/search/category.json'
    headers = {"Authorization" : "KakaoAK "}
    distance = []
    addr = []
    name = []
    category = []
    culture_x = []
    culture_y = []
    code = ['SW8']
    for cd in code:
        params = {'category_group_code': cd, 'x': x[index], 'y': y[index], 'radius': radius}
        res = requests.get(url, params=params, headers=headers).json()['documents']
        for r in res:
            category.append(r['category_name'].split('>')[-1].strip())
            name.append(r['place_name'])
            distance.append(r['distance'])
            addr.append(r['road_address_name'])
            culture_x.append(r['x'])
            culture_y.append(r['y'])
    df = pd.DataFrame([category, name, addr, distance, culture_x, culture_y]).T
    df.columns = ['카테고리', '건물명','도로명주소', '사이거리', 'x좌표', 'y좌표']
    return df

def parse():
    global soup
    html = driver.page_source
    soup = bs(html, 'html.parser')

service = webdriver.firefox.service.Service('/home/jngmk/geckodriver')
driver = webdriver.Firefox(service=service)
driver.get('https://map.kakao.com/')
time.sleep(5)

for uni in uni_lst:
    search = uni
    search_input = driver.find_element(By.ID, "search.keyword.query")
    search_input.send_keys(search)

    try:
        driver.find_element(By.ID, "search.keyword.submit").click()
        time.sleep(3)
    except:
        driver.find_element(By.CLASS_NAME, "view_coach").click()
        time.sleep(1)
        driver.find_element(By.ID, "search.keyword.submit").click()
        time.sleep(3)

    driver.find_element(By.CSS_SELECTOR, ".option3").click()
    time.sleep(1)

    parse()
    bus = []
    busline = []
    time_distance = []

    bus_lst = soup.select('li.BusItem')
    for i in range(len(bus_lst)):
        driver.find_element(By.CSS_SELECTOR, f"li.BusItem:nth-child({i+1}) > div:nth-child(3) > strong:nth-child(1) > a").click()
        time.sleep(1)
        parse()
        bus_name = soup.select_one('.busname').text
        if bus_name in bus:
            pass
        else:
            bus.append(bus_name)
            bus_line = soup.select('.totalPath > span')[0].text + '-' + soup.select('.totalPath > span')[2].text
            busline.append(bus_line)
            txt = soup.select_one('p.info:nth-child(4)').text
            time_distance.append(txt)

    driver.refresh()
    

    
    df = pd.DataFrame([bus, busline, time_distance]).T
    df.columns = ['버스', '버스노선', '배차간격']
    df.index.name = uni
    if len(search_subway(uni, 1000)):
        df['지하철역'] = 'True'
    else:
        df['지하철역'] = 'False'
    df.to_csv(f'./data/{uni}1km내버스,지하철.csv', encoding='UTF-8')