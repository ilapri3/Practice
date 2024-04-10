import csv

data_csv = [['Gena','22','student'],['Andrew','43','manager'],['Vova','35','worker']]
dict = {}

with open('main.csv', 'r', encoding = 'UTF-8') as file:
    csv_r = csv.reader(file)
    data_csv_r = [*csv_r]

for i in range(len(data_csv)):
    dict = {f'столбец {i+1}':type(data_csv[0][i])}
    print(dict)