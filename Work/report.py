# report.py
#
# Exercise 2.5
import csv
def read_portfolio(filename):
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    portfolio = []
    for row in rows:
        holding={}
        holding['name'] = row[0]
        holding['shares'] = int(row[1])
        holding['price'] = float(row[2])
        portfolio.append(holding) 
    return portfolio

p = read_portfolio('Data\portfolio.csv')
port_value0 = sum([s['shares'] * s['price'] for s in p])
print(p)
print(port_value0)

# Exercise 2.6
def read_prices(filename):
    f =  open(filename, 'r')
    rows = csv.reader(f)
    prices={}
    for row in rows:
        try:
            prices[row[0]] = float(row[1])
        except:
            pass
    return prices

prices = read_prices('Data\prices.csv')
# Exercise 2.7
port_value1 = sum([s['shares'] * prices[s['name']] for s in p])
print(prices)
print(port_value1)
print(f'Opening portfolio value: {port_value0:>10.2f}, current value: {port_value1:>10.2f}, gain/loss: {(port_value1 - port_value0):>10.2f}')

#Exercise 2.9
def make_report(portfolio, prices):
    report=[]
    for holding in portfolio:
        report_line = holding['name'], holding['shares'], prices[holding['name']], prices[holding['name']] - holding['price']
        report.append(report_line) 
    return report

#Exercise 2.10, 2.11 & 2.12
def format_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print('---------- ' * 4)
    for name, shares, price, change in report:
        strprice = f'${price:.2f}'
        print(f'{name:>10} {shares: >10d} {strprice: >10s} {change: >10.2f}')

