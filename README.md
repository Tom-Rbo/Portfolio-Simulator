Portfolio Simulator  

**Overview**  
This project is a Python-based portfolio simulator designed to model investment portfolios. It provides tools to manage stocks, track transactions, and evaluate portfolio performance over time.

**Project Objectives**  
- Stock Management: Create and manage stock objects with relevant attributes.
- Transaction Handling: Record and process buy/sell transactions for various stocks.
- Portfolio Analysis: Aggregate stock data and transactions to assess overall portfolio performance.

**Tools & Technologies**
- Python (Pandas, NumPy, yfinance)
- API
- Object-Oriented Programming

**Project Structure**  
- main.py: The main script to run simulations and interact with the portfolio.
- stock.py: Contains the Stock class, representing individual stock entities with their properties.
- transaction.py: Manages the Transaction class, detailing buy/sell operations on stocks.
- portfolio.py: Defines the Portfolio class, encapsulating a collection of stocks and their associated transactions.

Disclaimer  
We assume that each stock have the same currency.
If a transaction append during a non-trading day, we use the next valid day to assess the transaction price.

Improvements & Future Work  
- Consider currencies for each stock
