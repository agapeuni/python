import pandas as pd

corona = pd.read_csv("data/corona.csv", thousands=',')

print(corona[["국가", "확진자", "인구수"]].sort_values(
    by=['확진자'], ascending=False).head())
