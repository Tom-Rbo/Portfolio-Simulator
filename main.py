import datetime

from stock import Stock
from transaction import Transaction
from portfolio import Portfolio

# Test stock class
print("Stock class test :\n")

tsla = Stock("TSLA")
lvmh = Stock("MC.PA")

print(tsla)
tsla.info()

print(lvmh)
lvmh.info()

print(100*"*")
# Test transaction class
print("Transaction class test :\n")

t1 = Transaction(tsla, 10, datetime.datetime(2025, 1, 13), 1)  # Buy 10 share of tsla on 1st january 2025
t2 = Transaction(lvmh, 10, datetime.datetime(2025, 1, 13), -1) # Sell 10 share of lvmh on 1st january 2025

print(t1)
print(t2)

print(100*"*")
# Test portfolio class
print("Portfolio class test :\n")

portfolio = Portfolio(10000)

t3 = Transaction(tsla, 10, datetime.datetime(2025, 2, 13), -1)  # Sell 10 share of tsla on 1st january 2025
t4 = Transaction(lvmh, 10, datetime.datetime(2025, 1, 13), 1) # Buy 10 share of lvmh on 1st january 2025

portfolio.add_transaction(t1)
portfolio.add_transaction(t3)
portfolio.add_transaction(t4)

print(portfolio)


