import csv
import matplotlib.pyplot as ptl 
def dot_graph():
    all_year = []
    years_data = []
    outcome_money = []
    income_money = []
    debt_money = []
    years = (2539,2543,2545,2547,2549,2550,2552,2554,2556)
    for i in years:
        name_file = "data%d.txt"%i
        file=open(name_file, 'rt')
        data=csv.reader(file, delimiter=',')
        table=[[i] + row for row in data]
        all_year += table
    print(all_year[:])
    name = input()
    for num in all_year:
        if num[1] == str(name):
            years_data.append(num[0])
            outcome_money.append(num[2])
            income_money.append(num[3])
            debt_money.append(num[4])
    p1 = ptl.plot(years_data, outcome_money, 'rs-')
    p2 = ptl.plot(years_data, income_money, 'bs-')
    p3 = ptl.plot(years_data, debt_money, 'gs-')
    ptl.legend((p1[0], p2[0], p3[0]), ("outcome", "income", "Debt"))
    ptl.title("Different of Outcome, Income and Debt in " + name)
    ptl.xlabel("Province")
    ptl.ylabel("Amout of money in Baht")
    ptl.show()
dot_graph()
