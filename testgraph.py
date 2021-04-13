import yfinance as yf
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd


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

    forwardPE = s.info['forwardPE']

    sector = s.info['sector']
    industry = s.info['industry']
    longSummary = s.info['longBusinessSummary']

    return name, exchange, sector, industry, ask, bid, _open, prevClose, divYield, forwardPE, vol_10_days, vol, longSummary


def screener_1(web):
    URL = web
    req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    soup = BeautifulSoup(webpage, 'html.parser')
    tickers = soup.find_all('a', attrs={'class': 'screener-link-primary'})

    symbol_list = []
    for ticker in tickers:
        symbol_list.append(ticker.text)

    return symbol_list


def screener_2(test):
    # Web scraping tickers from a finviz screener
    # Copy & paste the url to your browser and go to the website to edit the screener
    # Then copy & paste the new url into the script

    URL = test
    req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    soup = BeautifulSoup(webpage, 'html.parser')
    tickers = soup.find_all('a', attrs={'class': 'screener-link-primary'})
    ticker_info = soup.find_all('a', attrs={'class': 'screener-link'})

    symbol_list = []
    for ticker in tickers:
        symbol_list.append(ticker.text)

    info_list = []
    for info in ticker_info:
        info_list.append(info.text)

    percent_list = []
    percent_list.append(info_list[8::10])

    name_list = []
    name_list.append(info_list[1::10])

    names_list = name_list[0]
    percents_list = percent_list[0]

    return symbol_list, names_list, percents_list


def topGainers():
    url = ('https://finance.yahoo.com/gainers')
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    for row in soup.find_all('table')[0].tbody.find_all('tr')[:10]:

        stockSymbol = row.find_all('td')[0].text
        stockName = row.find_all('td')[1].text
        stockChange = row.find_all('td')[4].text
        #        vol = row.find_all('td')[5].text
        #        threeMonVol = row.find_all('td')[6].text

        stockList = {'Stock Symbol': [stockSymbol],
                     'Stock Name': [stockName],
                     'Percentage Change': [stockChange]}

        df = pd.DataFrame(stockList)
        stock_list = df.values.tolist()

    return stockList
        # f = '{:<5} | {:<40} | {:<6}'
        # for i in stock_list:
        #     print(f.format(*i))



def topLosers():
    url = ('https://finance.yahoo.com/losers')
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    for row in soup.find_all('table')[0].tbody.find_all('tr')[:10]:

        stockSymbol = row.find_all('td')[0].text
        stockName = row.find_all('td')[1].text
        stockChange = row.find_all('td')[4].text
        #        vol = row.find_all('td')[5].text
        #        threeMonVol = row.find_all('td')[6].text

        stockList = {'Stock Symbol': [stockSymbol],
                     'Stock Name': [stockName],
                     'Percentage Change': [stockChange]}

        df = pd.DataFrame(stockList)
        stock_list = df.values.tolist()

    return stockList
        # f = '{:<5} | {:<40} | {:<6}'
        # for i in stock_list:
        #     print(f.format(*i))




def price(test):
    symbol = test
    s = yf.Ticker(symbol)
    ask = s.info['ask']
    return ask

def more(test):
    symbol = test
    s = yf.Ticker(symbol)
    longSummary = s.info['longBusinessSummary']
    return longSummary