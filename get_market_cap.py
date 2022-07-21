


#

import os
import constants_ as c
import requests
from bs4 import BeautifulSoup
import yfinance as yf
import pandas as pd



# load csv hist.csv
def close_at_year(hist, year):
    for i in range(0, 10):
        if len(hist[hist['Date'] == f'{year}-12-{31-i}']) > 0:
            return hist[hist['Date'] == f'{year}-12-{31-i}']['Close']


file_name = 'market_caps_2018-2021.csv'
if not os.path.exists(file_name):
    with open(file_name, "w") as f:
        f.write(",".join(['Ticker', '2018 MC', '2019 MC', '2020 MC', '2021 MC']) + "\n")


def mc_for_ticker(ticker):
    msft = yf.Ticker(f"{ticker}.SA")
    print(msft)
    info = msft.info
    if not 'marketCap' in info or not 'regularMarketPrice' in info:
        return None
        
    market_cap = info['marketCap']
    current_price = info['regularMarketPrice']
    print(f'Market Cap: {market_cap}')
    print(f'Price: {current_price}')

    if market_cap == None or current_price == None: return None

    hist = msft.history(period="max")
    hist.to_csv('hist.csv')
    hist = pd.read_csv('hist.csv')

    close_2018 = close_at_year(hist, 2018)
    close_2019 = close_at_year(hist, 2019)
    close_2020 = close_at_year(hist, 2020)
    close_2021 = close_at_year(hist, 2021)

    if type(close_2018) == type(None) or type(close_2019) == type(None) or type(close_2020) == type(None) or type(close_2021) == type(None):
        return None

    market_cap_2018 = str(((market_cap / current_price) * close_2018).values[0])
    market_cap_2019 = str(((market_cap / current_price) * close_2019).values[0])
    market_cap_2020 = str(((market_cap / current_price) * close_2020).values[0])
    market_cap_2021 = str(((market_cap / current_price) * close_2021).values[0])

    with open(file_name, "a+") as f:
        f.write(",".join([ticker, market_cap_2018, market_cap_2019, market_cap_2020, market_cap_2021]) + "\n")

# read csv cvm_to_ticker.csv
with open('cvm_to_ticker.csv', "r") as f:
    lines = f.readlines()
    ignore_firsts = 48
    for line in lines:
        ticker = line.split(',')[1].replace('\n', '')

        if ignore_firsts < 1:
            mc_for_ticker(ticker)
        ignore_firsts -= 1