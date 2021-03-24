from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)
import yfinance as yf

import testgraph

class MatplotlibWidget(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))


    def update_graph(self, stockPeriod):
        stockSymbol = self.lineEdit_symbol.text()
        stockTicker = yf.Ticker(stockSymbol)

        # stockPeriod = '1y'

        # if self.btn_1D.isClicked():
        #     stockPeriod = '1d'
        # elif self.btn_W.clicked():
        #     stockPeriod = '1wk'
        # elif self.radioButton_month.isChecked():
        #     stockPeriod = '1mo'
        # elif self.radioButton_year.isChecked():
        #     stockPeriod = '1y'

        df = stockTicker.history(period=stockPeriod) # Placing stock data into a dataframe
        data = df['Close']

        chartTitle = stockSymbol

        if chartTitle == 'DJI':
            self.MplWidget.canvas.axes.clear()
            self.MplWidget.canvas.axes.plot(data)

            self.MplWidget.canvas.axes.set_title(chartTitle.upper())
            self.MplWidget.canvas.draw()

        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(data)

        self.MplWidget.canvas.axes.set_title(chartTitle.upper())
        self.MplWidget.canvas.draw()

        name, exchange, sector, industry, ask, bid, _open, prevClose, divYield, beta, forwardPE, vol_10_days, vol, longSummary = testgraph.summary(stockSymbol)

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
        self.lbl_summary.setText(longSummary)





    def update_graph_index(self, stockPeriod, stockSymbol):
        stockTicker = yf.Ticker(stockSymbol)

        df = stockTicker.history(period=stockPeriod)  # Placing stock data into a dataframe
        data = df['Close']

        chartTitle = stockSymbol

        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(data)

        self.MplWidget.canvas.axes.set_title(chartTitle.upper())
        self.MplWidget.canvas.draw()