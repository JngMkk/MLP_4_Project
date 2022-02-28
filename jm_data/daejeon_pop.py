import pandas as pd

all_df = pd.read_csv('./resources/전국.csv', encoding='cp949')
dae_df = pd.read_csv('./resources/대전.csv', encoding='cp949')

all_c_ratio = round(int(all_df.loc[0][3].replace(',', '')) / int(all_df.loc[0][2].replace(',','')), 3)
all_st_ratio = round((int(all_df.loc[0][3].replace(',', '')) + int(all_df.loc[0][4].replace(',',''))) / int(all_df.loc[0][2].replace(',', '')) ,3)
dae_c_ratio = round(int(dae_df.loc[0][3].replace(',', '')) / int(dae_df.loc[0][2].replace(',','')), 3)
yu_c_ratio = round(int(dae_df.loc[4][3].replace(',', '')) / int(dae_df.loc[4][2].replace(',','')), 3)
dae_st_ratio = round((int(dae_df.loc[0][3].replace(',', '')) + int(dae_df.loc[0][4].replace(',',''))) / int(dae_df.loc[0][2].replace(',', '')) ,3)
yu_st_ratio = round((int(dae_df.loc[4][3].replace(',', '')) + int(dae_df.loc[4][4].replace(',',''))) / int(dae_df.loc[4][2].replace(',', '')) ,3)
