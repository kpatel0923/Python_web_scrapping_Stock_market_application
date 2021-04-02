import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import actions
import re

#files
import actions


class User:
    def __init__(self, email, first, last, password, age, bills, account_size, goal, score):
        self.__email = email
        self.__first = first
        self.__last = last
        self.__password = password
        self.__age = age
        self.__bills = bills
        self.__account_size = account_size
        self.__goal = goal
        self.__score = score

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

    def getAge(self):
        return self.__age

    def getBills(self):
        return self.__bills

    def getAccount_size(self):
        return self.__account_size

    def getGoal(self):
        return self.__goal

    def __str__(self):
        return f" Email: {self.__email} \
                  first: {self.__first} \
                  last:  {self.__last}  \
                  password: {self.__password} \
                  age: {self.__age} \
                  bills: {self.__bills} \
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
            self.lbl_welcome.setText(f"Welcome: {Login.current_user.getFirst(), Login.current_user.getScore()}")
            Login.clear(self)


    @staticmethod
    def getUser(self):
        return Login.current_user



#  current_user = Login.getUser()

#  DATABASE("update user set age == {10} where email == {current_user.getEmail()}")

#  DATABASE("select * from user where bills == {current_user.getBills()} ")