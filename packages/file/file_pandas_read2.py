import pandas as pd

corona = pd.read_csv("data/corona.csv")

print(corona["인구수"].sum())