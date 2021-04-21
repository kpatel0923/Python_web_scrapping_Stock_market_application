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

# class TimerMessageBox(QtGui.QMessageBox):
#     def __init__(self, timeout=3, parent=None):
#         super(TimerMessageBox, self).__init__(parent)
#         self.setWindowTitle("wait")
#         self.time_to_wait = timeout
#         self.setText("wait (closing automatically in {0} secondes.)".format(timeout))
#         self.setStandardButtons(QtGui.QMessageBox.NoButton)
#         self.timer = QtCore.QTimer(self)
#         self.timer.setInterval(1000)
#         self.timer.timeout.connect(self.changeContent)
#         self.timer.start()
#
#     def changeContent(self):
#         self.setText("wait (closing automatically in {0} secondes.)".format(self.time_to_wait))
#         self.time_to_wait -= 1
#         if self.time_to_wait <= 0:
#             self.close()
#
#     def closeEvent(self, event):
#         self.timer.stop()
#         event.accept()