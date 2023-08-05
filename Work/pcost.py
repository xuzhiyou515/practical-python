# pcost.py
#
# Exercise 1.27
import sys
from report import read_portfolio_as_dict

def portfolio_cost(filename):
    total_cost = 0.0
    portfolio = read_portfolio_as_dict(filename)
    for s in portfolio:
        total_cost += s['shares'] *s['price']
    return total_cost
def main(argv):
    cost = portfolio_cost(argv[1])
    print(f"Total cost {cost}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(f'Usage: {sys.argv[0]:s} portfoliofile')
    else:
        main(sys.argv)