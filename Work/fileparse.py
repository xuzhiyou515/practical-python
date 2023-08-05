# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(file, select=None, types=None, has_headers=True, delimiter=',',slience_errors=False):
    '''
    Parse a CSV file into a list of records
    '''
    if not has_headers and select:
        raise RuntimeError('select argument requires column headers')
    rows = csv.reader(file, delimiter=delimiter)
    if has_headers:
        headers=next(rows)
        if select:
            indices=[headers.index(colname) for colname in select if colname in headers]
            headers= [colname for colname in select if colname in headers]
        else:
            indices=[]
    records=[]
    for i, row in enumerate(rows,start=1):
        if not row:
            continue
        if has_headers:
            if indices:
                row = [row[index] for index in indices]
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not slience_errors:
                    print(f'Row {i:d}: ', row)
                    print(f'Row {i:d}: ',e)
                continue
        if has_headers:
            record=dict(zip(headers,row))
        else:
            record=tuple(row)
        records.append(record)
    return records