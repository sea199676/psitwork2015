import csv
import plotly.plotly as py
import plotly.graph_objs as go
py.sign_in('sea199676', 'vrmlh14j43')
years = 2543
name_file = "data%d.txt"%years
file=open(name_file, 'rt')
data=csv.reader(file)
table=[row for row in data]
province = [name for [name, outcome, income, debt] in table]
outcome_money = [int(outcome) for [name, outcome, income, debt] in table]
income_money = [int(income) for [name, outcome, income, debt] in table]
debt_money = [int(debt) for [name, outcome, income, debt] in table]
outcome = go.Bar(x=province, y=outcome_money, name="Outcome")
income = go.Bar(x=province, y=income_money, name="Income")
debt = go.Bar(x=province, y=debt_money, name="Debt")
data = [outcome, income, debt]
layout = go.Layout(barmode='group')
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='grouped-bar')
