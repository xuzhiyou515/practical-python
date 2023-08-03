
import csv

def read_prices(filename):
    '''Read stock prices from a csv format file'''
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                print("IndexError: ", row)
    
    return prices
