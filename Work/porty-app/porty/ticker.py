# ticker.py
#

from .follow import follow
import csv

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [ func(val) for func, val in zip(types, row) ]

def make_dicts(rows, headers):
    return (dict(zip(headers, row)) for row in rows)

def filter_symbols(rows, names):
     return (row for row in rows if row['name'] in names)

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def ticker(portfile, logfile, fmt):
    from report import read_portfolio
    from tableformat import create_formatter
    
    formatter = create_formatter(fmt)

    portfolio = read_portfolio(portfile)
    lines = follow(logfile)
    rows = parse_stock_data(lines)
    rows = filter_symbols(rows, portfolio)

    formatter.headings(['Name', 'Price', 'Change'])
    for row in rows:
        rowdata = ( str(row[colname]) for colname in ['name', 'price', 'change'] ) 
        formatter.row(rowdata)

    def main(args):
        if len(args) != 4:
            raise SystemExit('Usage: %s portfoliofile logfile fmt' % args[0])
        else:
            ticker(args[1], args[2], args[3])
    
    if __name__ == '__main__':
        import sys
        main(sys.argv)
