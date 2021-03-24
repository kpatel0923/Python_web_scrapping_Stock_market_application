import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime


"A golden cross is considered a bullish sign; it occurs when the 50-day moving average \
rises above 200-day moving average. A death cross is considered a bearish sign; it \
occurs when the 50-day moving average drops below 200-day moving average."


def LongAverage():
    # symbol = input(str("Enter Stock Symbol: "))
    # date = input("Date YYYY-MM-DD: ").
    symbol = "TSLA"
    date = "2020-01-01"
    s = yf.Ticker(symbol)

    df = yf.download(symbol,start = date)


    df['MA50'] = df['Adj Close'].rolling(50).mean()
    df['MA200'] = df['Adj Close'].rolling(200).mean()

    df = df.dropna()
    df = df[['Adj Close','MA50','MA200']]

    Buy = []
    Sell = []
    for i in range(len(df)):
        if df.MA50.iloc[i] > df.MA200.iloc[i] and df.MA50.iloc[i-1] < df.MA200.iloc[i-1]:
            Buy.append(i)
        elif df.MA50.iloc[i] < df.MA200.iloc[i] and df.MA50.iloc[i-1] > df.MA200.iloc[i-1]:
            Sell.append(i)
    plt.figure(figsize = (12,5))
    plt.plot(df['Adj Close'], label='Asset price', c='blue', alpha=.5)
    plt.plot(df['MA50'], label='MA50', c='red', alpha = .9)
    plt.plot(df['MA200'], label='MA200', c='black', alpha = .9)
    plt.scatter(df.iloc[Buy].index, df.iloc[Buy]['Adj Close'], marker = '^', color = 'g', s = 100)
    plt.scatter(df.iloc[Sell].index, df.iloc[Sell]['Adj Close'], marker = 'v', color = 'r', s = 100)

    plt.title(symbol.upper() + " - 50 / 200 Day Moving Average")
    plt.legend()
    plt.show()


def summary(test):
    symbol = test
    s = yf.Ticker(symbol)

    name = s.info['shortName']
    ask = s.info['ask']
    bid = s.info['bid']
    vol = s.info['volume']
    exchange = s.info['exchange']

    _open = s.info['open']
    prevClose = s.info['previousClose']
    vol_10_days = s.info['averageVolume10days']
    divYield = s.info['dividendYield']

    beta = s.info['beta']
    forwardPE = s.info['forwardPE']

    sector = s.info['sector']
    industry = s.info['industry']
    longSummary = s.info['longBusinessSummary']

    print(name, '\t', 'Exchange: ', exchange, '\n\n', 'Ask: ', ask, '\t', 'Bid: ', bid, '\n\n', 'Volume: ', vol,
          '\t', 'Average 10 Day Volume: ', vol_10_days, '\n\n''Open: ', _open, '\t', 'Previous Close: ',
          prevClose, '\n\n', 'Dividend Yield: ', divYield, '\t', 'Beta: ', beta, '\t', 'Forward PE: ', forwardPE,
          '\n\n',
          'Sector: ', sector, '\t', 'Industry: ', industry, '\n\n', longSummary)

    return name, exchange, sector, industry, ask, bid, _open, prevClose, divYield, beta, forwardPE, vol_10_days, vol, longSummary