import csv
import matplotlib.pyplot as ptl 
def dot_graph():
    """make a dot graph use data from text file"""
    years = int(input())
    name_file = "data%d.txt"%years
    file=open(name_file, 'rt')
    data=csv.reader(file)
    table=[row for row in data]
    print(table[:])
    province = [name for [name, outcome, income, debt] in table]
    outcome_money = [outcome for [name, outcome, income, debt] in table]
    income_money = [income for [name, outcome, income, debt] in table]
    debt_money = [debt for [name, outcome, income, debt] in table]
    number_province = [num for num in range(1, 78)]
    p1 = ptl.plot(number_province, outcome_money, 'rs-')
    p2 = ptl.plot(number_province, income_money, 'bs-')
    p3 = ptl.plot(number_province, debt_money, 'gs-')
    ptl.legend((p1[0], p2[0], p3[0]), ("outcome", "income", "Debt"))
    ptl.title("Total income, outcome and dept in every province in Thailand %d"%years)
    ptl.xlabel("Province")
    ptl.ylabel("Amout of money in Baht")
    ptl.show()
dot_graph()

    
        


