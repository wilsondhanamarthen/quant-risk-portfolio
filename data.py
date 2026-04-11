import yfinance as yf
import numpy as np
TICKERS = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'SPY']
START = '2010-01-01'
END = "2025-01-01"

def get_prices():
    data = yf.download(TICKERS, start=START, end=END, auto_adjust=True)
    prices = data['Close']
    return prices

def get_returns(prices):
    returns = np.log(prices / prices.shift(1)).dropna()
    return returns


    