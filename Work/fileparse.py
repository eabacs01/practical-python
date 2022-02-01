# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, delimiter=',', select=[], types=[], has_headers = True):
    '''Parse a CSV file into a list of records/dicts'''
    with open(filename, 'r') as f:
        rows = csv.reader(f, delimiter = delimiter)
        if has_headers:
            headers = next(rows)
            # get indices of selected fields
            if select:
                indices = [headers.index(colname) for colname in select]
                headers = select
            else:
                indices = []
            records = []
            for row in rows:
                # skip if blank row
                if not row:
                    continue
                # pick out the fields according to the matching indices to select
                if indices:
                    row = [row[index] for index in indices]
                # convert the fields acording to types
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                # make the record and append it
                record = dict(zip(headers, row))
                records.append(record)
        else:
            records = []
            for row in rows:
                # skip if blank row
                if not row:
                    continue
                # convert the fields acording to types
                if types:
                    row = [func(val) for func, val in zip(types, row)]
                record = tuple(row)
                records.append(record)
    return records
