# report.py
#
from cmath import pi
import csv
def read_portfolio(filename):
    '''
    Read in a portfolio from a csv file
    Input: filename of csv file with headers in first row 
    Output: List of dictionaries of holdings in the portfolio
            Every holding has least these enties: name, shares & price
    '''
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    portfolio = []
    for row in rows:
        holding = dict(zip(headers,row))
        holding['shares'] = int(holding['shares'])
        holding['price'] = float(holding['price'])
        portfolio.append(holding) 
    return portfolio

def read_prices(filename):
    '''
    Read prices from a csv file
    Input: CSV filename, no headers, just two fields per line: name and price
    '''
    f =  open(filename, 'r')
    rows = csv.reader(f)
    prices={}
    for row in rows:
        try:
            prices[row[0]] = float(row[1])
        except:
            pass
    return prices

def make_report(portfolio, prices):
    '''
    Takes a portfolio and prices file and produces a rpeort of the holdings with the original price and gain/loss in price
    '''
    report=[]
    for holding in portfolio:
        report_line = holding['name'], holding['shares'], prices[holding['name']], prices[holding['name']] - holding['price']
        report.append(report_line) 
    return report

def print_report(report):
    '''Print out the report in nice format'''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print('---------- ' * 4)
    for name, shares, price, change in report:
        strprice = f'${price:.2f}'
        print(f'{name:>10} {shares: >10d} {strprice: >10s} {change: >10.2f}')

def portfolio_report(portfname, pricefname):
    '''Read in a ortfolio file and prices file and produce a report & print it'''
    portfolio = read_portfolio(portfname)
    prices = read_prices(pricefname)
    report = make_report(portfolio, prices)
    print_report(report)
    return report
    
    