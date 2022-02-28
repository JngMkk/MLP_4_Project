import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('./resources/Export.xlsx')

row = []
for i, r in df.iterrows():
    if r['방문객구분'] == '외부방문자(b+c)':
        row.append([r[i] for i in range(len(r)-2)])

df = pd.DataFrame(row, columns=['연도', '지역명', '방문객구분', '방문객수'])
del df['방문객구분']
df['연도'] = df['연도'].astype('int')

x = [2018, 2019, 2020, 2021]
y1 = list(map(lambda x: x/1000000,df[df['지역명'] =='태백시']['방문객수']))
y2 = list(map(lambda x: x/1000000,df[df['지역명'] =='삼척시']['방문객수']))
y3 = list(map(lambda x: x/1000000,df[df['지역명'] =='정선군']['방문객수']))
y4 = list(map(lambda x: x/1000000,df[df['지역명'] =='영월군']['방문객수']))
plt.figure(figsize=(10,8))
plt.plot(x, y1, c='red', label='태백시')
plt.plot(x, y2, c='blue', label='삼척시')
plt.plot(x, y3, c='green', label='정선군')
plt.plot(x, y4, c='black', label='영월군')
plt.text(2020.5, 5, '태백시')
plt.text(2020.5, 6, '영월군')
plt.text(2020.5, 7, '정선군')
plt.text(2020.5, 11, '삼척시')
plt.title('연도별 지역 관광객 수')
plt.xticks(x)
plt.ylim((3, 15))
plt.xlabel('연도')
plt.ylabel('관광객 수(단위 : 백만)')
plt.legend()
plt.savefig('./data/관광객 수.png')
