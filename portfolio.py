import numpy as np
import pandas as pd
from stock import Stock
from transaction import Transaction
from collections import defaultdict


class Portfolio:
    def __init__(self, initial_cash: float):
        self.history = pd.DataFrame(columns=['date', 'transaction date', 'stock', 'quantity', 'price', 'side'])
        self.cash = initial_cash
        self.positions = defaultdict(int)

    def add_transaction(self, transaction: Transaction):
        ticker = transaction.stock.ticker
        qty = transaction.quantity
        price = transaction.price
        side = transaction.side

        cost = qty * price * side * -1

        if side == 1 and self.cash < qty * price:
            raise ValueError(f"Not enought cash for this transaction\n" + 
                             f"Portfolio cash: {self.cash}, Cost: {qty * price}, diff: {qty * price - self.cash }")
        if side == -1 and self.positions[ticker] < qty:
            raise ValueError(f"Not enought stock to sell\n" +
                            f"Stock available: {self.positions[ticker]}, Number of stock to sell: {qty}, diff: {self.positions[ticker] - qty} ") 
        
        # Update status of portfolio
        self.cash += cost
        self.positions[ticker] += qty * side

        # Add transacation to history
        self.history.loc[len(self.history)] = [transaction.original_date, transaction.date, transaction.stock, qty, price, side]

    def portfolio_value(self):
        asset = 0
        for ticker, qty in self.positions.items():
            asset += qty * Stock(ticker).current_price
        return asset
    
    def __str__(self):
        asset = self.portfolio_value()
        total = asset + self.cash
        return (f"Portfolio value: {total:.2f} = {self.cash:.2f} (cash) + {asset:.2f} (asset)\n" +
                f"Positions:\n{dict(self.positions)}\n" + 
                f"History:\n{self.history}")
