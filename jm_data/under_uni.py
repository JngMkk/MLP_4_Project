# 정부재정지원제한대학(부실대학) 기준인 충원율 70퍼 미만 대학
import pandas as pd

datas = ['uni_2019', 'uni_2020', 'uni_2021']

for data in datas:
    df = pd.read_csv(f'./data/{data}.csv', index_col=0)
    df[df.iloc[:, [11]].values < 70].to_csv(f'./data/under_{data}')