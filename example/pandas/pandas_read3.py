import pandas as pd
corona = pd.read_csv("./data/csv/corona.csv", thousands = ',')

print('인구수', format(corona["인구수"].sum(), ','))
print('확진자', format(corona["확진자"].sum(), ','))
print('치료중', format(corona["치료중"].sum(), ','))
print('사망자', format(corona["사망자"].sum(), ','))

