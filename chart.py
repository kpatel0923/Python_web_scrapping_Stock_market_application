from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt
import threading
from PyQt5.uic import loadUiType
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import sys
import time

import yfinance as yf
import testgraph
from error_messages import *


class MatplotlibWidget(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))

    def chart(self, stockPeriod):
        stockSymbol = self.lineEdit_symbol.text()
        stockTicker = yf.Ticker(stockSymbol)

        df = stockTicker.history(period=stockPeriod)  # Placing stock data into a dataframe
        data = df['Close']

        chartTitle = stockSymbol

        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(data)

        self.MplWidget.canvas.axes.set_title(chartTitle.upper())
        self.MplWidget.canvas.draw()

        if (stockSymbol != "DJI" and stockSymbol != "^GSPC" and stockSymbol != "^IXIC" and stockSymbol != "^RUT"):

            name, exchange, sector, industry, ask, bid, _open, prevClose, divYield, forwardPE, vol_10_days, vol, longSummary = testgraph.summary(
                stockSymbol)
            longSummary = " ".join(longSummary.split(' ')[:101])

            self.lbl_name.setText(name)
            self.lbl_exchange.setText(exchange)
            self.lbl_sector.setText(sector)
            self.lbl_industry.setText(industry)
            self.lbl_ask.setText(str(ask))
            self.lbl_bid.setText(str(bid))
            self.lbl_open.setText(str(_open))
            self.lbl_close.setText(str(prevClose))
            self.lbl_yield.setText(str(divYield))
            self.lbl_pe.setText(str(forwardPE))
            self.lbl_tenvol.setText(str(vol_10_days))
            self.lbl_vol.setText(str(vol))
            self.lbl_summary.setText(longSummary + "...")

            self.lbl_exchange.setToolTip(
                "<html><head/><body><p><span style=\" color:#000058;\">An exchange is a marketplace where securities, commodities, derivatives and other financial instruments are traded. The core function of an exchange is to ensure fair and orderly trading and the efficient dissemination of price information for any securities trading on that exchange. Exchanges give companies, governments, and other groups a platform from which to sell securities to the investing public.The more prominent exchanges include the New York Stock Exchange (NYSE), the Nasdaq, the London Stock Exchange (LSE), and the Tokyo Stock Exchange (TSE).</span></p></body></html>")
            self.lbl_ask.setToolTip(
                "<html><head/><body><p><span style=\" color:#00005d;\">The ask is the lowest price someone is willing to sell a share.</span></p></body></html>")
            self.lbl_bid.setToolTip(
                "<html><head/><body><p><span style=\" color:#00005f;\">The bid represents the highest price someone is willing to pay for a share.</span></p></body></html>")
            self.lbl_vol.setToolTip(
                "<html><head/><body><p><span style=\" color:#000058;\">Volume measures the number of shares traded in a stock or contracts traded in futures or options. Volume can be an indicator of market strength, as rising markets on increasing volume are typically viewed as strong and healthy.When prices fall on increasing volume, the trend is gathering strength to the downside. When prices reach new highs (or new lows) on decreasing volume, watch out; a reversal might be taking shape.</span></p></body></html>")
            self.lbl_tenvol.setToolTip(
                "<html><head/><body><p><span style=\" color:#00004b;\">This is the daily average of the cumulative trading volume for the last 10 days on which there was volume traded for the stock.</span></p></body></html>")
            self.lbl_open.setToolTip(
                "<html><head/><body><p><span style=\" color:#00005a;\">The open is the starting period of trading on a securities exchange or organized over-the-counter market.</span></p></body></html>")
            self.lbl_close.setToolTip(
                "<html><head/><body><p><span style=\" color:#000062;\">Previous close is a security\'s closing price on the preceding time period of the one being referenced. Previous close almost always refers to the prior day\'s final price of a security when the market officially closes for the day.</span></p></body></html>")
            self.lbl_yield.setToolTip(
                "<html><head/><body><p><span style=\" color:#000062;\">The dividend yield, expressed as a percentage, is a financial ratio (dividend/price) that shows how much a company pays out in dividends each year relative to its stock price.The dividend yield is an estimate of the dividend-only return of a stock investment. Assuming the dividend is not raised or lowered, the yield will rise when the price of the stock falls. And conversely, it will fall when the price of the stock rises. Because dividend yields change relative to the stock price, it can often look unusually high for stocks that are falling in value quickly.</span></p></body></html>")
            self.lbl_pe.setToolTip(
                "<html><head/><body><p><span style=\" color:#000068;\">The forward P/E ratio (or forward price-to-earnings ratio) divides the current share price of a company by the estimated future (“forward”) earnings per share (EPS) of that company. For valuation purposes, a forward P/E ratio is typically considered more relevant than a historical P/E ratio.</span></p></body></html>")
            self.lbl_sector.setToolTip(
                "<html><head/><body><p><span style=\" color:#000062;\">A sector is one of a few general segments in the economy within which a large group of companies can be categorized. An economy can be broken down into about a dozen sectors, which can describe nearly all of the business activity in that economy.</span></p></body></html>")
            self.lbl_industry.setToolTip(
                "<html><head/><body><p><span style=\" color:#000047;\">Industry refers to a specific group of companies that operate in a similar business sphere. Essentially, industries are created by breaking down sectors into more defined groupings.Each of the dozen or so sectors will have a varying number of industries, but it can be in the hundreds.</span></p></body></html>")
            self.loading.setText("")
        else:
            self.frame_116.setEnabled(False)
            self.loading.setText("")
            self.lbl_name.clear()
            self.lbl_exchange.clear()
            self.lbl_sector.clear()
            self.lbl_industry.clear()
            self.lbl_ask.clear()
            self.lbl_bid.clear()
            self.lbl_open.clear()
            self.lbl_close.clear()
            self.lbl_yield.clear()
            self.lbl_pe.clear()
            self.lbl_tenvol.clear()
            self.lbl_vol.clear()
            self.lbl_summary.clear()


    def update_graph(self, stockPeriod):
        self.loading.setText("Loading")
        Chart.loading(self)
        # self.statusbar = self.statusBar()
        # self.statusbar.showMessage("Loading", 3000)

        # self.loading_screen = LoadingScreen()
        # self.movie = QMovie("giphy.gif")
        # self.loading.setMovie(self.movie)
        # self.movie.start()
        self.frame_116.setEnabled(True)

        if self.loading.text() == "Loading":
            MatplotlibWidget.chart(self, stockPeriod)

        # Signup_Messages.close(self)

            # self.loading_screen = LoadingScreen.closes(self)



    def update_graph_time(self, stockPeriod):
        stockSymbol = self.lineEdit_symbol.text()
        stockTicker = yf.Ticker(stockSymbol)
        Chart.loading(self)

        df = stockTicker.history(period=stockPeriod) # Placing stock data into a dataframe
        data = df['Close']

        chartTitle = stockSymbol

        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(data)

        self.MplWidget.canvas.axes.set_title(chartTitle.upper())
        self.MplWidget.canvas.draw()


    def update_graph_btn(self, symbol):
        self.loading.setText("Loading")
        Chart.loading(self)
        print(symbol)
        self.frame_116.setEnabled(True)
        self.lineEdit_symbol.setText(symbol)
        stockSymbol = self.lineEdit_symbol.text()
        stockTicker = yf.Ticker(stockSymbol)

        df = stockTicker.history(period='1y')  # Placing stock data into a dataframe
        data = df['Open']

        chartTitle = stockSymbol

        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(data)

        self.MplWidget.canvas.axes.set_title(chartTitle.upper())
        self.MplWidget.canvas.draw()

        if (symbol != "DJI" and symbol != "^GSPC" and symbol != "^IXIC" and symbol != "^RUT"):

            name, exchange, sector, industry, ask, bid, _open, prevClose, divYield, forwardPE, vol_10_days, vol, longSummary = testgraph.summary(stockSymbol)
            longSummary = " ".join(longSummary.split(' ')[:101])

            self.lbl_name.setText(name)
            self.lbl_exchange.setText(exchange)
            self.lbl_sector.setText(sector)
            self.lbl_industry.setText(industry)
            self.lbl_ask.setText(str(ask))
            self.lbl_bid.setText(str(bid))
            self.lbl_open.setText(str(_open))
            self.lbl_close.setText(str(prevClose))
            self.lbl_yield.setText(str(divYield))
            self.lbl_pe.setText(str(forwardPE))
            self.lbl_tenvol.setText(str(vol_10_days))
            self.lbl_vol.setText(str(vol))
            self.lbl_summary.setText(longSummary + "...")

            self.lbl_exchange.setToolTip(
                "<html><head/><body><p><span style=\" color:#000058;\">An exchange is a marketplace where securities, commodities, derivatives and other financial instruments are traded. The core function of an exchange is to ensure fair and orderly trading and the efficient dissemination of price information for any securities trading on that exchange. Exchanges give companies, governments, and other groups a platform from which to sell securities to the investing public.The more prominent exchanges include the New York Stock Exchange (NYSE), the Nasdaq, the London Stock Exchange (LSE), and the Tokyo Stock Exchange (TSE).</span></p></body></html>")
            self.lbl_ask.setToolTip(
                "<html><head/><body><p><span style=\" color:#00005d;\">The ask is the lowest price someone is willing to sell a share.</span></p></body></html>")
            self.lbl_bid.setToolTip(
                "<html><head/><body><p><span style=\" color:#00005f;\">The bid represents the highest price someone is willing to pay for a share.</span></p></body></html>")
            self.lbl_vol.setToolTip(
                "<html><head/><body><p><span style=\" color:#000058;\">Volume measures the number of shares traded in a stock or contracts traded in futures or options. Volume can be an indicator of market strength, as rising markets on increasing volume are typically viewed as strong and healthy.When prices fall on increasing volume, the trend is gathering strength to the downside. When prices reach new highs (or new lows) on decreasing volume, watch out; a reversal might be taking shape.</span></p></body></html>")
            self.lbl_tenvol.setToolTip(
                "<html><head/><body><p><span style=\" color:#00004b;\">This is the daily average of the cumulative trading volume for the last 10 days on which there was volume traded for the stock.</span></p></body></html>")
            self.lbl_open.setToolTip(
                "<html><head/><body><p><span style=\" color:#00005a;\">The open is the starting period of trading on a securities exchange or organized over-the-counter market.</span></p></body></html>")
            self.lbl_close.setToolTip(
                "<html><head/><body><p><span style=\" color:#000062;\">Previous close is a security\'s closing price on the preceding time period of the one being referenced. Previous close almost always refers to the prior day\'s final price of a security when the market officially closes for the day.</span></p></body></html>")
            self.lbl_yield.setToolTip(
                "<html><head/><body><p><span style=\" color:#000062;\">The dividend yield, expressed as a percentage, is a financial ratio (dividend/price) that shows how much a company pays out in dividends each year relative to its stock price.The dividend yield is an estimate of the dividend-only return of a stock investment. Assuming the dividend is not raised or lowered, the yield will rise when the price of the stock falls. And conversely, it will fall when the price of the stock rises. Because dividend yields change relative to the stock price, it can often look unusually high for stocks that are falling in value quickly.</span></p></body></html>")
            self.lbl_pe.setToolTip(
                "<html><head/><body><p><span style=\" color:#000068;\">The forward P/E ratio (or forward price-to-earnings ratio) divides the current share price of a company by the estimated future (“forward”) earnings per share (EPS) of that company. For valuation purposes, a forward P/E ratio is typically considered more relevant than a historical P/E ratio.</span></p></body></html>")
            self.lbl_sector.setToolTip(
                "<html><head/><body><p><span style=\" color:#000062;\">A sector is one of a few general segments in the economy within which a large group of companies can be categorized. An economy can be broken down into about a dozen sectors, which can describe nearly all of the business activity in that economy.</span></p></body></html>")
            self.lbl_industry.setToolTip(
                "<html><head/><body><p><span style=\" color:#000047;\">Industry refers to a specific group of companies that operate in a similar business sphere. Essentially, industries are created by breaking down sectors into more defined groupings.Each of the dozen or so sectors will have a varying number of industries, but it can be in the hundreds.</span></p></body></html>")
            self.loading.setText("")
        else:
            self.frame_116.setEnabled(False)
            self.loading.setText("")
            self.lbl_name.clear()
            self.lbl_exchange.clear()
            self.lbl_sector.clear()
            self.lbl_industry.clear()
            self.lbl_ask.clear()
            self.lbl_bid.clear()
            self.lbl_open.clear()
            self.lbl_close.clear()
            self.lbl_yield.clear()
            self.lbl_pe.clear()
            self.lbl_tenvol.clear()
            self.lbl_vol.clear()
            self.lbl_summary.clear()


    def more(self):
        stockSymbol = self.lineEdit_symbol.text()
        longSummary = testgraph.more(stockSymbol)
        self.lbl_summary.setFont(QFont('Century Gothic', 9))
        self.lbl_summary.setText(longSummary)

    def less(self):
        stockSymbol = self.lineEdit_symbol.text()
        longSummary = testgraph.more(stockSymbol)
        longSummary = " ".join(longSummary.split(' ')[:101])
        self.lbl_summary.setFont(QFont('Century Gothic', 12))
        self.lbl_summary.setText(longSummary + "...")