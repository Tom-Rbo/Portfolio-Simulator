import yfinance as yf

class Stock:
    def __init__(self, ticker: str):
        self.ticker = ticker.upper()

        info = yf.Ticker(self.ticker).info

        self.name = info.get("shortName", "N/A")
        self.currency = info.get("currency", "USD")
        self.sector = info.get("sector", "N/A")
        self.current_price = info.get("regularMarketPrice", 0.0)

    def __str__(self) -> str:
        return f"{self.name}"
    
    def info(self):
        print(f"{self.name} {self.ticker} \n" +
        f"Sector: {self.sector} | Current Price: {self.current_price} {self.currency}")
        