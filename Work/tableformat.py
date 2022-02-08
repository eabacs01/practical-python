#tableformat.py
#

# Exercise 4.5
class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()
    
class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()
        
class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))
        
class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print('<tr><th>' + '</th><th>'.join(headers) + '</th></tr>')

    def row(self, rowdata):
        print('<tr><td>' + '</td><td>'.join(rowdata) + '</td></tr>')
        
#Exercise 4.11
class FormatError(Exception):
    pass

#Exercise 4.7
def create_formatter(fmt):
    if fmt == 'txt':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown formatter type: {fmt}')

# Exercise 4.10
def print_table(objlist, select=None, formatter=None):
    '''
    Print out table formatted according to selected tableformat type
    '''
    if not select:
        raise ValueError('Usage: select = list of attributes/properties not empty')
    if not formatter:
        raise ValueError('Usage: formatter = instance of tableformat class')
    
    formatter.headings(select)
    for obj in objlist:
        rowdata = [ str(getattr(obj, selitem)) for selitem in select ] 
        formatter.row(rowdata)
