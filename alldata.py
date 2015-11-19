import csv
file=open('data2543.txt', 'rt')
data=csv.reader(file)
for i in data:
    print(i.split())
