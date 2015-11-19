import csv
file=open('data.txt', 'rt')
data=csv.reader(file)
for i in data:
    if len(i) == 1:
        print(i[0])
    else:
        print(i[0]+i[1])
