import csv
start = 0
end = 1

with open('main.csv', 'r', encoding = 'UTF-8') as file:
    csv_r = csv.reader(file)
    data_csv_r = [*csv_r]

print(data_csv_r[start:end])