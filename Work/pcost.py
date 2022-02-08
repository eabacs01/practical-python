# pcost.py
#
# Exercise .30
# def portfolio_cost(filename):   
#     total_cost = 0
#     with open(filename, 'rt') as f:
#         next(f)
#         for line in f:
#             _, numshares, price = tuple(line.split(','))
#             total_cost += int(numshares) * float(price)
#     return total_cost

# import sys # ex 1.33
# # Exercise 1.32
# import csv
# def portfolio_cost(filename):
#     f = open(filename)
#     rows = csv.reader(f)
#     headers = next(rows)
#     total_cost = 0
#     for rownum, row in enumerate(rows):
#         # Exercise 2.15 - try/except block
#         try:
#             total_cost += int(row[1]) * float(row[2])
#         except ValueError:
#             print(f'Row {rownum}: couldn\'t convert: {row}')
#     return total_cost

# if len(sys.argv)==2:
#     filename = sys.argv[1]
# else:
#     filename = 'Data\portfolio.csv'

# cost = portfolio_cost(filename)
# print(f'Total cost: {cost: 10.2f}')

# Exercise 2.16
# import csv
# def portfolio_cost(filename):
#     f = open(filename)
#     rows = csv.reader(f)
#     headers = next(rows)
#     total_cost = 0
#     for rownum, row in enumerate(rows, start=1):
#         holding = dict(zip(headers, row))
#         try:
#             numshares = int(holding['shares'])
#             price = float(holding['price'])
#             total_cost += numshares * price
#         except ValueError:
#             print(f'Row {rownum}: couldn\'t convert: {row}')
#     return total_cost

# Exercise 3.14
import sys
import report

def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)
    return sum(holding.cost for holding in portfolio)

def main(args):
    if len(args) != 2:
        raise SystemExit(f'Usage: {args[0]} ' 'portfile')
    print(f'Total cost: {portfolio_cost(args[1]):10.2f}')

# Run main from the command line prompt
if __name__ == '__main__':
    main(sys.argv)