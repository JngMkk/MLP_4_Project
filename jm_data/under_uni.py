# 정부재정지원제한대학(부실대학) 기준인 신입생 충원율 97% 미만, 재학생 충원율 86% 미만 대학
import pandas as pd

datas = ['uni_freshman_2019', 'uni_freshman_2020', 'uni_freshman_2021']
freshman_total = [] #총 대학 수(신입생 기준)
freshman_under = [] #미달 대학 수(신입생 기준)
freshman_rate = [] #미달 대학 비율(신입생 기준)

for data in datas:
    df = pd.read_csv(f'./data/{data}.csv', index_col=0)
    freshman_total.append(len(df)) #총 대학 수 입력

    df = df[df.iloc[:, [11]].values < 97]
    freshman_under.append(len(df)) #미달 대학 수 입력
    df = df.reset_index(drop=True)

    df.to_csv(f'./data/under_{data}.csv')




datas = ['uni_students_2019', 'uni_students_2020', 'uni_students_2021']
not_f_total = [] # 총 대학 수(재학생 기준)
not_f_under = [] # 미달 대학 수(재학생 기준)
not_f_rate = [] #미달 대학 비율(재학생 기준)

for data in datas:
    df = pd.read_csv(f'./data/{data}.csv', index_col=0)
    not_f_total.append(len(df)) # 총 대학 수 입력

    df = df[df.iloc[:, [11]].values < 86]
    not_f_under.append(len(df)) # 미달 대학 수 입력
    df = df.reset_index(drop=True)


    df.to_csv(f'./data/under_{data}.csv')


for i in range(3):  #19, 20, 21년도의 미달대학 비율 입력
    freshman_rate.append(freshman_under[i]/freshman_total[i])
    not_f_rate.append(not_f_under[i]/not_f_total[i])



rate_df = pd.DataFrame({'신입생 기준 미달대학':freshman_rate, '재학생 기준 미달대학': not_f_rate}, index=[2019, 2020, 2021])
rate_df.to_csv(f'./data/under_rate.csv')


