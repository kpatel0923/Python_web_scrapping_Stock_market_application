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


    def help(self):
        if self.btn_login_signup.text() == "Logout":
            self.stackedWidget.setCurrentWidget(self.user_page)
        else:
            self.stackedWidget.setCurrentWidget(self.home_page)

    def back_screen(self):
        self.stackedWidget_2.setCurrentWidget(self.chart_page)
        self.stackedWidget_3.setCurrentWidget(self.page_3)

    def pass_change(self):
        self.stackedWidget.setCurrentWidget(self.password_page)
        self.stackedWidget_3.setCurrentWidget(self.page_3)

    def quiz(self):
        self.stackedWidget.setCurrentWidget(self.quiz_page)
        self.stackedWidget_3.setCurrentWidget(self.page_3)

    def delete(self):
        email = self.lineEdit_emailholder.text()
        print(email)
        self.stackedWidget_3.setCurrentWidget(self.delete_page)
        # warning = QMessageBox.warning(self, 'Delete', "Are you sure you want to delete?", QMessageBox.Yes | QMessageBox.No)
        # if warning == QMessageBox.Yes:
        self.btn_yes.clicked.connect(lambda: user_Buttons.delete_commands(self))
        self.btn_no.clicked.connect(lambda: self.stackedWidget_3.setCurrentWidget(self.page_3))

    def delete_commands(self):
        email = self.lineEdit_emailholder.text()
        actions.DATABASE(f"delete from users where email = '{email}' ")
        print('Success')
        user_Buttons_budget.logout(self)


class user_Buttons_budget(QMainWindow):

    URL = None

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def income(self):
        score = self.lineEdit_scoreholder.text()
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
        self.Goal.setText(str(goal))


        actions.DATABASE(f"update users set expenses = '{expenses}' where email = '{email}' ")
        actions.DATABASE(f"update users set account_size = '{acct_size}' where email = '{email}' ")
        actions.DATABASE(f"update users set goal = '{goal}' where email = '{email}' ")

    def update(self):
        first = self.lineEdit_first_2.text()
        last = self.lineEdit_last_2.text()
        email = self.lineEdit_emailholder.text()
        update_email = self.lineEdit_useremail.text()

        actions.DATABASE(f"update users set first = '{first}' where email = '{email}' ")
        actions.DATABASE(f"update users set last = '{last}' where email = '{email}' ")
        actions.DATABASE(f"update users set email = '{update_email}' where email = '{email}' ")

        self.lineEdit_emailholder.setText(update_email)

    def getting_stocks(self):
        score = self.lineEdit_scoreholder.text()
        score = int(score)
        question = int(self.lineEdit_q6.text())
        self.loading.setText("Loading")
        Chart.loading(self)

        if score >= 11 and score <= 23:
            if question == 1:
                user_Buttons_budget.URL = ("https://finviz.com/screener.ashx?v=111&f=cap_mega,ta_sma20_pa,ta_sma200_pa,ta_sma50_pa&ft=4&o=-marketcap")
                lis = testgraph.screener_1(user_Buttons_budget.URL)
                self.btn_1.setText(lis[0])
                self.btn_2.setText(lis[1])
                self.btn_3.setText(lis[2])
                self.btn_4.setText(lis[3])
                self.btn_5.setText(lis[4])
                self.btn_6.setText(lis[5])
                self.btn_7.setText(lis[6])
                self.btn_8.setText(lis[7])

            elif question == 2:
                user_Buttons_budget.URL = ("https://finviz.com/screener.ashx?v=111&f=cap_mega,ta_sma20_pa,ta_sma200_pa,ta_sma50_pa&ft=4&o=-change")
                lis = testgraph.screener_1(user_Buttons_budget.URL)
                self.btn_1.setText(lis[0])
                self.btn_2.setText(lis[1])
                self.btn_3.setText(lis[2])
                self.btn_4.setText(lis[3])
                self.btn_5.setText(lis[4])
                self.btn_6.setText(lis[5])
                self.btn_7.setText(lis[6])
                self.btn_8.setText(lis[7])

            elif question == 3:
                user_Buttons_budget.URL = ("https://finviz.com/screener.ashx?v=111&f=cap_mega,ta_sma20_pa,ta_sma200_pa,ta_sma50_pa&ft=4&o=-volume")
                lis = testgraph.screener_1(user_Buttons_budget.URL)
                self.btn_1.setText(lis[0])
                self.btn_2.setText(lis[1])
                self.btn_3.setText(lis[2])
                self.btn_4.setText(lis[3])
                self.btn_5.setText(lis[4])
                self.btn_6.setText(lis[5])
                self.btn_7.setText(lis[6])
                self.btn_8.setText(lis[7])

            elif question == 4:
                user_Buttons_budget.URL = ("https://finviz.com/screener.ashx?v=141&f=cap_mega,ta_sma20_pa,ta_sma200_pa,ta_sma50_pa&ft=4&o=-relativevolume")
                lis = testgraph.screener_1(user_Buttons_budget.URL)
                self.btn_1.setText(lis[0])
                self.btn_2.setText(lis[1])
                self.btn_3.setText(lis[2])
                self.btn_4.setText(lis[3])
                self.btn_5.setText(lis[4])
                self.btn_6.setText(lis[5])
                self.btn_7.setText(lis[6])
                self.btn_8.setText(lis[7])


        elif score >= 24 and score <= 34:
            if question == 1:
                user_Buttons_budget.URL = ("https://finviz.com/screener.ashx?v=111&f=cap_large,ta_sma20_pa,ta_sma200_pa,ta_sma50_pa&ft=4&o=-marketcap")
                lis = testgraph.screener_1(user_Buttons_budget.URL)
                self.btn_1.setText(lis[0])
                self.btn_2.setText(lis[1])
                self.btn_3.setText(lis[2])
                self.btn_4.setText(lis[3])
                self.btn_5.setText(lis[4])
                self.btn_6.setText(lis[5])
                self.btn_7.setText(lis[6])
                self.btn_8.setText(lis[7])

            elif question == 2:
                user_Buttons_budget.URL = ("https://finviz.com/screener.ashx?v=111&f=cap_large,ta_sma20_pb,ta_sma200_pa,ta_sma50_pa&ft=4&o=-marketcap")
                lis = testgraph.screener_1(user_Buttons_budget.URL)
                self.btn_1.setText(lis[0])
                self.btn_2.setText(lis[1])
                self.btn_3.setText(lis[2])
                self.btn_4.setText(lis[3])
                self.btn_5.setText(lis[4])
                self.btn_6.setText(lis[5])
                self.btn_7.setText(lis[6])
                self.btn_8.setText(lis[7])

            elif question == 3:
                user_Buttons_budget.URL = ("https://finviz.com/screener.ashx?v=111&f=cap_mid,ta_sma20_pa,ta_sma200_pa,ta_sma50_pa&ft=4&o=-volume")
                lis = testgraph.screener_1(user_Buttons_budget.URL)
                self.btn_1.setText(lis[0])
                self.btn_2.setText(lis[1])
                self.btn_3.setText(lis[2])
                self.btn_4.setText(lis[3])
                self.btn_5.setText(lis[4])
                self.btn_6.setText(lis[5])
                self.btn_7.setText(lis[6])
                self.btn_8.setText(lis[7])

            elif question == 4:
                user_Buttons_budget.URL = ("https://finviz.com/screener.ashx?v=111&f=cap_mid,ta_sma20_pb,ta_sma200_pa,ta_sma50_pa&ft=4&o=-relativevolume")
                lis = testgraph.screener_1(user_Buttons_budget.URL)
                self.btn_1.setText(lis[0])
                self.btn_2.setText(lis[1])
                self.btn_3.setText(lis[2])
                self.btn_4.setText(lis[3])
                self.btn_5.setText(lis[4])
                self.btn_6.setText(lis[5])
                self.btn_7.setText(lis[6])
                self.btn_8.setText(lis[7])


        elif score >= 35 and score <= 47:
            if question == 1:
                user_Buttons_budget.URL = ("https://finviz.com/screener.ashx?v=141&f=cap_midunder,ta_sma20_pa20,ta_sma200_pa,ta_sma50_pa&ft=4&o=-volume")
                lis = testgraph.screener_1(user_Buttons_budget.URL)
                self.btn_1.setText(lis[0])
                self.btn_2.setText(lis[1])
                self.btn_3.setText(lis[2])
                self.btn_4.setText(lis[3])
                self.btn_5.setText(lis[4])
                self.btn_6.setText(lis[5])
                self.btn_7.setText(lis[6])
                self.btn_8.setText(lis[7])

            elif question == 2:
                user_Buttons_budget.URL = ("https://finviz.com/screener.ashx?v=141&f=cap_midunder,ta_sma20_pa30,ta_sma200_pa,ta_sma50_pa&ft=4&o=-volume")
                lis = testgraph.screener_1(user_Buttons_budget.URL)
                self.btn_1.setText(lis[0])
                self.btn_2.setText(lis[1])
                self.btn_3.setText(lis[2])
                self.btn_4.setText(lis[3])
                self.btn_5.setText(lis[4])
                self.btn_6.setText(lis[5])
                self.btn_7.setText(lis[6])
                self.btn_8.setText(lis[7])

            elif question == 3:
                user_Buttons_budget.URL = ("https://finviz.com/screener.ashx?v=111&f=cap_midunder,ta_sma20_pa,ta_sma200_pa,ta_sma50_pa&ft=4&o=-volume")
                lis = testgraph.screener_1(user_Buttons_budget.URL)
                self.btn_1.setText(lis[0])
                self.btn_2.setText(lis[1])
                self.btn_3.setText(lis[2])
                self.btn_4.setText(lis[3])
                self.btn_5.setText(lis[4])
                self.btn_6.setText(lis[5])
                self.btn_7.setText(lis[6])
                self.btn_8.setText(lis[7])

            elif question == 4:
                user_Buttons_budget.URL = ("https://finviz.com/screener.ashx?v=111&f=cap_smallunder&ft=4&o=-relativevolume")
                lis = testgraph.screener_1(user_Buttons_budget.URL)
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

        self.loading.setText("")

        self.btn_more.setEnabled(True)

    def more_stocks(self):
        self.label_72.setText("Stonks Page Loading!")
        Chart.loading(self)

        # User Recommended from Finviz

        symbol_list, names_list, percents_list = testgraph.screener_2(user_Buttons_budget.URL)
        print("User Picks\n", symbol_list, names_list, percents_list)

        self.label_sym_5_0.setText(symbol_list[0])
        self.label_sym_5_1.setText(symbol_list[1])
        self.label_sym_5_2.setText(symbol_list[2])
        self.label_sym_5_3.setText(symbol_list[3])
        self.label_sym_5_4.setText(symbol_list[4])
        self.label_sym_5_5.setText(symbol_list[5])
        self.label_sym_5_6.setText(symbol_list[6])
        self.label_sym_5_7.setText(symbol_list[7])
        self.label_sym_5_8.setText(symbol_list[8])
        self.label_sym_5_9.setText(symbol_list[9])

        self.label_name_5_0.setText(names_list[0])
        self.label_name_5_1.setText(names_list[1])
        self.label_name_5_2.setText(names_list[2])
        self.label_name_5_3.setText(names_list[3])
        self.label_name_5_4.setText(names_list[4])
        self.label_name_5_5.setText(names_list[5])
        self.label_name_5_6.setText(names_list[6])
        self.label_name_5_7.setText(names_list[7])
        self.label_name_5_8.setText(names_list[8])
        self.label_name_5_9.setText(names_list[9])

        percent_color = []
        style_sheet_red = "color: rgb(255,0,0)"
        style_sheet_green = "color: rgb(0,255,0)"

        for percent in percents_list:
            percent = percent.replace("%", "")
            percent_color.append(float(percent))

        if percent_color[0] < 0.0:
            self.label_percent_5_0.setStyleSheet(style_sheet_red)
            self.label_percent_5_0.setText(percents_list[0])
        else:
            self.label_percent_5_0.setStyleSheet(style_sheet_green)
            self.label_percent_5_0.setText(percents_list[0])

        if percent_color[1] < 0.0:
            self.label_percent_5_1.setStyleSheet(style_sheet_red)
            self.label_percent_5_1.setText(percents_list[1])
        else:
            self.label_percent_5_1.setStyleSheet(style_sheet_green)
            self.label_percent_5_1.setText(percents_list[1])

        if percent_color[2] < 0.0:
            self.label_percent_5_2.setStyleSheet(style_sheet_red)
            self.label_percent_5_2.setText(percents_list[2])
        else:
            self.label_percent_5_2.setStyleSheet(style_sheet_green)
            self.label_percent_5_2.setText(percents_list[2])

        if percent_color[3] < 0.0:
            self.label_percent_5_3.setStyleSheet(style_sheet_red)
            self.label_percent_5_3.setText(percents_list[3])
        else:
            self.label_percent_5_3.setStyleSheet(style_sheet_green)
            self.label_percent_5_3.setText(percents_list[3])

        if percent_color[4] < 0.0:
            self.label_percent_5_4.setStyleSheet(style_sheet_red)
            self.label_percent_5_4.setText(percents_list[4])
        else:
            self.label_percent_5_4.setStyleSheet(style_sheet_green)
            self.label_percent_5_4.setText(percents_list[4])

        if percent_color[5] < 0.0:
            self.label_percent_5_5.setStyleSheet(style_sheet_red)
            self.label_percent_5_5.setText(percents_list[5])
        else:
            self.label_percent_5_5.setStyleSheet(style_sheet_green)
            self.label_percent_5_5.setText(percents_list[5])

        if percent_color[6] < 0.0:
            self.label_percent_5_6.setStyleSheet(style_sheet_red)
            self.label_percent_5_6.setText(percents_list[6])
        else:
            self.label_percent_5_6.setStyleSheet(style_sheet_green)
            self.label_percent_5_6.setText(percents_list[6])

        if percent_color[7] < 0.0:
            self.label_percent_5_7.setStyleSheet(style_sheet_red)
            self.label_percent_5_7.setText(percents_list[7])
        else:
            self.label_percent_5_7.setStyleSheet(style_sheet_green)
            self.label_percent_5_7.setText(percents_list[7])

        if percent_color[8] < 0.0:
            self.label_percent_5_8.setStyleSheet(style_sheet_red)
            self.label_percent_5_8.setText(percents_list[8])
        else:
            self.label_percent_5_8.setStyleSheet(style_sheet_green)
            self.label_percent_5_8.setText(percents_list[8])

        if percent_color[9] < 0.0:
            self.label_percent_5_9.setStyleSheet(style_sheet_red)
            self.label_percent_5_9.setText(percents_list[9])
        else:
            self.label_percent_5_9.setStyleSheet(style_sheet_green)
            self.label_percent_5_9.setText(percents_list[9])

        # Top Gainers from Finviz

        gainers = "https://finviz.com/screener.ashx?v=111&s=ta_topgainers&ft=4"
        symbol_list, names_list, percents_list = testgraph.screener_2(gainers)
        print("Gainers\n", symbol_list, names_list, percents_list)

        self.label_sym_3_0.setText(symbol_list[0])
        self.label_sym_3_1.setText(symbol_list[1])
        self.label_sym_3_2.setText(symbol_list[2])
        self.label_sym_3_3.setText(symbol_list[3])
        self.label_sym_3_4.setText(symbol_list[4])
        self.label_sym_3_5.setText(symbol_list[5])
        self.label_sym_3_6.setText(symbol_list[6])
        self.label_sym_3_7.setText(symbol_list[7])
        self.label_sym_3_8.setText(symbol_list[8])
        self.label_sym_3_9.setText(symbol_list[9])

        self.label_name_3_0.setText(names_list[0])
        self.label_name_3_1.setText(names_list[1])
        self.label_name_3_2.setText(names_list[2])
        self.label_name_3_3.setText(names_list[3])
        self.label_name_3_4.setText(names_list[4])
        self.label_name_3_5.setText(names_list[5])
        self.label_name_3_6.setText(names_list[6])
        self.label_name_3_7.setText(names_list[7])
        self.label_name_3_8.setText(names_list[8])
        self.label_name_3_9.setText(names_list[9])

        self.label_percent_3_0.setText(percents_list[0])
        self.label_percent_3_1.setText(percents_list[1])
        self.label_percent_3_2.setText(percents_list[2])
        self.label_percent_3_3.setText(percents_list[3])
        self.label_percent_3_4.setText(percents_list[4])
        self.label_percent_3_5.setText(percents_list[5])
        self.label_percent_3_6.setText(percents_list[6])
        self.label_percent_3_7.setText(percents_list[7])
        self.label_percent_3_8.setText(percents_list[8])
        self.label_percent_3_9.setText(percents_list[9])

        # Top Losers from Finviz

        losers = "https://finviz.com/screener.ashx?v=111&s=ta_toplosers"
        symbol_list, names_list, percents_list = testgraph.screener_2(losers)
        print("Losers\n", symbol_list, names_list, percents_list)

        self.label_sym_4_0.setText(symbol_list[0])
        self.label_sym_4_1.setText(symbol_list[1])
        self.label_sym_4_2.setText(symbol_list[2])
        self.label_sym_4_3.setText(symbol_list[3])
        self.label_sym_4_4.setText(symbol_list[4])
        self.label_sym_4_5.setText(symbol_list[5])
        self.label_sym_4_6.setText(symbol_list[6])
        self.label_sym_4_7.setText(symbol_list[7])
        self.label_sym_4_8.setText(symbol_list[8])
        self.label_sym_4_9.setText(symbol_list[9])

        self.label_name_4_0.setText(names_list[0])
        self.label_name_4_1.setText(names_list[1])
        self.label_name_4_2.setText(names_list[2])
        self.label_name_4_3.setText(names_list[3])
        self.label_name_4_4.setText(names_list[4])
        self.label_name_4_5.setText(names_list[5])
        self.label_name_4_6.setText(names_list[6])
        self.label_name_4_7.setText(names_list[7])
        self.label_name_4_8.setText(names_list[8])
        self.label_name_4_9.setText(names_list[9])

        self.label_percent_4_0.setText(percents_list[0])
        self.label_percent_4_1.setText(percents_list[1])
        self.label_percent_4_2.setText(percents_list[2])
        self.label_percent_4_3.setText(percents_list[3])
        self.label_percent_4_4.setText(percents_list[4])
        self.label_percent_4_5.setText(percents_list[5])
        self.label_percent_4_6.setText(percents_list[6])
        self.label_percent_4_7.setText(percents_list[7])
        self.label_percent_4_8.setText(percents_list[8])
        self.label_percent_4_9.setText(percents_list[9])

        # Top Gainers from Yahoo Finance

        symbol_list, names_list, percents_list = testgraph.top_gainers()

        self.label_sym_0_0.setText(symbol_list[0])
        self.label_sym_0_1.setText(symbol_list[1])
        self.label_sym_0_2.setText(symbol_list[2])
        self.label_sym_0_3.setText(symbol_list[3])
        self.label_sym_0_4.setText(symbol_list[4])
        self.label_sym_0_5.setText(symbol_list[5])
        self.label_sym_0_6.setText(symbol_list[6])
        self.label_sym_0_7.setText(symbol_list[7])
        self.label_sym_0_8.setText(symbol_list[8])
        self.label_sym_0_9.setText(symbol_list[9])

        self.label_name_0_0.setText(names_list[0])
        self.label_name_0_1.setText(names_list[1])
        self.label_name_0_2.setText(names_list[2])
        self.label_name_0_3.setText(names_list[3])
        self.label_name_0_4.setText(names_list[4])
        self.label_name_0_5.setText(names_list[5])
        self.label_name_0_6.setText(names_list[6])
        self.label_name_0_7.setText(names_list[7])
        self.label_name_0_8.setText(names_list[8])
        self.label_name_0_9.setText(names_list[9])

        self.label_percent_0_0.setText(percents_list[0])
        self.label_percent_0_1.setText(percents_list[1])
        self.label_percent_0_2.setText(percents_list[2])
        self.label_percent_0_3.setText(percents_list[3])
        self.label_percent_0_4.setText(percents_list[4])
        self.label_percent_0_5.setText(percents_list[5])
        self.label_percent_0_6.setText(percents_list[6])
        self.label_percent_0_7.setText(percents_list[7])
        self.label_percent_0_8.setText(percents_list[8])
        self.label_percent_0_9.setText(percents_list[9])

        # Top Losers from Yahoo Finance

        symbol_list, names_list, percents_list = testgraph.top_losers()

        self.label_sym_1_0.setText(symbol_list[0])
        self.label_sym_1_1.setText(symbol_list[1])
        self.label_sym_1_2.setText(symbol_list[2])
        self.label_sym_1_3.setText(symbol_list[3])
        self.label_sym_1_4.setText(symbol_list[4])
        self.label_sym_1_5.setText(symbol_list[5])
        self.label_sym_1_6.setText(symbol_list[6])
        self.label_sym_1_7.setText(symbol_list[7])
        self.label_sym_1_8.setText(symbol_list[8])
        self.label_sym_1_9.setText(symbol_list[9])

        self.label_name_1_0.setText(names_list[0])
        self.label_name_1_1.setText(names_list[1])
        self.label_name_1_2.setText(names_list[2])
        self.label_name_1_3.setText(names_list[3])
        self.label_name_1_4.setText(names_list[4])
        self.label_name_1_5.setText(names_list[5])
        self.label_name_1_6.setText(names_list[6])
        self.label_name_1_7.setText(names_list[7])
        self.label_name_1_8.setText(names_list[8])
        self.label_name_1_9.setText(names_list[9])

        self.label_percent_1_0.setText(percents_list[0])
        self.label_percent_1_1.setText(percents_list[1])
        self.label_percent_1_2.setText(percents_list[2])
        self.label_percent_1_3.setText(percents_list[3])
        self.label_percent_1_4.setText(percents_list[4])
        self.label_percent_1_5.setText(percents_list[5])
        self.label_percent_1_6.setText(percents_list[6])
        self.label_percent_1_7.setText(percents_list[7])
        self.label_percent_1_8.setText(percents_list[8])
        self.label_percent_1_9.setText(percents_list[9])

        # Most Active from Finviz

        symbol_list, names_list, percents_list = testgraph.screener_2("https://finviz.com/screener.ashx?v=111&s=ta_mostactive")
        print("Most Active\n", symbol_list, names_list, percents_list)

        self.label_sym_2_0.setText(symbol_list[0])
        self.label_sym_2_1.setText(symbol_list[1])
        self.label_sym_2_2.setText(symbol_list[2])
        self.label_sym_2_3.setText(symbol_list[3])
        self.label_sym_2_4.setText(symbol_list[4])
        self.label_sym_2_5.setText(symbol_list[5])
        self.label_sym_2_6.setText(symbol_list[6])
        self.label_sym_2_7.setText(symbol_list[7])
        self.label_sym_2_8.setText(symbol_list[8])
        self.label_sym_2_9.setText(symbol_list[9])

        self.label_name_2_0.setText(names_list[0])
        self.label_name_2_1.setText(names_list[1])
        self.label_name_2_2.setText(names_list[2])
        self.label_name_2_3.setText(names_list[3])
        self.label_name_2_4.setText(names_list[4])
        self.label_name_2_5.setText(names_list[5])
        self.label_name_2_6.setText(names_list[6])
        self.label_name_2_7.setText(names_list[7])
        self.label_name_2_8.setText(names_list[8])
        self.label_name_2_9.setText(names_list[9])

        percent_color = []
        style_sheet_red = "color: rgb(255,0,0)"
        style_sheet_green = "color: rgb(0,255,0)"

        for percent in percents_list:
            percent = percent.replace("%", "")
            percent_color.append(float(percent))

        if percent_color[0] < 0.0:
            self.label_percent_2_0.setStyleSheet(style_sheet_red)
            self.label_percent_2_0.setText(percents_list[0])
        else:
            self.label_percent_2_0.setStyleSheet(style_sheet_green)
            self.label_percent_2_0.setText(percents_list[0])

        if percent_color[1] < 0.0:
            self.label_percent_2_1.setStyleSheet(style_sheet_red)
            self.label_percent_2_1.setText(percents_list[1])
        else:
            self.label_percent_2_1.setStyleSheet(style_sheet_green)
            self.label_percent_2_1.setText(percents_list[1])

        if percent_color[2] < 0.0:
            self.label_percent_2_2.setStyleSheet(style_sheet_red)
            self.label_percent_2_2.setText(percents_list[2])
        else:
            self.label_percent_2_2.setStyleSheet(style_sheet_green)
            self.label_percent_2_2.setText(percents_list[2])

        if percent_color[3] < 0.0:
            self.label_percent_2_3.setStyleSheet(style_sheet_red)
            self.label_percent_2_3.setText(percents_list[3])
        else:
            self.label_percent_2_3.setStyleSheet(style_sheet_green)
            self.label_percent_2_3.setText(percents_list[3])

        if percent_color[4] < 0.0:
            self.label_percent_2_4.setStyleSheet(style_sheet_red)
            self.label_percent_2_4.setText(percents_list[4])
        else:
            self.label_percent_2_4.setStyleSheet(style_sheet_green)
            self.label_percent_2_4.setText(percents_list[4])

        if percent_color[5] < 0.0:
            self.label_percent_2_5.setStyleSheet(style_sheet_red)
            self.label_percent_2_5.setText(percents_list[5])
        else:
            self.label_percent_2_5.setStyleSheet(style_sheet_green)
            self.label_percent_2_5.setText(percents_list[5])

        if percent_color[6] < 0.0:
            self.label_percent_2_6.setStyleSheet(style_sheet_red)
            self.label_percent_2_6.setText(percents_list[6])
        else:
            self.label_percent_2_6.setStyleSheet(style_sheet_green)
            self.label_percent_2_6.setText(percents_list[6])

        if percent_color[7] < 0.0:
            self.label_percent_2_7.setStyleSheet(style_sheet_red)
            self.label_percent_2_7.setText(percents_list[7])
        else:
            self.label_percent_2_7.setStyleSheet(style_sheet_green)
            self.label_percent_2_7.setText(percents_list[7])

        if percent_color[8] < 0.0:
            self.label_percent_2_8.setStyleSheet(style_sheet_red)
            self.label_percent_2_8.setText(percents_list[8])
        else:
            self.label_percent_2_8.setStyleSheet(style_sheet_green)
            self.label_percent_2_8.setText(percents_list[8])

        if percent_color[9] < 0.0:
            self.label_percent_2_9.setStyleSheet(style_sheet_red)
            self.label_percent_2_9.setText(percents_list[9])
        else:
            self.label_percent_2_9.setStyleSheet(style_sheet_green)
            self.label_percent_2_9.setText(percents_list[9])

        self.label_72.setText("Stonks Page")

    def saved(self):
        email = self.lineEdit_emailholder.text()
        profits = self.lineEdit_profits.text()
        loses = self.lineEdit_loses.text()

        saved = float(self.Saved.text())
        goal = float(self.Goal.text())
        print(f"Goal: {goal}, Saved: {saved}")

        if profits.isalnum() and loses.isalnum():
            total = float(profits) + (float(loses) * (-1))
            print(total)

            if total >= 0:
                print("profit")
                new = saved + total
                actions.DATABASE(f"update users set saved = '{new}' where email = '{email}' ")
                self.Saved.setText(str(new))
                print(f"Goal: {goal}, Saved: {new}")
                per = float(new) / float(goal) * 100
                if new >= goal:
                    self.progressBar.setValue(100)
                else:
                    print(per)
                    self.progressBar.setValue(per)

            elif total < 0:
                print("loss")
                new = saved + total
                actions.DATABASE(f"update users set saved = '{new}' where email = '{email}' ")
                self.Saved.setText(str(new))
                print(f"Goal: {goal}, Saved: {new}")
                per = float(new) / float(goal) * 100
                if new <= 0:
                    self.progressBar.setValue(0)
                else:
                    print(per)
                    self.progressBar.setValue(per)

        else:
            print("invalid inputs")

    def what_if_price(self):
        symbol = self.lineEdit_symbol_2.text()
        price = testgraph.price(symbol)
        price = float(price)
        price = "{:,.2f}".format(price)
        self.label_price.setText("$" + str(price))

    def process(self):
        shares = self.lineEdit_shares.text()
        pt = float(self.lineEdit_pt.text())
        price = self.label_price.text()
        price = price.replace("$", "")
        price = price.replace(",", "")

        cost = float(price) * int(shares)
        cost = float("{:.2f}".format(cost))
        self.label_cost.setText("$" + str("{:,.2f}".format(cost)))
        self.label_pt.setText("$" + str("{:,.2f}".format(pt)))

        per = ((float(pt)-float(price)) / float(price)) * 100
        per = float("{:.2f}".format(per))
        self.label_per.setText(str(per) + "%")



        g_5 = float(price) * 0.05
        g_5 = float("{:.2f}".format(g_5))
        self.label_price_5.setText("$" + str("{:,.2f}".format(g_5)))

        g_10 = float(price) * 0.10
        g_10 = float("{:.2f}".format(g_10))
        self.label_price_10.setText("$" + str("{:,.2f}".format(g_10)))

        g_25 = float(price) * 0.25
        g_25 = float("{:.2f}".format(g_25))
        self.label_price_25.setText("$" + str("{:,.2f}".format(g_25)))

        g_50 = float(price) * 0.50
        g_50 = float("{:.2f}".format(g_50))
        self.label_price_50.setText("$" + str("{:,.2f}".format(g_50)))

        g_75 = float(price) * 0.75
        g_75 = float("{:.2f}".format(g_75))
        self.label_price_75.setText("$" + str("{:,.2f}".format(g_75)))

        g_100 = float(price) * 1.00
        g_100 = float("{:.2f}".format(g_100))
        self.label_price_100.setText("$" + str("{:,.2f}".format(g_100)))



        s_5 = float(price) + g_5
        s_5 = float("{:.2f}".format(s_5))
        self.label_pt_5.setText("$" + str("{:,.2f}".format(s_5)))

        s_10 = float(price) + g_10
        s_10 = float("{:.2f}".format(s_10))
        self.label_pt_10.setText("$" + str("{:,.2f}".format(s_10)))

        s_25 = float(price) + g_25
        s_25 = float("{:.2f}".format(s_25))
        self.label_pt_25.setText("$" + str("{:,.2f}".format(s_25)))

        s_50 = float(price )+ g_50
        s_50 = float("{:.2f}".format(s_50))
        self.label_pt_50.setText("$" + str("{:,.2f}".format(s_50)))

        s_75 = float(price) + g_75
        s_75 = float("{:.2f}".format(s_75))
        self.label_pt_75.setText("$" + str("{:,.2f}".format(s_75)))

        s_100 = float(price) + g_100
        s_100 = float("{:.2f}".format(s_100))
        self.label_pt_100.setText("$" + str("{:,.2f}".format(s_100)))



        c_5 = float(cost) * 0.05
        print(c_5)
        c_5 = float("{:.2f}".format(c_5))
        self.label_pos_5.setText("$" + str("{:,.2f}".format(c_5)))

        c_10 = float(cost) * 0.10
        c_10 = float("{:.2f}".format(c_10))
        self.label_pos_10.setText("$" + str("{:,.2f}".format(c_10)))

        c_25 = float(cost) * 0.25
        c_25 = float("{:.2f}".format(c_25))
        self.label_pos_25.setText("$" + str("{:,.2f}".format(c_25)))

        c_50 = float(cost) * 0.50
        c_50 = float("{:.2f}".format(c_50))
        self.label_pos_50.setText("$" + str("{:,.2f}".format(c_50)))

        c_75 = float(cost) * 0.75
        c_75 = float("{:.2f}".format(c_75))
        self.label_pos_75.setText("$" + str("{:,.2f}".format(c_75)))

        c_100 = float(cost) * 1.00
        c_100 = float("{:.2f}".format(c_100))
        self.label_pos_100.setText("$" + str("{:,.2f}".format(c_100)))



        pt_5 = float(cost) + c_5
        pt_5 = float("{:.2f}".format(pt_5))
        self.label_post_5.setText("$" + str("{:,.2f}".format(pt_5)))

        pt_10= float(cost) + c_10
        pt_10 = float("{:.2f}".format(pt_10))
        self.label_post_10.setText("$" + str("{:,.2f}".format(pt_10)))

        pt_25 = float(cost) + c_25
        pt_25 = float("{:.2f}".format(pt_25))
        self.label_post_25.setText("$" + str("{:,.2f}".format(pt_25)))

        pt_50 = float(cost) + c_50
        pt_50 = float("{:.2f}".format(pt_50))
        self.label_post_50.setText("$" + str("{:,.2f}".format(pt_50)))

        pt_75 = float(cost) + c_75
        pt_75 = float("{:.2f}".format(pt_75))
        self.label_post_75.setText("$" + str("{:,.2f}".format(pt_75)))

        pt_100 = float(cost) + c_100
        pt_100 = float("{:.2f}".format(pt_100))
        self.label_post_100.setText("$" + str("{:,.2f}".format(pt_100)))

    def clear_what(self):
        self.lineEdit_symbol_2.setText("")
        self.lineEdit_shares.setText("")

        self.lineEdit_pt.setText("")
        self.label_price.setText("....")
        self.label_cost.setText("....")
        self.label_pt.setText("....")
        self.label_per.setText("....")

        self.label_price_5.setText("....")
        self.label_price_10.setText("....")
        self.label_price_25.setText("....")
        self.label_price_50.setText("....")
        self.label_price_75.setText("....")
        self.label_price_100.setText("....")

        self.label_pt_5.setText("....")
        self.label_pt_10.setText("....")
        self.label_pt_25.setText("....")
        self.label_pt_50.setText("....")
        self.label_pt_75.setText("....")
        self.label_pt_100.setText("....")

        self.label_pos_5.setText("....")
        self.label_pos_10.setText("....")
        self.label_pos_25.setText("....")
        self.label_pos_50.setText("....")
        self.label_pos_75.setText("....")
        self.label_pos_100.setText("....")

        self.label_post_5.setText("....")
        self.label_post_10.setText("....")
        self.label_post_25.setText("....")
        self.label_post_50.setText("....")
        self.label_post_75.setText("....")
        self.label_post_100.setText("....")

    def clear_more(self):
        self.label_sym_5_0.setText("....")
        self.label_sym_5_1.setText("....")
        self.label_sym_5_2.setText("....")
        self.label_sym_5_3.setText("....")
        self.label_sym_5_4.setText("....")
        self.label_sym_5_5.setText("....")
        self.label_sym_5_6.setText("....")
        self.label_sym_5_7.setText("....")
        self.label_sym_5_8.setText("....")
        self.label_sym_5_9.setText("....")

        self.label_name_5_0.setText("....")
        self.label_name_5_1.setText("....")
        self.label_name_5_2.setText("....")
        self.label_name_5_3.setText("....")
        self.label_name_5_4.setText("....")
        self.label_name_5_5.setText("....")
        self.label_name_5_6.setText("....")
        self.label_name_5_7.setText("....")
        self.label_name_5_8.setText("....")
        self.label_name_5_9.setText("....")

        self.label_sym_3_4.setText("....")
        self.label_sym_3_5.setText("....")
        self.label_sym_3_6.setText("....")
        self.label_sym_3_7.setText("....")
        self.label_sym_3_8.setText("....")
        self.label_sym_3_9.setText("....")

        self.label_name_3_0.setText("....")
        self.label_name_3_1.setText("....")
        self.label_name_3_2.setText("....")
        self.label_name_3_3.setText("....")
        self.label_name_3_4.setText("....")
        self.label_name_3_5.setText("....")
        self.label_name_3_6.setText("....")
        self.label_name_3_7.setText("....")
        self.label_name_3_8.setText("....")
        self.label_name_3_9.setText("....")

        self.label_percent_3_0.setText("....")
        self.label_percent_3_1.setText("....")
        self.label_percent_3_2.setText("....")
        self.label_percent_3_3.setText("....")
        self.label_percent_3_4.setText("....")
        self.label_percent_3_5.setText("....")
        self.label_percent_3_6.setText("....")
        self.label_percent_3_7.setText("....")
        self.label_percent_3_8.setText("....")
        self.label_percent_3_9.setText("....")

        self.label_sym_4_0.setText("....")
        self.label_sym_4_1.setText("....")
        self.label_sym_4_2.setText("....")
        self.label_sym_4_3.setText("....")
        self.label_sym_4_4.setText("....")
        self.label_sym_4_5.setText("....")
        self.label_sym_4_6.setText("....")
        self.label_sym_4_7.setText("....")
        self.label_sym_4_8.setText("....")
        self.label_sym_4_9.setText("....")

        self.label_name_4_0.setText("....")
        self.label_name_4_1.setText("....")
        self.label_name_4_2.setText("....")
        self.label_name_4_3.setText("....")
        self.label_name_4_4.setText("....")
        self.label_name_4_5.setText("....")
        self.label_name_4_6.setText("....")
        self.label_name_4_7.setText("....")
        self.label_name_4_8.setText("....")
        self.label_name_4_9.setText("....")

        self.label_percent_4_0.setText("....")
        self.label_percent_4_1.setText("....")
        self.label_percent_4_2.setText("....")
        self.label_percent_4_3.setText("....")
        self.label_percent_4_4.setText("....")
        self.label_percent_4_5.setText("....")
        self.label_percent_4_6.setText("....")
        self.label_percent_4_7.setText("....")
        self.label_percent_4_8.setText("....")
        self.label_percent_4_9.setText("....")

        self.label_sym_0_0.setText("....")
        self.label_sym_0_1.setText("....")
        self.label_sym_0_2.setText("....")
        self.label_sym_0_3.setText("....")
        self.label_sym_0_4.setText("....")
        self.label_sym_0_5.setText("....")
        self.label_sym_0_6.setText("....")
        self.label_sym_0_7.setText("....")
        self.label_sym_0_8.setText("....")
        self.label_sym_0_9.setText("....")

        self.label_name_0_0.setText("....")
        self.label_name_0_1.setText("....")
        self.label_name_0_2.setText("....")
        self.label_name_0_3.setText("....")
        self.label_name_0_4.setText("....")
        self.label_name_0_5.setText("....")
        self.label_name_0_6.setText("....")
        self.label_name_0_7.setText("....")
        self.label_name_0_8.setText("....")
        self.label_name_0_9.setText("....")

        self.label_percent_0_0.setText("....")
        self.label_percent_0_1.setText("....")
        self.label_percent_0_2.setText("....")
        self.label_percent_0_3.setText("....")
        self.label_percent_0_4.setText("....")
        self.label_percent_0_5.setText("....")
        self.label_percent_0_6.setText("....")
        self.label_percent_0_7.setText("....")
        self.label_percent_0_8.setText("....")
        self.label_percent_0_9.setText("....")

        self.label_sym_1_0.setText("....")
        self.label_sym_1_1.setText("....")
        self.label_sym_1_2.setText("....")
        self.label_sym_1_3.setText("....")
        self.label_sym_1_4.setText("....")
        self.label_sym_1_5.setText("....")
        self.label_sym_1_6.setText("....")
        self.label_sym_1_7.setText("....")
        self.label_sym_1_8.setText("....")
        self.label_sym_1_9.setText("....")

        self.label_name_1_0.setText("....")
        self.label_name_1_1.setText("....")
        self.label_name_1_2.setText("....")
        self.label_name_1_3.setText("....")
        self.label_name_1_4.setText("....")
        self.label_name_1_5.setText("....")
        self.label_name_1_6.setText("....")
        self.label_name_1_7.setText("....")
        self.label_name_1_8.setText("....")
        self.label_name_1_9.setText("....")

        self.label_percent_1_0.setText("....")
        self.label_percent_1_1.setText("....")
        self.label_percent_1_2.setText("....")
        self.label_percent_1_3.setText("....")
        self.label_percent_1_4.setText("....")
        self.label_percent_1_5.setText("....")
        self.label_percent_1_6.setText("....")
        self.label_percent_1_7.setText("....")
        self.label_percent_1_8.setText("....")
        self.label_percent_1_9.setText("....")

        self.label_sym_2_0.setText("....")
        self.label_sym_2_1.setText("....")
        self.label_sym_2_2.setText("....")
        self.label_sym_2_3.setText("....")
        self.label_sym_2_4.setText("....")
        self.label_sym_2_5.setText("....")
        self.label_sym_2_6.setText("....")
        self.label_sym_2_7.setText("....")
        self.label_sym_2_8.setText("....")
        self.label_sym_2_9.setText("....")

        self.label_name_2_0.setText("....")
        self.label_name_2_1.setText("....")
        self.label_name_2_2.setText("....")
        self.label_name_2_3.setText("....")
        self.label_name_2_4.setText("....")
        self.label_name_2_5.setText("....")
        self.label_name_2_6.setText("....")
        self.label_name_2_7.setText("....")
        self.label_name_2_8.setText("....")
        self.label_name_2_9.setText("....")

        self.label_percent_5_0.setText("....")
        self.label_percent_5_1.setText("....")
        self.label_percent_5_2.setText("....")
        self.label_percent_5_3.setText("....")
        self.label_percent_5_4.setText("....")
        self.label_percent_5_5.setText("....")
        self.label_percent_5_6.setText("....")
        self.label_percent_5_7.setText("....")
        self.label_percent_5_8.setText("....")
        self.label_percent_5_9.setText("....")

        self.label_percent_2_0.setText("....")
        self.label_percent_2_1.setText("....")
        self.label_percent_2_2.setText("....")
        self.label_percent_2_3.setText("....")
        self.label_percent_2_4.setText("....")
        self.label_percent_2_2.setText("....")
        self.label_percent_2_6.setText("....")
        self.label_percent_2_7.setText("....")
        self.label_percent_2_8.setText("....")
        self.label_percent_2_9.setText("....")

    def logout(self):
            # Resetting default pages
            self.stackedWidget.setCurrentWidget(self.login_page)
            self.stackedWidget_2.setCurrentWidget(self.chart_page)
            self.stackedWidget_3.setCurrentWidget(self.page_3)
            self.stackedWidget_4.setCurrentWidget(self.user_tops)

            # Resetting the default finance labels
            self.income.setText("....")
            self.expenses.setText("....")
            self.Saved.setText("....")
            self.Goal.setText("....")

            # Clearing any entries in the budget info page
            self.lineEdit_primary.clear()
            self.lineEdit_secondary.clear()
            self.lineEdit_acct_size.clear()
            self.lineEdit_goal.clear()
            self.lineEdit_rent.clear()
            self.lineEdit_utilities.clear()
            self.lineEdit_groceries.clear()
            self.lineEdit_insurance.clear()
            self.lineEdit_other.clear()
            self.lineEdit_profits.clear()
            self.lineEdit_loses.clear()

            # Clearing the what if page
            user_Buttons_budget.clear_what(self)

            # Clearing the summary section and the user picks/indices
            self.frame_116.setEnabled(False)
            self.loading.setText("")
            self.lbl_name.setText("....")
            self.lbl_exchange.setText("....")
            self.lbl_sector.setText("....")
            self.lbl_industry.setText("....")
            self.lbl_ask.setText("....")
            self.lbl_bid.setText("....")
            self.lbl_open.setText("....")
            self.lbl_close.setText("....")
            self.lbl_yield.setText("....")
            self.lbl_pe.setText("....")
            self.lbl_tenvol.setText("....")
            self.lbl_vol.setText("....")
            self.lbl_summary.setText("....")

            self.lineEdit_symbol.clear

            self.btn_1.setText("....")
            self.btn_2.setText("....")
            self.btn_3.setText("....")
            self.btn_4.setText("....")
            self.btn_5.setText("....")
            self.btn_6.setText("....")
            self.btn_7.setText("....")
            self.btn_8.setText("....")
            self.btn_more.setEnabled(False)

            self.btn_DOW_quote.setText("....")
            self.btn_NAS_quote.setText("....")
            self.btn_SP_quote.setText("....")
            self.btn_RUSS_quote.setText("....")

            user_Buttons_budget.clear_more(self)

            self.btn_login_signup.setText("Login/Sign up")