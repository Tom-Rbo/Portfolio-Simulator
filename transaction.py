import yfinance as yf
from stock import Stock
import datetime
import warnings

class Transaction:
    def __init__(self, stock: Stock, quantity: float, date: datetime.datetime, side: int):
        if side not in (1, -1):
            raise ValueError("side must be 1 (buy) or -1 (sell)")

        self.stock = stock
        self.quantity = quantity
        self.original_date = date  # Keep the requested date for reference
        self.side = side

        # Try up to 5 days ahead to find a valid trading day
        self.price = None
        for i in range(5):
            check_date = date + datetime.timedelta(days=i)
            history = yf.Ticker(stock.ticker).history(start=check_date, end=check_date + datetime.timedelta(days=1))
            
            if not history.empty:
                self.price = history["Close"].iloc[0]
                self.date = check_date  # Use the actual trading date
                break

        if self.price is None:
            raise ValueError(f"No trading data found for {stock.ticker} within 5 days from {date.date()}")

    def __str__(self):
        action = "BUY" if self.side == 1 else "SELL"
        return (
            f"{action} {self.quantity} of {self.stock.ticker} "
            f"at {self.price:.2f} on {self.date.date()}"
            + (f" (requested {self.original_date.date()})" if self.date != self.original_date else "")
        )
