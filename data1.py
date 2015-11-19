import csv
file=open('data2550.txt', 'rt')
data=csv.reader(file)
table=[row for row in data]
print(table[:])
