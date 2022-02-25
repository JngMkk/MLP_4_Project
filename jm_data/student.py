import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./data/student_data.csv', encoding='cp949')
data = data.loc[26:29]
del data['가정별']
data.reset_index(drop=True, inplace=True)
data.rename(columns={'인구종류별':'학령인구'}, inplace=True)
data['학령인구'][0] = '초등학생'
data['학령인구'][1] = '중학생'
data['학령인구'][2] = '고등학생'
data['학령인구'][3] = '대학생'
data.set_index('학령인구', inplace=True)
data = data.transpose()
plt.style.use('ggplot')
ax = data.plot(stacked=True, kind='bar', figsize = (14,10), rot='horizontal')
for rect in ax.patches:
    height = rect.get_height()
    width = rect.get_width()
    x = rect.get_x()
    y = rect.get_y()
    label_text = f'{int(height)}'
    label_x = x + width / 2
    label_y = y + height / 2
    if height > 0:
        ax.text(label_x, label_y, label_text, ha = 'center', va = 'center', fontsize = 12)

ax.legend(bbox_to_anchor=(1.0, 1), loc='upper left', borderaxespad=0., fontsize=10) 
ax.set_title('학령인구', fontsize = 20)
ax.set_xlabel("연도", fontsize = 16)
plt.savefig('./data/학령인구.png')