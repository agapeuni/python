import pandas as pd

corona = pd.read_csv("./data/csv/corona.csv", thousands = ',')
corona["비율"] = corona["확진자"] / corona["인구수"] * 100

print(corona)
