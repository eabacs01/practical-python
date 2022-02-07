# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(lines, select=None, types=None, has_headers = True, delimiter=',', silence_errors = False):
    '''Parse iterable of CSV entries into a list of records/dicts'''
    # Error checking of inputs
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    #Turn rows into an iterable
    rows = csv.reader(lines, delimiter = delimiter)
    
    # Get the headers if there are any
    headers = next(rows) if has_headers else []
    
    # get indices of selected fields
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select

    records = []
    for rownum, row in enumerate(rows, start=1):
        # skip if blank row
        if not row:
            continue
        
        # pick out the fields according to the matching indices to select
        if select:
            row = [row[index] for index in indices]
        
        # convert the fields according to types
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as v:
                if not silence_errors:  
                    print(f'Row {rownum}: Couldn\'t convert {row}')
                    print(f'Row {rownum}: Reason {v}')                        
        
        # make the record and append it
        if headers:
            # Headers - put values into list dictionaries
            record = dict(zip(headers, row))
        else:
            # No headers - put values into list of tuples 
            record = tuple(row)
        records.append(record)
    # Return the list of dicts/tuples
    return records
