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
        self.btn_home.setToolTip(
            "<html><head/><body><p><span style=\" color:#ffffff;\">Home</span></p></body></html>")

        #The common buttons to navigate the pages
        common_Buttons.home_screen(self)
        common_Buttons.login_screen(self)
        common_Buttons.signup_screen(self)

        #The Login buttoms are listed here
        login_Buttons.login(self)
        login_Buttons.reset_pass(self)


        #The Sign buttons are listed here
        sign_Buttons.signup(self)

        #These are the quiz buttons
        quiz_Buttons_actions.navigate(self)


        #The navigation buttons
        user_Buttons_actions.navigate(self)
        user_Buttons_actions.indicies(self)
        user_Buttons_actions.what_if(self)
        user_Buttons_actions.top_stocks(self)
        user_Buttons_actions.info(self)
        user_Buttons_actions.top_stocks(self)



def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()