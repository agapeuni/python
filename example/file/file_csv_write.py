import csv

items1 = [
    ['2020-09-08', '서울경기', '23.1', '20.7', '26.1'],
    ['2020-09-09', '서울경기', '20.5', '18.3', '24.7'],
    ['2020-09-10', '서울경기', '22.2', '18.2', '26.5'],
    ['2020-09-11', '서울경기', '22.1', '19.1', '26.6'],
    ['2020-09-12', '서울경기', '19.9', '17.8', '22.3']
]
with open('data/example1.csv', 'w', encoding='utf-8', newline='') as f1:
    csv_writer1 = csv.writer(f1)
    for item in items1:
        csv_writer1.writerow(item)

items2 = [
    ['1', '한국', 'Korea'],
    ['2', '중국', 'China'],
    ['3', '미국', 'America'],
    ['4', '독일', 'Germany'],
    ['5', '일본', 'Japan']
]
with open('data/example2.csv', 'w', encoding='utf-8', newline='') as f2:
    csv_writer2 = csv.writer(f2)
    for item in items2:
        csv_writer2.writerow(item)
