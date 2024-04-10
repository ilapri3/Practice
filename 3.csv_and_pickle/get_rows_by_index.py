import csv

with open('main.csv', 'r', encoding = 'UTF-8') as file:
    csv_r = csv.reader(file)
    data_csv_r = [*csv_r]

for index, cell in enumerate(data_csv_r):
    print(index, *cell)