import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import actions
import re



class user_Buttons(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)


    def back_screen(self):
        self.stackedWidget_2.setCurrentWidget(self.chart_page)
        self.stackedWidget_3.setCurrentWidget(self.page_3)

    def pass_change(self):
        self.stackedWidget.setCurrentWidget(self.password_page)
        self.stackedWidget_3.setCurrentWidget(self.page_3)

    def quiz(self):
        self.stackedWidget.setCurrentWidget(self.quiz_page)
        self.stackedWidget_3.setCurrentWidget(self.page_3)