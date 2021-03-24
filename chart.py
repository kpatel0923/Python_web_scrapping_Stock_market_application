from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

import yfinance as yf

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


    def update_graph_index(self, stockPeriod, stockSymbol):
        stockTicker = yf.Ticker(stockSymbol)

        df = stockTicker.history(period=stockPeriod)  # Placing stock data into a dataframe
        data = df['Close']

        chartTitle = stockSymbol

        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.plot(data)

        self.MplWidget.canvas.axes.set_title(chartTitle.upper())
        self.MplWidget.canvas.draw()