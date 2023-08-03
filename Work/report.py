# report.py
#
# Exercise 2.4
import csv
from price import read_prices
def read_portfolio_as_list(filename):
    '''Read portfolio info from a csv format file'''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            try:
                portfolio.append((row[0], int(row[1]), float(row[2])))
            except ValueError:
                print('Error Format: ', row)
    return portfolio

def read_portfolio_as_dict(filename):
    '''Read portfolio info from a csv format file'''
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers=next(rows)
        select=['name','shares','price']
        indices=[headers.index(colname) for colname in select]
        try:
            portfolio=[{colname: row[index] if colname=='name' else int(row[index]) if colname=='shares' else float(row[index]) for colname, index in zip(select, indices)} for row in rows]
        except ValueError:
            print('Error Format: ', row)
    return portfolio

def report_gain_or_loss(portfolioFile, priceFile):
    gain = 0.0
    portfolio = read_portfolio_as_dict(portfolioFile)
    prices = read_prices(priceFile)
    for s in portfolio:
        buymoney = s['price'] * s['shares']
        curmoney = prices[s['name']] * s['shares']
        gain += (curmoney - buymoney)
    return gain

def make_report(portfolio, prices):
    report = []
    for stock in portfolio:
        price = prices[stock['name']]
        item = (stock['name'], stock['shares'], price, price - stock['price'])
        report.append(item)
    return report

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    sep = ''
    print(f'{sep:->10s} {sep:->10s} {sep:->10s} {sep:->10s}')
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')

portfolio = read_portfolio_as_dict('Data/portfoliodate.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio,prices)
print_report(report)