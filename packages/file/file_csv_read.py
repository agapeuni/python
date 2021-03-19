import csv

with open("data/example1.csv", 'r', encoding='utf-8') as f1:
    csv_reader = csv.reader(f1, delimiter=',', quotechar='|')
    for row in csv_reader:
        print(row)
print()

with open("data/example2.csv", 'r', encoding='utf-8') as f2:
    csv_reader = csv.reader(f2, delimiter=',', quotechar='|')
    for row in csv_reader:
        print(row)
