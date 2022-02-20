# 대학 주변지역 지도 시각화

import folium

import pandas as pd

df = pd.read_csv('./data/location.csv', index_col=0)

for _, r in df.iterrows():
    loc = folium.Map(location=[r['y좌표'], r['x좌표']], zoom_start = 13)
    df_building = pd.read_csv(f'./data/{r["대학교"]}반경내시설.csv', index_col= 0)
    for _, row in df_building.iterrows():
        if 'CT1' in row['카테고리']:
            folium.Marker(location=[row['y좌표'], row['x좌표']], icon= folium.Icon(color='orange', icon='info-sign') , tooltip=f'{row["건물명"]}').add_to(loc)
        elif 'AT4' in row['카테고리']:
            folium.Marker(location=[row['y좌표'], row['x좌표']], icon= folium.Icon(color='blue', icon='cloud'), tooltip=f'{row["건물명"]}').add_to(loc)
        elif 'AD5' in row['카테고리']:
            folium.Marker(location=[row['y좌표'], row['x좌표']], icon= folium.Icon(color='red', icon='fire'), tooltip=f'{row["건물명"]}').add_to(loc)
        elif 'SW8' in row['카테고리']:
            folium.Marker(location=[row['y좌표'], row['x좌표']], icon= folium.Icon(color='red', icon='subway'), tooltip=f'{row["건물명"]}').add_to(loc)
        elif '기차역' in row['카테고리']:
            folium.Marker(location=[row['y좌표'], row['x좌표']], icon= folium.Icon(color='red', icon='plane'), tooltip=f'{row["건물명"]}').add_to(loc)
        elif 'HP8' in row['카테고리']:
            folium.Marker(location=[row['y좌표'], row['x좌표']], icon= folium.Icon(color='green', icon='plus-sign'), tooltip=f'{row["건물명"]}').add_to(loc)
        elif '버스터미널' in row['카테고리']:
            folium.Marker(location=[row['y좌표'], row['x좌표']], icon= folium.Icon(color='red', icon='plane'), tooltip=f'{row["건물명"]}').add_to(loc)

    folium.Marker(location=[r['y좌표'], r['x좌표']], icon = folium.Icon(color='black', icon = 'book'), tooltip = r['대학교']).add_to(loc)
    folium.CircleMarker(location= [r['y좌표'], r['x좌표']], radius=50, color='black').add_to(loc)
    loc.save(f'./html/{r["대학교"]}.html')