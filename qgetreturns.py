# -*- coding: utf-8 -*-
"""qGetReturns.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rBaYTiRYRkd9aowGJiInrxBk9gi5fy9h
"""

import yfinance as yf
import pandas as pd
import numpy as np
def get_stock_data(tickers, start='2020-01-01', end='2020-02-01'):
    data = yf.download(tickers, start=start, end=end)['Close']
    return data

def get_returns(price):
    n = len(price)
    ratiovec = price.iloc[1:n].values / price.iloc[:n-1].values  # Compute ratio P_t / P_t-1
    returns = ratiovec - 1
    return pd.DataFrame(returns, index=price.index[1:], columns=price.columns)

# Define tickers
tickers = ['GS', 'JPM', 'MS', 'SPY', 'TLT']

# Fetch stock data
price = get_stock_data(tickers)
print(price.head())


returns = get_returns(price)
print(returns.head())