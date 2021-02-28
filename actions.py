import sys
import subprocess
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sqlite3

#files
from login import *
from signup import *
from forgot_password import *


def DATABASE(query):

    with sqlite3.connect("490_database.db") as file:
        C = file.cursor()
        C.execute(query)
        file.commit()
        result = C.fetchall()
        return result


class common_Buttons(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def home_screen(self):
        # PAGE home
        self.btn_home.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.home_page))

    def login_screen(self):
        # PAGE login
        self.btn_login_signup.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.login_page))

    def signup_screen(self):
        # PAGE signup
        self.btn_signup.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.signup_page))




class login_Buttons(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def login(self):
        # PAGE home
        self.btn_login.clicked.connect(lambda: Login.handleLogin(self))

    def reset_pass(self):
        # PAGE home
        self.btn_password.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.password_page))
        self.btn_send.clicked.connect(lambda: Password.handleSend(self))
        self.btn_continue.clicked.connect(lambda: Password.code(self))
        self.btn_back.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.login_page))
        self.btn_back_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.password_page))
        self.btn_reset.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.login_page))


class sign_Buttons(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def signup(self):
        # PAGE home
        self.btn_signup_add.clicked.connect(lambda: Signup.addNewUser(self))