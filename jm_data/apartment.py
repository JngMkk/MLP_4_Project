import pandas as pd
import requests
def apartment(university, radius):
    global uni_lst, x, y
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
    headers = {"Authorization" : "KakaoAK e888bb19dc37d394e91822fbef88d445"}
    index = uni_lst.index(university)
    params = {'query': '주거시설', 'x': x[index], 'y': y[index], 'radius': radius}
    res = requests.get(url, params=params, headers=headers).json()['documents']
    station = []
    distance = []
    station_x = []
    station_y = []
    category = []
    addr = []
    for r in res:
        station.append(r['place_name'])
        distance.append(r['distance'])
        station_x.append(r['x'])
        station_y.append(r['y'])
        category.append(r['category_name'])
        addr.append(r['road_address_name'])
    df = pd.DataFrame([category, station, addr, distance, station_x, station_y]).T
    df.columns = ['카테고리', '건물명', '도로명주소', '사이거리', 'x좌표', 'y좌표']
    df.to_csv(f'./data/{university}apartment.csv')

uni_df = pd.read_csv('./data/location.csv', index_col =0)
uni_df['대학교'][7] = '두원공과대학교안성캠퍼스'
uni_df['대학교'][12] = '영남외국어대학'
uni_lst = list(uni_df['대학교'])
x = list(uni_df['x좌표'])
y = list(uni_df['y좌표'])
for uni in uni_df['대학교']:
    apartment(uni, 10000)
