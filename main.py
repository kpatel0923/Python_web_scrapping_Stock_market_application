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
from indices import *

ui,_ = loadUiType('test_ui.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        title = "Trading with a Budget"
        self.setWindowTitle(title)


        #Timer for the Indcies
        #self.timer = QTimer(self)
        #self.timer.timeout.connect(self.updateLabels)
        #self.timer.start(5000)

        #This is called to install any packages that a new user might be missing


        #The common buttons to navigate the pages
        common_Buttons.home_screen(self)
        common_Buttons.login_screen(self)
        common_Buttons.signup_screen(self)
        common_Buttons.test(self)
        common_Buttons.refresh(self)

        #The Login buttoms are listed here
        login_Buttons.login(self)
        login_Buttons.reset_pass(self)


        #The Sign buttons are listed here
        sign_Buttons.signup(self)

        #These are the quiz buttons
        quiz_Buttons_actions.navigate(self)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
