import pandas as pd
import requests

uni_df = pd.read_csv('./data/location.csv', index_col = 0)
uni_lst = list(uni_df['대학교'])
x = list(uni_df['x좌표'])
y = list(uni_df['y좌표'])

# 대학교 중심 반경 내 분석
# 문화시설(str) : 'CT1', 지하철역 : 'SW8', 관광명소 : 'AT4', 숙박 : 'AD5', 병원 : 'HP8'
# radius(m 단위 int) : ex. 10000 -> 10km
def search(university, radius):
    global uni_lst, x, y
    index = uni_lst.index(university)
    url = 'https://dapi.kakao.com/v2/local/search/category.json'
    headers = {"Authorization" : "KakaoAK e888bb19dc37d394e91822fbef88d445"}
    distance = []
    addr = []
    name = []
    category = []
    culture_x = []
    culture_y = []
    code = ['CT1', 'SW8', 'AT4', 'AD5', 'HP8']
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
    df.index.name = university
    return df

# 반경 radius 내 기차역 목록
def train(university, radius):
    global uni_lst, x, y
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
    headers = {"Authorization" : "KakaoAK e888bb19dc37d394e91822fbef88d445"}
    index = uni_lst.index(university)
    params = {'query': '기차역', 'x': x[index], 'y': y[index], 'radius': radius}
    res = requests.get(url, params=params, headers=headers).json()['documents']
    station = []
    addr = []
    distance = []
    station_x = []
    station_y = []
    category = []
    for r in res:
        if '기차역' in r['category_name']:
            if '폐역' in r['place_name']:
                pass
            else:
                station.append(r['place_name'])
                addr.append(r['road_address_name'])
                distance.append(r['distance'])
                station_x.append(r['x'])
                station_y.append(r['y'])
                category.append(r['category_name'].split('>')[-1].strip())
        else:
            continue
    df = pd.DataFrame([category, station, addr, distance, station_x, station_y]).T
    df.columns = ['카테고리', '건물명', '도로명주소', '사이거리', 'x좌표', 'y좌표']
    return df

# 버스터미널 목록
def bus(university, radius):
    global uni_lst, x, y
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
    headers = {"Authorization" : "KakaoAK e888bb19dc37d394e91822fbef88d445"}
    index = uni_lst.index(university)
    params = {'query': '터미널', 'x': x[index], 'y': y[index], 'radius': radius}
    res = requests.get(url, params=params, headers=headers).json()['documents']
    station = []
    distance = []
    station_x = []
    station_y = []
    category = []
    addr = []
    for r in res:
        if '버스터미널' in r['category_name']:
            station.append(r['place_name'])
            distance.append(r['distance'])
            station_x.append(r['x'])
            station_y.append(r['y'])
            category.append(r['category_name'].split('>')[-1].strip())
            addr.append(r['road_address_name'])
        else:
            continue
    df = pd.DataFrame([category, station, addr, distance, station_x, station_y]).T
    df.columns = ['카테고리', '건물명', '도로명주소', '사이거리', 'x좌표', 'y좌표']
    return df

def uni_bound(university, radius):
    df = pd.concat([search(university, radius), bus(university, radius), train(university, radius)])
    km = str(int(radius / 1000)) + 'km'
    df.to_csv(f'./data/{university}반경{km}내시설.csv')

for uni in uni_lst:
    uni_bound(uni, 10000)


