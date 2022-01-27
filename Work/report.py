# report.py
#
# Exercise 2.4
import csv
def read_portfolio(filename):
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    portfolio = []
    for row in rows:
        holding = row[0], int(row[1]), float(row[2])
        portfolio.append(holding)
    return portfolio

portfolio = read_portfolio('Data\portfolio.csv')
print(portfolio)
