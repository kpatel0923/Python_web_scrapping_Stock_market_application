import yfinance as yf
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


"A golden cross is considered a bullish sign; it occurs when the 50-day moving average \
rises above 200-day moving average. A death cross is considered a bearish sign; it \
occurs when the 50-day moving average drops below 200-day moving average."

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

def screener_1():
    URL = ("https://finviz.com/screener.ashx?v=111&f=cap_micro,geo_usa,sh_relvol_o2&o=-change")
    req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()

    soup = BeautifulSoup(webpage, 'html.parser')
    tickers = soup.find_all('a', attrs={'class': 'screener-link-primary'})

    symbol_list = []
    for ticker in tickers:
        symbol_list.append(ticker.text)