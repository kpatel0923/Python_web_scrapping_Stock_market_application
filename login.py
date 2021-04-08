import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import actions
import re

#files
import actions


class User:
    def __init__(self, email, first, last, password, account_size, goal, saved, score, income, expenses, q5, q8):
        self.__email = email
        self.__first = first
        self.__last = last
        self.__password = password
        self.__account_size = account_size
        self.__goal = goal
        self.__saved = saved
        self.__score = score
        self.__income = income
        self.__expenses = expenses
        self.__q5 = q5
        self.__q8 = q8


    def getEmail(self):
        return self.__email

    def getFirst(self):
        return self.__first

    def setFirst(self,new_name):
        pass
        # DATABASE(update users set first == {new_name} where email == {self.__email})

    def setScore(self, score):
        pass

    def getScore(self):
        return self.__score

    def getLast(self):
        return self.__last

    def getPassword(self):
        return self.__password

    def getAccount_size(self):
        return self.__account_size

    def getGoal(self):
        return self.__goal

    def getIncome(self):
        return self.__income

    def getExpenses(self):
        return self.__expenses

    def getQ5(self):
        return self.__q5

    def getQ8(self):
        return self.__q8

    def getSaved(self):
        return self.__saved

    def __str__(self):
        return f" Email: {self.__email} \
                  first: {self.__first} \
                  last:  {self.__last}  \
                  password: {self.__password} \
                  account_size: {self.__account_size} \
                  goal: {self.__goal} \
                  score: {self.__score}"


class Login(QMainWindow):

    current_user = None

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def loginPage(self):
        self.stackedWidget.setCurrentWidget(self.login_page)
        self.btn_login_signup.setText("Login/Sign up")

    def clear(self):
        self.lineEdit_email.clear()
        self.lineEdit_password.clear()

    def handleLogin(self):
        email = self.lineEdit_email.text()
        password = self.lineEdit_password.text()
        person = actions.DATABASE(f"select * from users where email  == '{email}' and password == '{password}'")

        if not password.isalnum():
            print("Invalid input(s)y")

        elif not re.search("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)" , email):
            print('Invalid input(s)')

        elif not person:
            print("Invalid login")

        else:
            print("success")
            Login.current_user = User(*person[0])
            print(Login.current_user)
            self.stackedWidget.setCurrentWidget(self.user_page)
            self.btn_login_signup.setText("Logout")
            self.lineEdit_first_2.setText(Login.current_user.getFirst())
            self.lineEdit_last_2.setText(Login.current_user.getLast())
            self.lineEdit_useremail.setText(Login.current_user.getEmail())
            self.lineEdit_emailholder.setText(Login.current_user.getEmail())
            self.lineEdit_scoreholder.setText(str(Login.current_user.getScore()))
            self.lineEdit_goalholder.setText(str(Login.current_user.getGoal()))
            self.lineEdit_income.setText(str(Login.current_user.getIncome()))
            self.lineEdit_expenses.setText(str(Login.current_user.getExpenses()))
            self.income.setText(str(Login.current_user.getIncome()))
            self.expenses.setText(str(Login.current_user.getExpenses()))
            self.Saved.setText(str(Login.current_user.getSaved()))
            self.Goal.setText(str(Login.current_user.getGoal()))

            self.lineEdit_q5.setText(str(Login.current_user.getQ5()))
            self.lineEdit_q8.setText(str(Login.current_user.getQ8()))
            print("Email: ", self.lineEdit_emailholder.text(), "Score: ", self.lineEdit_scoreholder.text())
            self.lbl_welcome.setText(f"Welcome: {Login.current_user.getFirst()}")
            Login.clear(self)


    @staticmethod
    def getUser(self):
        return Login.current_user



#  current_user = Login.getUser()

#  DATABASE("update user set age == {10} where email == {current_user.getEmail()}")

#  DATABASE("select * from user where bills == {current_user.getBills()} ")