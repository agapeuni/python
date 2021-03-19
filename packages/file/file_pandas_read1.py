import pandas as pd

corona = pd.read_csv("data/corona.csv")
print(type(corona))
print(corona)
print()

print(type(corona["인구수"]))
print(corona["인구수"])