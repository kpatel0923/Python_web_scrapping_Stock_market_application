import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import random
from indices import *

#files
from actions import *
from quiz import *

ui,_ = loadUiType('test_ui.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        title = "Trading with a budget"
        self.setWindowTitle(title)


        #Timer for the Indcies
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateLabels)
        self.timer.start(5000)

        #This is called to install any packages that a new user might be missing


        #The common buttons to navigate the pages
        common_Buttons.home_screen(self)
        common_Buttons.login_screen(self)
        common_Buttons.signup_screen(self)
        common_Buttons.test(self)

        #The Login buttoms are listed here
        login_Buttons.login(self)
        login_Buttons.reset_pass(self)


        #The Sign buttons are listed here
        sign_Buttons.signup(self)

        #These are the quiz buttons
        quiz_Buttons_actions.navigate(self)

    def updateLabels(self):
        print("Updating Prices...")

        # DOW update
        url = "https://finance.yahoo.com/quote/%5EDJI?p=%5EDJI"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
        print(price)
        self.btn_DOW.setText(price)

        # NASDAQ update
        url = "https://finance.yahoo.com/quote/%5EIXIC?p=%5EIXIC"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
        print(price)
        self.btn_NAS.setText(price)

        # S&P 500 update
        url = "https://finance.yahoo.com/quote/%5EGSPC?p=%5EGSPC"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
        print(price)
        self.btn_SP.setText(price)

        # Russell 2000 update
        url = "https://finance.yahoo.com/quote/%5ERUT?p=%5ERUT"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
        self.btn_RUSS.setText(price)

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
