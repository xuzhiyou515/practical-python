
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    
    def cost(self):
        return self.shares*self.price

    def sell(self, sell_shares):
        if self.shares < sell_shares:
            raise RuntimeError(f"Cannot sell more than {self.shares:d}")
        self.shares -= sell_shares