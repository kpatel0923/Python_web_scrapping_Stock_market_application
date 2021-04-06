import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import actions
import re

import testgraph
from chart import *


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
        income = float(primary) + float(secondary)
        self.income.setText(str(income))
        actions.DATABASE(f"update users set income = '{income}' where email = '{email}' ")

        e1 = self.lineEdit_rent.text()
        e2 = self.lineEdit_utilities.text()
        e3 = self.lineEdit_groceries.text()
        e4 = self.lineEdit_insurance.text()
        e5 = self.lineEdit_other.text()

        acct_size = self.lineEdit_acct_size.text()
        goal = self.lineEdit_goal.text()

        expenses = float(e1) + float(e2) + float(e3) + float(e4) + float(e5)
        self.expenses.setText(str(expenses))
        actions.DATABASE(f"update users set expenses = '{expenses}' where email = '{email}' ")
        actions.DATABASE(f"update users set account_size = '{acct_size}' where email = '{email}' ")
        actions.DATABASE(f"update users set goal = '{goal}' where email = '{email}' ")

    def getting_stocks(self):
        score = self.lineEdit_scoreholder.text()
        score = int(score)

        if score >= 11 and score <= 23:
            URL = ("https://finviz.com/screener.ashx?v=111&f=cap_mega,geo_usa&o=-change")
            lis = testgraph.screener_1(URL)
            self.btn_1.setText(lis[0])
            self.btn_2.setText(lis[1])
            self.btn_3.setText(lis[2])
            self.btn_4.setText(lis[3])
            self.btn_5.setText(lis[4])
            self.btn_6.setText(lis[5])
            self.btn_7.setText(lis[6])
            self.btn_8.setText(lis[7])

        elif score >= 24 and score <= 34:
            URL = ("https://finviz.com/screener.ashx?v=111&f=cap_mid,geo_usa&o=-change")
            lis = testgraph.screener_1(URL)
            self.btn_1.setText(lis[0])
            self.btn_2.setText(lis[1])
            self.btn_3.setText(lis[2])
            self.btn_4.setText(lis[3])
            self.btn_5.setText(lis[4])
            self.btn_6.setText(lis[5])
            self.btn_7.setText(lis[6])
            self.btn_8.setText(lis[7])

        elif score >= 35 and score <= 47:
            URL = ("https://finviz.com/screener.ashx?v=111&f=cap_micro,geo_usa,sh_relvol_o2&o=-change")
            lis = testgraph.screener_1(URL)
            self.btn_1.setText(lis[0])
            self.btn_2.setText(lis[1])
            self.btn_3.setText(lis[2])
            self.btn_4.setText(lis[3])
            self.btn_5.setText(lis[4])
            self.btn_6.setText(lis[5])
            self.btn_7.setText(lis[6])
            self.btn_8.setText(lis[7])

        sym_1 = self.btn_1.text()
        self.btn_1.clicked.connect(lambda: MatplotlibWidget.update_graph_btn(self, sym_1))

        sym_2 = self.btn_2.text()
        self.btn_2.clicked.connect(lambda: MatplotlibWidget.update_graph_btn(self, sym_2))

        sym_3 = self.btn_3.text()
        self.btn_3.clicked.connect(lambda: MatplotlibWidget.update_graph_btn(self, sym_3))

        sym_4 = self.btn_4.text()
        self.btn_4.clicked.connect(lambda: MatplotlibWidget.update_graph_btn(self, sym_4))

        sym_5 = self.btn_5.text()
        self.btn_5.clicked.connect(lambda: MatplotlibWidget.update_graph_btn(self, sym_5))

        sym_6 = self.btn_6.text()
        self.btn_6.clicked.connect(lambda: MatplotlibWidget.update_graph_btn(self, sym_6))

        sym_7 = self.btn_7.text()
        self.btn_7.clicked.connect(lambda: MatplotlibWidget.update_graph_btn(self, sym_7))

        sym_8 = self.btn_8.text()
        self.btn_8.clicked.connect(lambda: MatplotlibWidget.update_graph_btn(self, sym_8))


    def test(self):
        print(self.btn_2.text())



    def what_if_price(self):
        symbol = self.lineEdit_symbol_2.text()
        price = testgraph.price(symbol)
        self.label_price.setText(str(price))

    def process(self):
        shares = self.lineEdit_shares.text()
        pt = self.lineEdit_pt.text()
        price = self.label_price.text()

        cost = float(price) * int(shares)
        cost = float("{:.2f}".format(cost))
        self.label_cost.setText(str(cost))
        self.label_pt.setText(str(pt))

        per = ((float(pt)-float(price)) / float(price)) * 100
        per = float("{:.2f}".format(per))
        self.label_per.setText(str(per))


