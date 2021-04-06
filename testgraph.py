import yfinance as yf
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


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

    return name, exchange, sector, industry, ask, bid, _open, prevClose, divYield, beta, forwardPE, vol_10_days, vol, longSummary


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


def price(test):
    symbol = test
    s = yf.Ticker(symbol)
    ask = s.info['ask']
    return ask