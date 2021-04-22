from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

import requests
from bs4 import BeautifulSoup
from error_messages import *

class RealTimeLabel(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)


    def update_indices(self):
        print("Updating Quotes...")
        self.loading.setText("Loading")
        Chart.loading(self)

        # DOW update
        url = "https://finance.yahoo.com/quote/%5EDJI?p=%5EDJI"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
        print(price)
        self.btn_DOW_quote.setText(price)

        # NASDAQ update
        url = "https://finance.yahoo.com/quote/%5EIXIC?p=%5EIXIC"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
        print(price)
        self.btn_NAS_quote.setText(price)

        # S&P 500 update
        url = "https://finance.yahoo.com/quote/%5EGSPC?p=%5EGSPC"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
        print(price)
        self.btn_SP_quote.setText(price)

        # Russell 2000 update
        url = "https://finance.yahoo.com/quote/%5ERUT?p=%5ERUT"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
        self.btn_RUSS_quote.setText(price)
        self.loading.setText("")