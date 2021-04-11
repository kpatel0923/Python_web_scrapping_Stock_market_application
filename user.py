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

    URL = None

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
        symbol_list, names_list, percents_list = testgraph.screener_2(user_Buttons_budget.URL)
        print("User Picks\n", symbol_list, names_list, percents_list)

        gainers = "https://finviz.com/screener.ashx?v=111&s=ta_topgainers&ft=4"
        symbol_list, names_list, percents_list = testgraph.screener_2(gainers)
        print("Gainers\n", symbol_list, names_list, percents_list)

        losers = "https://finviz.com/screener.ashx?v=111&s=ta_toplosers"
        symbol_list, names_list, percents_list = testgraph.screener_2(losers)
        print("Losers\n", symbol_list, names_list, percents_list)

        #call the screener_2 twice for the tops and bottoms

        #call andy's functions here also
        stockList = testgraph.topGainers()
        print(stockList)



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


