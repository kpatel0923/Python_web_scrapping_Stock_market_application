from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import actions
from signup import *
from error_messages import *


class quiz_Buttons(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)


    def quiz_next_screen(self):
        # PAGES next
        quiz_Buttons.score_1 = 0
        quiz_Buttons.score_2 = 0
        quiz_Buttons.score_3 = 0
        quiz_Buttons.score_4 = 0
        quiz_Buttons.score_5 = 0
        quiz_Buttons.score_6 = 0
        quiz_Buttons.score_7 = 0
        quiz_Buttons.score_8 = 0
        quiz_Buttons.score_9 = 0
        quiz_Buttons.score_10 = 0
        quiz_Buttons.score_11 = 0

        quiz_Buttons.total = 0

        quiz_Buttons.score_list = [quiz_Buttons.score_1, quiz_Buttons.score_2, quiz_Buttons.score_3, quiz_Buttons.score_4, quiz_Buttons.score_5, quiz_Buttons.score_6, quiz_Buttons.score_7, quiz_Buttons.score_8, quiz_Buttons.score_9, quiz_Buttons.score_10, quiz_Buttons.score_11]
        self.btn_Q_1.clicked.connect(lambda: self.stackedWidget_quiz.setCurrentWidget(self.Q_1))
        self.btn_Q_2.clicked.connect(lambda: quiz_Buttons.Q_1(self))
        self.btn_Q_3.clicked.connect(lambda: quiz_Buttons.Q_2(self))
        self.btn_Q_4.clicked.connect(lambda: quiz_Buttons.Q_3(self))
        self.btn_Q_5.clicked.connect(lambda: quiz_Buttons.Q_4(self))
        self.btn_Q_6.clicked.connect(lambda: quiz_Buttons.Q_5(self))
        self.btn_Q_7.clicked.connect(lambda: quiz_Buttons.Q_6(self))
        self.btn_Q_8.clicked.connect(lambda: quiz_Buttons.Q_7(self))
        self.btn_Q_9.clicked.connect(lambda: quiz_Buttons.Q_8(self))
        self.btn_Q_10.clicked.connect(lambda: quiz_Buttons.Q_9(self))
        self.btn_Q_11.clicked.connect(lambda: quiz_Buttons.Q_10(self))
        self.btn_result.clicked.connect(lambda: quiz_Buttons.Q_11(self))
        self.btn_userprofile.clicked.connect(lambda: quiz_Buttons.score(self))


    def quiz_back_screen(self):
        # PAGES back
        self.btn_back_quiz.clicked.connect(lambda: quiz_Buttons.screen(self))
        self.btn_back_Q1.clicked.connect(lambda: self.stackedWidget_quiz.setCurrentWidget(self.page_1))
        self.btn_back_Q2.clicked.connect(lambda: self.stackedWidget_quiz.setCurrentWidget(self.Q_1))
        self.btn_back_Q3.clicked.connect(lambda: self.stackedWidget_quiz.setCurrentWidget(self.Q_2))
        self.btn_back_Q4.clicked.connect(lambda: self.stackedWidget_quiz.setCurrentWidget(self.Q_3))
        self.btn_back_Q5.clicked.connect(lambda: self.stackedWidget_quiz.setCurrentWidget(self.Q_4))
        self.btn_back_Q6.clicked.connect(lambda: self.stackedWidget_quiz.setCurrentWidget(self.Q_5))
        self.btn_back_Q7.clicked.connect(lambda: self.stackedWidget_quiz.setCurrentWidget(self.Q_6))
        self.btn_back_Q8.clicked.connect(lambda: self.stackedWidget_quiz.setCurrentWidget(self.Q_7))
        self.btn_back_Q9.clicked.connect(lambda: self.stackedWidget_quiz.setCurrentWidget(self.Q_8))
        self.btn_back_Q10.clicked.connect(lambda: self.stackedWidget_quiz.setCurrentWidget(self.Q_9))
        self.btn_back_Q11.clicked.connect(lambda: self.stackedWidget_quiz.setCurrentWidget(self.Q_10))


    def score(self):
        if self.btn_login_signup.text() == "Logout":
            user_email = self.lineEdit_useremail.text()
            actions.DATABASE(f"update users set score = '{quiz_Buttons.total}' where email = '{user_email}' ")
            actions.DATABASE(f"update users set q6 = '{quiz_Buttons.score_6}' where email = '{user_email}' ")
            print(quiz_Buttons.total)
            self.lineEdit_scoreholder.setText(str(quiz_Buttons.total))
            self.stackedWidget_quiz.setCurrentWidget(self.page_1)
            self.stackedWidget.setCurrentWidget(self.user_page)
        else:
            user_email = self.lineEdit_email_2.text()
            print(user_email)
            actions.DATABASE(f"update users set score = '{quiz_Buttons.total}' where email = '{user_email}' ")
            actions.DATABASE(f"update users set q6 = '{quiz_Buttons.score_6}' where email = '{user_email}' ")
            print(quiz_Buttons.total)
            Signup.clear(self)
            Signup_Messages.error_4(self)
            self.stackedWidget_quiz.setCurrentWidget(self.page_1)
            self.stackedWidget.setCurrentWidget(self.login_page)


    def screen(self):
        if self.btn_login_signup.text() == "Logout":
            self.stackedWidget.setCurrentWidget(self.user_page)
        else:
            self.stackedWidget.setCurrentWidget(self.signup_page)


    def Q_1(self):
        if self.Q1_A.isChecked():
            quiz_Buttons.score_1 = 5
        elif self.Q1_B.isChecked():
            quiz_Buttons.score_1 = 4
        elif self.Q1_C.isChecked():
            quiz_Buttons.score_1 = 3
        elif self.Q1_D.isChecked():
            quiz_Buttons.score_1 = 2
        elif self.Q1_E.isChecked():
            quiz_Buttons.score_1 = 1
        else:
            quiz_Buttons.score_1 = 1
        self.stackedWidget_quiz.setCurrentWidget(self.Q_2)
        print("1", quiz_Buttons.score_1)

    def Q_2(self):
        if self.Q2_A.isChecked():
            quiz_Buttons.score_2 = 1
        elif self.Q2_B.isChecked():
            quiz_Buttons.score_2 = 2
        elif self.Q2_C.isChecked():
            quiz_Buttons.score_2 = 3
        elif self.Q2_D.isChecked():
            quiz_Buttons.score_2 = 4
        elif self.Q2_E.isChecked():
            quiz_Buttons.score_2 = 5
        else:
            quiz_Buttons.score_2 = 1
        self.stackedWidget_quiz.setCurrentWidget(self.Q_3)
        print("2", quiz_Buttons.score_2)

    def Q_3(self):
        if self.Q3_A.isChecked():
            quiz_Buttons.score_3 = 4
        elif self.Q3_B.isChecked():
            quiz_Buttons.score_3 = 3
        elif self.Q3_C.isChecked():
            quiz_Buttons.score_3 = 2
        elif self.Q3_D.isChecked():
            quiz_Buttons.score_3 = 1
        else:
            quiz_Buttons.score_3 = 1
        self.stackedWidget_quiz.setCurrentWidget(self.Q_4)
        print("3", quiz_Buttons.score_3)

    def Q_4(self):
        if self.Q4_A.isChecked():
            quiz_Buttons.score_4 = 3
        elif self.Q4_B.isChecked():
            quiz_Buttons.score_4 = 2
        elif self.Q4_C.isChecked():
            quiz_Buttons.score_4 = 1
        else:
            quiz_Buttons.score_4 = 1
        self.stackedWidget_quiz.setCurrentWidget(self.Q_5)
        print("4", quiz_Buttons.score_4)

    def Q_5(self):
        if self.Q5_A.isChecked():
            quiz_Buttons.score_5 = 3
        elif self.Q5_B.isChecked():
            quiz_Buttons.score_5 = 2
        elif self.Q5_C.isChecked():
            quiz_Buttons.score_5 = 1
        else:
            quiz_Buttons.score_5 = 1
        self.stackedWidget_quiz.setCurrentWidget(self.Q_6)
        print("5", quiz_Buttons.score_5)

    def Q_6(self):
        if self.Q6_A.isChecked():
            quiz_Buttons.score_6 = 1
        elif self.Q6_B.isChecked():
            quiz_Buttons.score_6 = 2
        elif self.Q6_C.isChecked():
            quiz_Buttons.score_6 = 3
        elif self.Q6_D.isChecked():
            quiz_Buttons.score_6 = 4
        else:
            quiz_Buttons.score_6 = 1
        self.stackedWidget_quiz.setCurrentWidget(self.Q_7)
        print("6", quiz_Buttons.score_6)

    def Q_7(self):
        if self.Q7_A.isChecked():
            quiz_Buttons.score_7 = 5
        elif self.Q7_B.isChecked():
            quiz_Buttons.score_7 = 4
        elif self.Q7_C.isChecked():
            quiz_Buttons.score_7 = 3
        elif self.Q7_D.isChecked():
            quiz_Buttons.score_7 = 2
        elif self.Q7_E.isChecked():
            quiz_Buttons.score_7 = 1
        else:
            quiz_Buttons.score_7 = 1
        self.stackedWidget_quiz.setCurrentWidget(self.Q_8)
        print("7", quiz_Buttons.score_7)

    def Q_8(self):
        if self.Q8_A.isChecked():
            quiz_Buttons.score_8 = 5
        elif self.Q8_B.isChecked():
            quiz_Buttons.score_8 = 4
        elif self.Q8_C.isChecked():
            quiz_Buttons.score_8 = 3
        elif self.Q8_D.isChecked():
            quiz_Buttons.score_8 = 2
        elif self.Q8_E.isChecked():
            quiz_Buttons.score_8 = 1
        else:
            quiz_Buttons.score_8 = 1
        self.stackedWidget_quiz.setCurrentWidget(self.Q_9)
        print("8", quiz_Buttons.score_8)

    def Q_9(self):
        if self.Q9_A.isChecked():
            quiz_Buttons.score_9 = 5
        elif self.Q9_B.isChecked():
            quiz_Buttons.score_9 = 4
        elif self.Q9_C.isChecked():
            quiz_Buttons.score_9 = 3
        elif self.Q9_D.isChecked():
            quiz_Buttons.score_9 = 2
        elif self.Q9_E.isChecked():
            quiz_Buttons.score_9 = 1
        else:
            quiz_Buttons.score_9 = 1
        self.stackedWidget_quiz.setCurrentWidget(self.Q_10)
        print("9", quiz_Buttons.score_9)

    def Q_10(self):
        if self.Q10_A.isChecked():
            quiz_Buttons.score_10 = 4
        elif self.Q10_B.isChecked():
            quiz_Buttons.score_10 = 3
        elif self.Q10_C.isChecked():
            quiz_Buttons.score_10 = 2
        elif self.Q10_D.isChecked():
            quiz_Buttons.score_10 = 1
        else:
            quiz_Buttons.score_10 = 1
        self.stackedWidget_quiz.setCurrentWidget(self.Q_11)
        print("10", quiz_Buttons.score_10)

    def Q_11(self):
        if self.Q11_A.isChecked():
            quiz_Buttons.score_11 = 4
        elif self.Q11_B.isChecked():
            quiz_Buttons.score_11 = 3
        elif self.Q11_C.isChecked():
            quiz_Buttons.score_11 = 2
        elif self.Q11_D.isChecked():
            quiz_Buttons.score_11 = 1
        else:
            quiz_Buttons.score_11 = 1
        self.stackedWidget_quiz.setCurrentWidget(self.result)
        print("11", quiz_Buttons.score_11)

        quiz_Buttons.total = (quiz_Buttons.score_1 + quiz_Buttons.score_2 + quiz_Buttons.score_3 + quiz_Buttons.score_4 + quiz_Buttons.score_5 + quiz_Buttons.score_6 + quiz_Buttons.score_7 + quiz_Buttons.score_8 + quiz_Buttons.score_9 + quiz_Buttons.score_10 + quiz_Buttons.score_11)

        print("The total score is: ", quiz_Buttons.total)
        self.lcdNumber_13.display(quiz_Buttons.total)

    def process(self):
        score_list = [quiz_Buttons.score_1, quiz_Buttons.score_2, quiz_Buttons.score_3, quiz_Buttons.score_4, quiz_Buttons.score_5, quiz_Buttons.score_6, quiz_Buttons.score_7, quiz_Buttons.score_8, quiz_Buttons.score_9, quiz_Buttons.score_10, quiz_Buttons.score_11]
        print(score_list)
        for item in range(1, 12):
            # print(score_list[item], 'list ')
            # var = 'score_' + str(item)
            temp_var_A = 'Q' + str(item) + '_A'
            temp_var_B = 'Q' + str(item) + '_B'
            temp_var_C = 'Q' + str(item) + '_C'
            temp_var_D = 'Q' + str(item) + '_D'
            temp_var_E = 'Q' + str(item) + '_E'

            temp_page = 'Q_' + str(item)


            new_list = [temp_var_A, temp_var_B, temp_var_C, temp_var_D, temp_var_E]


            if item == 1:
                quiz_Buttons.score_1 = quiz_Buttons.Q_1(self, temp_var_A, temp_var_B, temp_var_C, temp_var_D, temp_var_E, temp_page)
                print(quiz_Buttons.score_1)
                print(score_list)
            elif item == 2:
                print(temp_page)

            # print(temp_var.isChecked())







        # print(score_list)