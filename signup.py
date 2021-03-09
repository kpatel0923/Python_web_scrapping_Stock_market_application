import sys
import re
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#files
import actions

class Signup(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

    def clear(self):
        self.lineEdit_first.clear()
        self.lineEdit_last.clear()
        self.lineEdit_email_2.clear()
        self.lineEdit_password_2.clear()
        self.lineEdit_password_3.clear()

    def addNewUser(self):
        user_first = self.lineEdit_first.text()
        user_last = self.lineEdit_last.text()
        user_email = self.lineEdit_email_2.text()
        user_password = self.lineEdit_password_2.text()
        user_retype = self.lineEdit_password_3.text()

        all_emails = actions.DATABASE("select email from users")
        print(all_emails)

        if not (user_first.isalpha() and user_last.isalpha() and user_password.isalnum() and user_retype.isalnum()):
            print("Invalid input(s) *")

        elif not re.search("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)" , user_email):
            print('Email bad')

        elif user_password != user_retype:
            print("Passwords do not match")

        elif user_email in [record[0] for record in all_emails]:
            print('Email already exists')

        else:
            print('added')
            actions.DATABASE(f" insert into users (email, first, last, password) values ( '{user_email}' , '{user_first}' , '{user_last}', '{user_password}' )  ")
            Signup.clear(self)
            self.stackedWidget.setCurrentWidget(self.quiz_page)
            print(all_emails)
