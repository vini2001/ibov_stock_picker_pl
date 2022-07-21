


#

import os
import constants_ as c
import requests
from bs4 import BeautifulSoup
import yfinance as yf
import pandas as pd



def close_at_year(hist, year):
    for i in range(0, 10):
        if len(hist[hist['Date'] == f'{year}-12-{31-i}']) > 0:
            return hist[hist['Date'] == f'{year}-12-{31-i}']['Close']
#25 top
tickers = ['GSHP3', 'BALM3', 'CAMB3', 'HAGA3', 'MSPA3', 'PATI3', 'EMAE3', 'EPAR3', 'CALI3', 'FRIO3', 'CRDE3', 'MWET3', 'DEXP3', 'UCAS3', 'EALT3', 'WLMM3', 'NUTR3', 'OSXB3', 'TXRX3', 'TPIS3', 'MNPR3', 'TEKA3', 'PDTC3', 'BDLL3', 'TECN3']
#50 top
# tickers = ['GSHP3', 'BALM3', 'WIZS3', 'CAMB3', 'HAGA3', 'VLID3', 'MSPA3', 'FESA3', 'PATI3', 'EMAE3', 'EPAR3', 'CALI3', 'PNVL3', 'JFEN3', 'EEEL3', 'FRIO3', 'CRDE3', 'ATMP3', 'TEND3', 'NEXP3', 'MOAR3', 'TUPY3', 'MWET3', 'DEXP3', 'UCAS3', 'BKBR3', 'EALT3', 'WLMM3', 'UNIP3', 'ROMI3', 'NUTR3', 'OSXB3', 'DIRR3', 'TXRX3', 'PFRM3', 'TPIS3', 'POSI3', 'LPSB3', 'SHOW3', 'CGRA3', 'GEPA3', 'MNPR3', 'PTBL3', 'TCSA3', 'TEKA3', 'PDTC3', 'BDLL3', 'TECN3', 'MILS3', 'PDGR3']

res_2020 = 0
res_2021 = 0

for ticker in tickers:
    msft = yf.Ticker(f"{ticker}.SA")
    print(msft)

    hist = msft.history(period="max")
    hist.to_csv('hist.csv')
    hist = pd.read_csv('hist.csv')

    close_2019 = float(close_at_year(hist, 2019).values[0])
    close_2020 = float(close_at_year(hist, 2020).values[0])
    close_2021 = float(close_at_year(hist, 2021).values[0])

    print(f'close_2019: {close_2019}')
    print(f'close_2020: {close_2020}')
    print(f'close_2021: {close_2021}')

    ind_res_2020 = close_2020 / close_2019
    ind_res_2021 = close_2021 / close_2019
    print(f'2020: {ind_res_2020}')
    print(f'2021: {ind_res_2021}')
    res_2020 += ind_res_2020
    res_2021 += ind_res_2021
    print()

# Ibov: +2.13%
print(f'Return of the portfolio (2020): {(res_2020/len(tickers) - 1) * 100}%')
# Ibov: -10.5%
print(f'Return of the portfolio (2021): {(res_2021/len(tickers) - 1) * 100}%')
