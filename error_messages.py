import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5 import QtGui


class Messages(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)


class Login_Messages(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

    def error(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Invalid Input(s)")
        self.label_home.setText("Invalid Input(s), Try again")
        # msg.setStandardButtons(msg.NoButton)
        x = msg.exec_()

    def error_2(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Invalid Email format")
        self.label_home.setText("Invalid Email format, Try again")
        # msg.setStandardButtons(msg.NoButton)
        x = msg.exec_()

    def error_3(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Credentials does not match database")
        self.label_home.setText("The credentials you entered does not match our records, Try again")
        # msg.setStandardButtons(msg.NoButton)
        x = msg.exec_()


class Signup_Messages(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

    def success(self):
        msg = QMessageBox()
        msg.setWindowTitle("Success!")
        msg.setText("Account created!")
        # msg.setStandardButtons(msg.NoButton)
        x = msg.exec_()

    def error_0(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Invalid Input(s)!")
        # msg.setStandardButtons(msg.NoButton)
        self.label_home_3.setText("Invalid Input(s) Please Check Fields")

        x = msg.exec_()

    def error_1(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Invalid Email!")
        # msg.setStandardButtons(msg.NoButton)
        self.label_home_3.setText("Invalid Email")

        x = msg.exec_()

    def error_2(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Passwords Do Not Match!")
        self.label_home_3.setText("Passwords Do Not Match")
        # msg.setStandardButtons(msg.NoButton)
        x = msg.exec_()

    def error_3(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Email Already Exists!")
        self.label_home_3.setText("Email Already Exists")
        # msg.setStandardButtons(msg.NoButton)
        x = msg.exec_()

    def error_4(self):
        msg = QMessageBox()
        msg.setWindowTitle("Success!")
        msg.setText("Thank you for creating a new account! Please login to continue.")
        self.label_home.setText("Thank you for creating a new account! Please login to continue.")
        # msg.setStandardButtons(msg.NoButton)
        x = msg.exec_()


class ForgotPass_Messages(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

    def error_1(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Invalid Input(s)")
        self.lbl_pass.setText("Invalid Input(s)")
        # msg.setStandardButtons(msg.NoButton)
        x = msg.exec_()

    def error_2(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Email Not Found In Database")
        self.lbl_pass.setText("Email Not Found In Database")
        # msg.setStandardButtons(msg.NoButton)
        x = msg.exec_()

    def error_3(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Invalid Code")
        self.lbl_pass.setText("Invalid Code")
        # msg.setStandardButtons(msg.NoButton)
        x = msg.exec_()

    def error_4(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error!")
        msg.setText("Passwords Must Match")
        self.label_19.setText("Passwords Must Match")
        # msg.setStandardButtons(msg.NoButton)
        x = msg.exec_()

    def error_5(self):
        msg = QMessageBox()
        msg.setWindowTitle("Sending Email")
        msg.setText("The reset code is being to the email...")
        self.lbl_pass.setText("Sending Email...")
        # msg.setStandardButtons(msg.NoButton)
        x = msg.exec_()

class Chart(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)

    def loading(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Loading!")
        msg.setText("Loading content!")
        # msg.setStandardButtons(msg.NoButton)
        x = msg.exec_()

    def invalid(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Invalid Ticker!")
        msg.setText("Invalid Ticker!")
        # msg.setStandardButtons(msg.NoButton)
        x = msg.exec_()

