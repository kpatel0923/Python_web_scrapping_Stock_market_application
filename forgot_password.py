from PyQt5.QtWidgets import *
import re
import random
import smtplib

#files
import actions
from error_messages import *

def send_email(code,user_email):
    # Email sender
    print("sending")

    password = "Teamafk123"
    sender = "team2afk@gmail.com"
    rec = user_email

    SUBJECT = "Reset Password test"
    TEXT = f"Hey, Please use the code below to reset your password. \nHere is your CODE: {code} \n" \
           f"\nThanks, \nAFK team"
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    print("Login success")
    server.sendmail(sender, rec, message)
    print("Email has been sent to ", rec)
    #print(f"The code is: {code}")


class Password(QMainWindow):

    valid_code = None
    email = None

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def clear(self):
        self.lineEdit_email_send.clear()
        self.lineEdit_code.clear()
        self.lineEdit_pass.clear()
        self.lineEdit_pass_2.clear()
        self.label_19.clear()
        self.lbl_pass.clear()

    def handleSend(self):
        Password.email = self.lineEdit_email_send.text()

        if not re.search("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", Password.email):
            print('Invalid input(s)')
            ForgotPass_Messages.error_1(self)

        elif not actions.DATABASE(f"select * from users where email  == '{Password.email}'"):
            print('Not in Database')
            ForgotPass_Messages.error_2(self)

        else:
            # Email sender
            ForgotPass_Messages.error_5(self)
            Password.valid_code = Password.random_code(self)
            send_email(Password.valid_code, Password.email)
            self.lineEdit_code.setEnabled(True)
            self.btn_continue.setEnabled(True)
            self.lbl_pass.setText("Email Sent")

    def code(self):
        code = self.lineEdit_code.text()
        sent_code = Password.valid_code
        print(f"The code is W: {sent_code}")
        if code.isalnum:
            if int(code) != int(sent_code):
                print("Invalid code")
                ForgotPass_Messages.error_3(self)
            else:
                self.stackedWidget.setCurrentWidget(self.password_reset_page)
                Password.clear(self)
                self.lineEdit_code.setEnabled(False)
                self.btn_continue.setEnabled(False)
        else:
            print("Enter valid code")

    def handleReset(self):
        password = self.lineEdit_pass.text()
        confirm_password = self.lineEdit_pass_2.text()
        print(password, confirm_password)

        if password == confirm_password:
            actions.DATABASE(f"update users set password = '{password}' where email = '{Password.email}' ")
            if self.btn_login_signup.text() == "Logout":
                self.stackedWidget.setCurrentWidget(self.user_page)
                Password.clear(self)
                self.lineEdit_code.setEnabled(False)
                self.btn_continue.setEnabled(False)
            else:
                self.stackedWidget.setCurrentWidget(self.login_page)
                Password.clear(self)
                self.lineEdit_code.setEnabled(False)
                self.btn_continue.setEnabled(False)

        else:
            print("Passwords must match")
            ForgotPass_Messages.error_4(self)

    def random_code(self):
        x = random.randint(1000, 9999)
        return x


    def screen(self):
        if self.btn_login_signup.text() == "Logout":
            self.stackedWidget.setCurrentWidget(self.user_page)
            Password.clear(self)
            self.lineEdit_code.setEnabled(False)
            self.btn_continue.setEnabled(False)
        else:
            self.stackedWidget.setCurrentWidget(self.login_page)
            Password.clear(self)
            self.lineEdit_code.setEnabled(False)
            self.btn_continue.setEnabled(False)