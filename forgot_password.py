from PyQt5.QtWidgets import *
import re
import random
import smtplib

#files
import actions

def send_email(code,user_email):
    # Email sender
    print("sending")

    password = "Veerbest23"
    sender = "bobdoe945@gmail.com"
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
    print(f"The code is: {code}")


class Password(QMainWindow):

    valid_code = None
    email = None

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def handleSend(self):
        Password.email = self.lineEdit_email_send.text()

        if not re.search("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", Password.email):
            print('Invalid input(s)')

        elif not actions.DATABASE(f"select * from users where email  == '{Password.email}'"):
             print('Not in Database')

        else:
            # Email sender
            Password.valid_code = self.random_code()
            send_email(Password.valid_code, Password.email)
            self.lineEdit_code.setEnabled(True)
            self.btn_continue.setEnabled(True)


    def code(self):
        code = self.lineEdit_code.text()
        sent_code = Password.valid_code
        print(f"The code is: {sent_code}")


    def random_code(self):
        x = random.randint(1000, 9999)
        return x



