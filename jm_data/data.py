# 데이터 전처리

import pandas as pd

def file_sort(file):
    df = pd.read_excel(f'./resources/{file}.xlsx')
    df = df.iloc[2:, [0,1,2,3,4,5,6,8,11,14,15,18,19]]
    df.columns = ['기준년도', '학교종류', '설립구분', '지역', '상태', '학교', '입학정원', '정원내(모집인원)', '정원내(지원자)', '정원내 입학자(남)', '정원내 입학자(여)', '정원내 신입생 충원율(정원내 입학자/정원내 모집인원)', '경쟁률(정원내 지원자/정원내 모집인원)']
    df = df.loc[5:]
    df.reset_index(drop=True, inplace=True)
    df.to_csv(f'./data/{file}.csv')

def file_sort2(file):
    df = pd.read_excel(f'./resources/{file}.xlsx', header=4)
    df = df.iloc[:,[0,1,2,3,4,5,6,7,8,9,10,11,12]]
    df.columns = ['기준연도', '학교종류', '설립구분', '지역', '상태', '학교', '학생정원', '학생모집정지인원', '총재학생', '정원내재학생', '정원외재학생', '재학생충원율[총재학생/(학생정원-정지인원)x100]', '정원내학생충원율[정원내재학생/(학생정원-정지인원)x100]']
    df.to_csv(f'./data/{file}.csv')

datas = ['uni_freshman_2019', 'uni_freshman_2020', 'uni_freshman_2021']
for data in datas:
    file_sort(data)

datas = ['uni_students_2019', 'uni_students_2020', 'uni_students_2021']
for data in datas:
    file_sort2(data)