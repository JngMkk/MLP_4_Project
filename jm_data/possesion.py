# 면적

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
driver.get('https://ko.wikipedia.org/wiki/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EB%8C%80%ED%95%99_%EC%BA%A0%ED%8D%BC%EC%8A%A4_%EB%A9%B4%EC%A0%81_%ED%98%84%ED%99%A9')
time.sleep(5)

df = pd.read_csv('./data/location.csv', index_col=0)

parse()
lst = list(df['대학교'])
row = soup.select('.wikitable > tbody:nth-child(2) > tr')
uni = []
pos = []
for r in row:
    if r.find('td').text in lst:
        uni.append(r.find_all('td')[0].text)
        pos.append(r.find_all('td')[4].text)

pos_df = pd.DataFrame([uni,pos]).T
pos_df.columns = ['대학', '면적']

pos_df.sort_values(by='대학', inplace=True)
pos_df.reset_index(drop=True, inplace=True)
df.sort_values(by='대학교', inplace=True)
df.reset_index(drop=True, inplace=True)

df = pd.concat([df, pos_df['면적']],axis=1)
for i, row in enumerate(df['면적']):
    df['면적'][i] = int(row.replace(',', ''))

df.rename(columns={'면적':'면적(m^2)'}, inplace=True)
df.to_csv('./data/location.csv', encoding='utf-8')


