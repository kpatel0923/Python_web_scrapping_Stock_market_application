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


class user_Buttons_budget(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def income(self):
        email = self.lineEdit_emailholder.text()
        primary = self.lineEdit_primary.text()
        secondary = self.lineEdit_secondary.text()
        income = primary + secondary
        self.income.setText(str(income))
        actions.DATABASE(f"update users set income = '{income}' where email = '{email}' ")

    def expenses(self):
        email = self.lineEdit_emailholder.text()
        e1 = self.lineEdit_rent.text()
        e2 = self.lineEdit_utilitiestext()
        e3 = self.lineEdit_groceriestext()
        e4 = self.lineEdit_insurancetext()
        e5 = self.lineEdit_entertainmenttext()
        e6 = self.lineEdit_othertext()

        expenses = e1 + e2 + e3 + e4 + e5 + e6
        self.expenses.setText(str(expenses))
        actions.DATABASE(f"update users set expenses = '{expenses}' where email = '{email}' ")

    def getting_stocks(self):
        score = self.lineEdit_scoreholder.text()


