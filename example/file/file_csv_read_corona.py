import csv

tot_population = 0
tot_corona19 = 0
tot_be_care = 0
tot_death = 0

with open("data/corona.csv", 'r', encoding='utf-8') as f:
    data = csv.reader(f)
    next(data) # Header 넘기기
    for row in data:
        tot_population = tot_population + int(row[8].replace(',', ''))
        tot_corona19 = tot_corona19 + int(row[1].replace(',', ''))
        if row[2] != '':
            tot_be_care = tot_be_care + int(row[2].replace(',', ''))
        tot_death = tot_death + int(row[3].replace(',', ''))

print('인구수', format(tot_population, ','))
print('확진자', format(tot_corona19, ','))
print('치료중', format(tot_be_care, ','))
print('사망자', format(tot_death, ','))

