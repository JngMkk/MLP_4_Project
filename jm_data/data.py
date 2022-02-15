import pandas as pd

def file_sort(file):
    df = pd.read_excel(f'./resources/{file}.xlsx')
    df = df.iloc[2:, [0,1,2,3,4,5,6,8,11,14,15,18,19]]
    df.columns = ['기준년도', '학교종류', '설립구분', '지역', '상태', '학교', '입학정원', '정원내(모집인원)', '정원내(지원자)', '정원내 입학자(남)', '정원내 입학자(여)', '정원내 신입생 충원율(정원내 입학자/정원내 모집인원)', '경쟁률(정원내 지원자/정원내 모집인원)']
    df = df.loc[5:]
    df.reset_index(drop=True, inplace=True)
    df.to_csv(f'./data/{file}.csv')

yrs = ['uni_2019', 'uni_2020', 'uni_2021']
for yr in yrs:
    file_sort(yr)