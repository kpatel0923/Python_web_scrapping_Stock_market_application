import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import actions
import re

#files
import actions

class Login(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def handleLogin(self):
        email = self.lineEdit_email.text()
        password = self.lineEdit_password.text()

        if not password.isalnum():
            print("Invalid input(s)")

        elif not re.search("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)" , email):
            print('Invalid input(s)')

        else:
            person = actions.DATABASE(f"select * from users where email  == '{email}' and password == '{password}'")
            if not person:
                print("Invalid login")
            else:
                print("success")






    def forgotPassword(self):
        pass

