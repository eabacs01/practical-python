# report.py
#
import sys
from fileparse import parse_csv
from stock import Stock
from tableformat import create_formatter 

def read_portfolio(filename):
    '''
    Read in a portfolio from a csv file
    Input: filename of csv file with headers in first row 
    Output: List of dictionaries of holdings in the portfolio
            Every holding has least these enties: name, shares & price
    '''
    with open(filename, 'rt') as f:
        portdicts = parse_csv(f, select=['name', 'shares', 'price'], types=[str, int, float])
    return [Stock(s['name'], s['shares'], s['price']) for s in portdicts]

def read_prices(filename):
    '''
    Read prices from a csv file
    Input: CSV filename, no headers, just two fields per line: name and price
    Output: dict of names and prices
    '''
    # read in prices and get list of tuples
    with open(filename, 'rt') as f:
        prices = parse_csv(f, types = [str, float], has_headers=False)
    return dict(prices)

def make_report(portfolio, prices):
    '''
    Takes a portfolio and prices file and produces a rpeort of the holdings with the original price and gain/loss in price
    '''
    report=[]
    for holding in portfolio:
        report_line = holding.name, holding.shares, prices[holding.name], prices[holding.name] - holding.price
        report.append(report_line) 
    return report

def print_report(reportdata, formatter):
    '''
    Print out a formatted report from list of (name, shares, price, price change) tuples
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ] 
        formatter.row(rowdata)

def portfolio_report(portfname, pricefname, fmt='txt'):
    '''Read in a portfolio file and prices file and produce a report & print it'''
    portfolio = read_portfolio(portfname)
    prices = read_prices(pricefname)
    report = make_report(portfolio, prices)
    #Print out report
    formatter = create_formatter(fmt)
    print_report(report, formatter)
    # return report

# Exercise 3.15
def main(args):
    if len(args) != 4:
        raise SystemExit(f'Usage: {args[0]} ' 'portfile pricefile')
    portfile = args[1]
    pricefile = args[2]
    fmt = args[3]
    portfolio_report(portfile, pricefile, fmt)

# Run main from the command line prompt
if __name__ == '__main__':
    main(sys.argv)