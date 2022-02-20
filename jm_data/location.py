# 행정동 가져오기

import pandas as pd
import requests

uni_df = pd.read_csv('./data/location.csv', encoding='UTF-8', index_col=0)

url = 'https://dapi.kakao.com/v2/local/geo/coord2regioncode.json'
headers = {"Authorization" : "KakaoAK e888bb19dc37d394e91822fbef88d445"}
uni = []
dong = []
for i, row in uni_df.iterrows():
    params = {'x': row['x좌표'], 'y': row['y좌표']}
    res = requests.get(url, params=params, headers=headers).json()['documents'][0]
    uni.append(row['대학교'])
    dong.append(res['address_name'])

uni_df['행정동'] = dong
uni_df.to_csv('./data/location.csv', encoding='UTF-8')