# report.py
#
import sys
from fileparse import parse_csv

def read_portfolio(filename):
    '''
    Read in a portfolio from a csv file
    Input: filename of csv file with headers in first row 
    Output: List of dictionaries of holdings in the portfolio
            Every holding has least these enties: name, shares & price
    '''
    portfolio = parse_csv(filename, select=['name', 'shares', 'price'], types=[str, int, float])
    return portfolio

def read_prices(filename):
    '''
    Read prices from a csv file
    Input: CSV filename, no headers, just two fields per line: name and price
    Output: dict of names and prices
    '''
    # read in prices and get list of tuples
    prices = parse_csv(filename, types = [str, float], has_headers=False)
    return dict(prices)

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
    # return report

# Exercise 3.15
def main(args):
    if len(args) != 3:
        raise SystemExit(f'Usage: {args[0]} ' 'portfile pricefile')
    portfile = args[1]
    pricefile = args[2]
    portfolio_report(portfile, pricefile)

# Run main from the command line prompt
if __name__ == '__main__':
    main(sys.argv)