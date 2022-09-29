# 주변지역


import pandas as pd
import requests

uni_df = pd.read_csv('./data/location.csv', index_col = 0)
uni_lst = list(uni_df['대학교'])
x = list(uni_df['x좌표'])
y = list(uni_df['y좌표'])

# 대학교 중심 반경 내 분석
# 문화시설(str) : 'CT1', 관광명소 : 'AT4', 숙박 : 'AD5', 병원 : 'HP8'
# radius(m 단위 int) : ex. 10000 -> 10km
def search(university, radius):
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
    # code = ['CT1', 'AT4', 'AD5', 'HP8']
    code = ['CT1', 'AT4']
    for cd in code:
        params = {'category_group_code': cd, 'x': x[index], 'y': y[index], 'radius': radius}
        res = requests.get(url, params=params, headers=headers).json()['documents']
        for r in res:
            category.append(r['category_name'].split('>')[-1].strip() + f'{cd}')
            name.append(r['place_name'])
            distance.append(r['distance'])
            addr.append(r['road_address_name'])
            culture_x.append(r['x'])
            culture_y.append(r['y'])
    df = pd.DataFrame([category, name, addr, distance, culture_x, culture_y]).T
    df.columns = ['카테고리', '건물명','도로명주소', '사이거리', 'x좌표', 'y좌표']
    return df

def search_sleep(university, radius):
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
    # code = ['CT1', 'AT4', 'AD5', 'HP8']
    code = ['AD5']
    for cd in code:
        params = {'category_group_code': cd, 'x': x[index], 'y': y[index], 'radius': radius}
        res = requests.get(url, params=params, headers=headers).json()['documents']
        for r in res:
            if '모텔' in r['category_name']:
                pass
            elif '민박' in r['category_name']:
                pass
            elif '펜션' in r['category_name']:
                pass
            elif '호텔' in r['category_name']:
                pass
            elif '유스호스텔' in r['category_name']:
                pass
            elif '게스트하우스' in r['category_name']:
                pass
            elif '산장' in r['category_name']:
                pass
            else:
                category.append(r['category_name'].split('>')[-1].strip() + f'{cd}')
                name.append(r['place_name'])
                distance.append(r['distance'])
                addr.append(r['road_address_name'])
                culture_x.append(r['x'])
                culture_y.append(r['y'])
    df = pd.DataFrame([category, name, addr, distance, culture_x, culture_y]).T
    df.columns = ['카테고리', '건물명','도로명주소', '사이거리', 'x좌표', 'y좌표']
    return df

def search_hospi(university, radius):
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
    # code = ['CT1', 'AT4', 'AD5', 'HP8']
    code = ['HP8']
    for cd in code:
        params = {'category_group_code': cd, 'x': x[index], 'y': y[index], 'radius': radius}
        res = requests.get(url, params=params, headers=headers).json()['documents']
        for r in res:
            if '종합병원' in r['category_name']:
                category.append(r['category_name'].split('>')[-1].strip() + f'{cd}')
                name.append(r['place_name'])
                distance.append(r['distance'])
                addr.append(r['road_address_name'])
                culture_x.append(r['x'])
                culture_y.append(r['y'])
            elif '대학병원' in r['category_name']:
                category.append(r['category_name'].split('>')[-1].strip() + f'{cd}')
                name.append(r['place_name'])
                distance.append(r['distance'])
                addr.append(r['road_address_name'])
                culture_x.append(r['x'])
                culture_y.append(r['y'])
            else:
                pass
    df = pd.DataFrame([category, name, addr, distance, culture_x, culture_y]).T
    df.columns = ['카테고리', '건물명','도로명주소', '사이거리', 'x좌표', 'y좌표']
    return df

def search_subway(university, radius):
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
    code = ['SW8']
    for cd in code:
        params = {'category_group_code': cd, 'x': x[index], 'y': y[index], 'radius': radius}
        res = requests.get(url, params=params, headers=headers).json()['documents']
        for r in res:
            category.append(r['category_name'].split('>')[-1].strip() + f'{cd}')
            name.append(r['place_name'])
            distance.append(r['distance'])
            addr.append(r['road_address_name'])
            culture_x.append(r['x'])
            culture_y.append(r['y'])
    df = pd.DataFrame([category, name, addr, distance, culture_x, culture_y]).T
    df.columns = ['카테고리', '건물명','도로명주소', '사이거리', 'x좌표', 'y좌표']
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
                category.append(r['category_name'].split('>')[-1].strip() + '기차역')
        else:
            continue
    df = pd.DataFrame([category, station, addr, distance, station_x, station_y]).T
    df.columns = ['카테고리', '건물명', '도로명주소', '사이거리', 'x좌표', 'y좌표']
    return df

# 버스터미널 목록
def bus(university, radius):
    global uni_lst, x, y
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
    headers = {"Authorization" : "KakaoAK "}
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
            category.append(r['category_name'].split('>')[-1].strip() + '버스터미널')
            addr.append(r['road_address_name'])
        else:
            continue
    df = pd.DataFrame([category, station, addr, distance, station_x, station_y]).T
    df.columns = ['카테고리', '건물명', '도로명주소', '사이거리', 'x좌표', 'y좌표']
    return df

# 시설 반경 10km, 정류장, 기차역 반경 5km, 지하철역 반경 1km
def uni_bound(university):
    df = pd.concat([search(university, 10000), search_sleep(university, 10000), search_hospi(university, 10000), search_subway(university,1000), bus(university, 5000), train(university, 5000)])
    df.reset_index(drop=True, inplace=True)
    df.index.name = university
    df.to_csv(f'./data/{university}반경내시설.csv')

for uni in uni_lst:
    uni_bound(uni)

