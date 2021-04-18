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
        self.label_home.setText("Invalid Input(s). Try again")
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

        # def closing():

    #
    # def close(self):
    #     Signup_Messages.msg.close()


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