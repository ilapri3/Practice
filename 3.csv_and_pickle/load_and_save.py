import csv
import pickle

data_csv = [['Gena','22','student'],['Andrew','43','manager'],['Vova','35','worker']]
data_txt = ['Some text 1','Some text 2','Some text 3']

class Table:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        return f'My name is {self.name}, I am {self.age} years old'

inf = Table('Kirill','19')

#save_table_csv
with open('main.csv', 'w', encoding = 'UTF-8') as file:
    csv_w = csv.writer(file)
    for el in data_csv:
        csv_w.writerow(el)

#load_table_csv
with open('main.csv', 'r', encoding = 'UTF-8') as file:
    csv_r = csv.reader(file)
    data_csv_r = [*csv_r]
print(data_csv_r)
print('---------')

# #save_table_pickle
# with open('main.pickle', 'wb') as file:
#      pickle.dump(inf, file)

# #load_table_pickle
# with open('main.pickle', 'rb') as file:
#     data_pickle = pickle.load(file)
# print(data_pickle)
# print('---------')

# #save_table_txt
# with open('main.txt', 'w', encoding = 'UTF-8') as file:
#     file.write('\n'.join(data_txt))

# #load_table_txt
# with open('main.txt', 'r', encoding = "UTF-8") as file:
#     data_txt_r = file.read()
# print(data_txt_r)