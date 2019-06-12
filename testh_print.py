import csv
#coding=utf-8
my_file = csv.reader(open('./data/login_data.csv', 'r', encoding='utf-8'))
list = []
for data in my_file:
    list.append(data)
print(list[1][0]+list[1][1]+list[1][2])