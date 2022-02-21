from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

def parse():
    global soup
    html = driver.page_source
    soup = bs(html, 'html.parser')

service = webdriver.firefox.service.Service('/home/jngmk/geckodriver')
driver = webdriver.Firefox(service=service)
driver.get('https://map.kakao.com/')
time.sleep(5)

df = pd.read_csv('./data/location.csv',index_col=0)
df['대학교'][7] = '두원공과대학교안성캠퍼스'
df['대학교'][12] = '영남외국어대학'

univ = list(df['대학교'])
pos = []
for uni in df['대학교']:
    search_input = driver.find_element(By.ID, "search.keyword.query")
    search_input.send_keys(uni)
    try:
        driver.find_element(By.ID, "search.keyword.submit").click()
        time.sleep(3)
    except:
        driver.find_element(By.CLASS_NAME, "view_coach").click()
        time.sleep(1)
        driver.find_element(By.ID, "search.keyword.submit").click()
        time.sleep(3)
    parse()
    text1 = soup.select_one('#localInfo\.map\.county').text
    text2 = soup.select_one('#localInfo\.map\.town').text
    pos.append(text1 + text2)
    driver.refresh()

df = pd.DataFrame([univ, pos]).T
df.columns = ['대학', '주변행정동']
df.to_csv('./data/around.csv', encoding='utf-8')