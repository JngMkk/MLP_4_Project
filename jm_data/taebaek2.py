import pandas as pd
import requests
import folium

df = pd.read_csv('./resources/famous.csv', encoding='cp949')
df = df[df['분류'] != '쇼핑센터']
df = df[df['분류'] != '모텔/여관']
df = df[df['분류'] != '운동장']
df = df[df['분류'] != '쇼핑기타']

df.reset_index(drop=True, inplace=True)
place = list(df['관광지명'])

uni_df = pd.read_csv('./data/location.csv', index_col=0)
dff = pd.read_csv('./data/강원관광대학교반경내시설.csv', index_col = 0)

url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
headers = {"Authorization" : "KakaoAK e888bb19dc37d394e91822fbef88d445"}
x = []
y = []
loc = []
for p in place:
    params = {'query': p, 'x': uni_df.loc[0]['x좌표'], 'y' : uni_df.loc[0]['y좌표'], 'radius':10000}
    res = requests.get(url, params=params, headers=headers).json()['documents']
    try:
        x.append(res[0]['x'])
        y.append(res[0]['y'])
        loc.append(p)
    except:
        continue

loc = folium.Map(location=[uni_df.iloc[0, 3], uni_df.iloc[0, 2]], zoom_start = 13)
folium.Marker(location=[uni_df.iloc[0, 3], uni_df.iloc[0, 2]]).add_to(loc)
folium.Marker(location = [dff.iloc[31, 5], dff.iloc[31, 4]], icon = folium.Icon(color='green', icon='plane')).add_to(loc)
folium.Marker(location = [dff.iloc[30, 5], dff.iloc[30, 4]], icon = folium.Icon(color='green', icon='plane')).add_to(loc)
for i in range(len(x)):
    folium.Marker(location=[y[i], x[i]], icon = folium.Icon(color='orange', icon='star')).add_to(loc)

    
loc.save('./html/강원관광대학교.html')