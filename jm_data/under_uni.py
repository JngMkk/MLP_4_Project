# 정부재정지원제한대학(부실대학) 기준인 신입생 충원율 97% 미만, 재학생 충원율 86% 미만 대학
import pandas as pd

datas = ['uni_freshman_2019', 'uni_freshman_2020', 'uni_freshman_2021']

for data in datas:
    df = pd.read_csv(f'./data/{data}.csv', index_col=0)
    df[df.iloc[:, [11]].values < 97].to_csv(f'./data/under_{data}.csv')

datas = ['uni_students_2019', 'uni_students_2020', 'uni_students_2021']
for data in datas:
    df = pd.read_csv(f'./data/{data}.csv', index_col=0)
    df[df.iloc[:, [11]].values < 86].to_csv(f'./data/under_{data}.csv')