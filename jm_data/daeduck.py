import pandas as pd
import requests
import folium

df = pd.read_csv('./data/location.csv', index_col=0)

url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={df['y좌표'][6]}%2C{df['x좌표'][6]}&radius=5000&keyword=아파트&language=ko&key="
payload={}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)
res = response.json()
npt = res['next_page_token']
result = res['results']

lat = []
lng = []
for r in result:
    lat.append(r['geometry']['location']['lat'])
    lng.append(r['geometry']['location']['lng'])

for _ in range(20):
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={df['y좌표'][6]}%2C{df['x좌표'][6]}&pagetoken={npt}&radius=5000&keyword=아파트&language=ko&key="
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    res = response.json()
    if 'next_page_token' in res:
        npt = res['next_page_token']
        result = res['results']
        for r in result:
            lat.append(r['geometry']['location']['lat'])
            lng.append(r['geometry']['location']['lng'])
    else:
        result = res['results']
        for r in result:
            lat.append(r['geometry']['location']['lat'])
            lng.append(r['geometry']['location']['lng'])
        break

url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={df['y좌표'][6]}%2C{df['x좌표'][6]}&radius=5000&keyword=연구&language=ko&key="

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

res = response.json()
npt = res['next_page_token']
result = res['results']

lat_2=[]
lng_2=[]
for r in result:
    lat_2.append(r['geometry']['location']['lat'])
    lng_2.append(r['geometry']['location']['lng'])

for _ in range(20):
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={df['y좌표'][6]}%2C{df['x좌표'][6]}&pagetoken={npt}&radius=5000&keyword=아파트&language=ko&key="
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    res = response.json()
    if 'next_page_token' in res:
        npt = res['next_page_token']
        result = res['results']
        for r in result:
            lat_2.append(r['geometry']['location']['lat'])
            lng_2.append(r['geometry']['location']['lng'])
    else:
        result = res['results']
        for r in result:
            lat_2.append(r['geometry']['location']['lat'])
            lng_2.append(r['geometry']['location']['lng'])
        break


loc = folium.Map(location=[df.iloc[6, 3], df.iloc[6, 2]], zoom_start = 13)
folium.Marker(location=[df.iloc[6, 3], df.iloc[6, 2]]).add_to(loc)
if len(lat) < len(lat_2):
    for i in range(len(lat_2)):
        folium.Marker(location=[lat[i], lng[i]], icon = folium.Icon(color='orange', icon='home')).add_to(loc)
        folium.Marker(location=[lat_2[i], lng_2[i]], icon = folium.Icon(color='red', icon='book')).add_to(loc)
else:
    for i in range(len(lat)):
        folium.Marker(location=[lat[i], lng[i]], icon = folium.Icon(color='orange', icon='home')).add_to(loc)
        folium.Marker(location=[lat_2[i], lng_2[i]], icon = folium.Icon(color='red', icon='book')).add_to(loc)
    
loc.save('./html/대덕대학교.html')
    
