import os
import pandas as pd

f_lst = os.listdir('./data/')
lst = [x for x in f_lst if '1km내' in x]

for ls in lst:
    df = pd.read_csv(f'./data/{ls}', index_col=0)
    name = df.index.name
    for i, row in df.iterrows():
        df['배차간격'][i] = row['배차간격'].split('현')[0]
        df['버스'][i] = str(row['버스']).split('(')[0].replace(' ', '')
    bus = []
    time_d = []
    subway = []
    for _, row in df.iterrows():
        if row['버스'] in bus:
            pass
        else:
            bus.append(row['버스'])
            time_d.append(row['배차간격'])
            subway.append(row['지하철역'])

    df_r = pd.DataFrame([bus, time_d, subway]).T
    df_r.columns = ['버스', '배차간격', '지하철역']
    df_r.index.name = df.index.name
    df_r.to_csv(f'./data/{name}1km내버스,지하철.csv', encoding='utf-8')