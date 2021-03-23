from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class quiz_Buttons(QMainWindow):

    TEST = { '10':10 , '20':20 , "blue":10 , "red":20 }

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

    def quiz_back_screen(self):
        # PAGES back
        self.btn_back_quiz.clicked.connect(lambda: self.stackedWidget_quiz.setCurrentWidget(self.signup_page))
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

    def Q_1(self):
        if self.Q1_A.isChecked():
            quiz_Buttons.score_1 = 10
        elif self.Q1_B.isChecked():
            quiz_Buttons.score_1 = 20
        elif self.Q1_C.isChecked():
            quiz_Buttons.score_1 = 30
        elif self.Q1_D.isChecked():
            quiz_Buttons.score_1 = 40
        elif self.Q1_E.isChecked():
            quiz_Buttons.score_1 = 50
        self.stackedWidget_quiz.setCurrentWidget(self.Q_2)
        print("1", quiz_Buttons.score_1)

    def Q_2(self):
        if self.Q2_A.isChecked():
            quiz_Buttons.score_2 = 10
        elif self.Q2_B.isChecked():
            quiz_Buttons.score_2 = 20
        elif self.Q2_C.isChecked():
            quiz_Buttons.score_2 = 30
        elif self.Q2_D.isChecked():
            quiz_Buttons.score_2 = 40
        elif self.Q2_E.isChecked():
            quiz_Buttons.score_2 = 50
        self.stackedWidget_quiz.setCurrentWidget(self.Q_3)
        print("2", quiz_Buttons.score_2)


    def Q_3(self):
        if self.Q3_A.isChecked():
            quiz_Buttons.score_3 = 10
        elif self.Q3_B.isChecked():
            quiz_Buttons.score_3 = 20
        elif self.Q3_C.isChecked():
            quiz_Buttons.score_3 = 30
        elif self.Q3_D.isChecked():
            quiz_Buttons.score_3 = 40
        elif self.Q3_E.isChecked():
            quiz_Buttons.score_3 = 50
        self.stackedWidget_quiz.setCurrentWidget(self.Q_4)
        print("3", quiz_Buttons.score_3)

    def Q_4(self):
        if self.Q4_A.isChecked():
            quiz_Buttons.score_4 = 10
        elif self.Q4_B.isChecked():
            quiz_Buttons.score_4 = 20
        elif self.Q4_C.isChecked():
            quiz_Buttons.score_4 = 30
        elif self.Q4_D.isChecked():
            quiz_Buttons.score_4 = 40
        elif self.Q4_E.isChecked():
            quiz_Buttons.score_4 = 50
        self.stackedWidget_quiz.setCurrentWidget(self.Q_5)
        print("4", quiz_Buttons.score_4)

    def Q_5(self):
        if self.Q5_A.isChecked():
            quiz_Buttons.score_5 = 10
        elif self.Q5_B.isChecked():
            quiz_Buttons.score_5 = 20
        elif self.Q5_C.isChecked():
            quiz_Buttons.score_5 = 30
        elif self.Q5_D.isChecked():
            quiz_Buttons.score_5 = 40
        elif self.Q5_E.isChecked():
            quiz_Buttons.score_5 = 50
        self.stackedWidget_quiz.setCurrentWidget(self.Q_6)
        print("5", quiz_Buttons.score_5)

    def Q_6(self):
        if self.Q6_A.isChecked():
            quiz_Buttons.score_6 = 10
        elif self.Q6_B.isChecked():
            quiz_Buttons.score_6 = 20
        elif self.Q6_C.isChecked():
            quiz_Buttons.score_6 = 30
        elif self.Q6_D.isChecked():
            quiz_Buttons.score_6 = 40
        elif self.Q6_E.isChecked():
            quiz_Buttons.score_6 = 50
        self.stackedWidget_quiz.setCurrentWidget(self.Q_7)
        print("6", quiz_Buttons.score_6)

    def Q_7(self):
        if self.Q7_A.isChecked():
            quiz_Buttons.score_7 = 10
        elif self.Q7_B.isChecked():
            quiz_Buttons.score_7 = 20
        elif self.Q7_C.isChecked():
            quiz_Buttons.score_7 = 30
        elif self.Q7_D.isChecked():
            quiz_Buttons.score_7 = 40
        elif self.Q7_E.isChecked():
            quiz_Buttons.score_7 = 50
        self.stackedWidget_quiz.setCurrentWidget(self.Q_8)
        print("7", quiz_Buttons.score_7)

    def Q_8(self):
        if self.Q8_A.isChecked():
            quiz_Buttons.score_8 = 10
        elif self.Q8_B.isChecked():
            quiz_Buttons.score_8 = 20
        elif self.Q8_C.isChecked():
            quiz_Buttons.score_8 = 30
        elif self.Q8_D.isChecked():
            quiz_Buttons.score_8 = 40
        elif self.Q8_E.isChecked():
            quiz_Buttons.score_8 = 50
        self.stackedWidget_quiz.setCurrentWidget(self.Q_9)
        print("8", quiz_Buttons.score_8)

    def Q_9(self):
        if self.Q9_A.isChecked():
            quiz_Buttons.score_9 = 10
        elif self.Q9_B.isChecked():
            quiz_Buttons.score_9 = 20
        elif self.Q9_C.isChecked():
            quiz_Buttons.score_9 = 30
        elif self.Q9_D.isChecked():
            quiz_Buttons.score_9 = 40
        elif self.Q9_E.isChecked():
            quiz_Buttons.score_9 = 50
        self.stackedWidget_quiz.setCurrentWidget(self.Q_10)
        print("9", quiz_Buttons.score_9)

    def Q_10(self):
        if self.Q10_A.isChecked():
            quiz_Buttons.score_10 = 10
        elif self.Q10_B.isChecked():
            quiz_Buttons.score_10 = 20
        elif self.Q10_C.isChecked():
            quiz_Buttons.score_10 = 30
        elif self.Q10_D.isChecked():
            quiz_Buttons.score_10 = 40
        elif self.Q10_E.isChecked():
            quiz_Buttons.score_10 = 50
        self.stackedWidget_quiz.setCurrentWidget(self.Q_11)
        print("10", quiz_Buttons.score_10)

    def Q_11(self):
        if self.Q11_A.isChecked():
            quiz_Buttons.score_11 = 10
        elif self.Q11_B.isChecked():
            quiz_Buttons.score_11 = 20
        elif self.Q11_C.isChecked():
            quiz_Buttons.score_11 = 30
        elif self.Q11_D.isChecked():
            quiz_Buttons.score_11 = 40
        elif self.Q11_E.isChecked():
            quiz_Buttons.score_11 = 50
        self.stackedWidget_quiz.setCurrentWidget(self.result)
        print("11", quiz_Buttons.score_11)

        quiz_Buttons.total = (quiz_Buttons.score_1 + quiz_Buttons.score_2 + quiz_Buttons.score_3 + quiz_Buttons.score_4 + quiz_Buttons.score_5 + quiz_Buttons.score_6 + quiz_Buttons.score_7 + quiz_Buttons.score_8 + quiz_Buttons.score_9 + quiz_Buttons.score_10 + quiz_Buttons.score_11)

        print("The total score is: ", quiz_Buttons.total)
        self.lcdNumber_13.display(quiz_Buttons.total)



#
    # def reset_Q_1(self):
    #     quiz_Buttons.score_1 = 0
    #     self.stackedWidget_quiz.setCurrentWidget(self.page_1)




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




#
# def Q_1(self):
#     quiz_Buttons.score_1 = 0
#     if self.Q1_A.isChecked():
#         quiz_Buttons.score_1 += 10
#         print(quiz_Buttons.score_1)
#         self.stackedWidget_quiz.setCurrentWidget(self.Q_2)
#     elif self.Q1_B.isChecked():
#         quiz_Buttons.score_1 += 20
#         print(quiz_Buttons.score_1)
#         self.stackedWidget_quiz.setCurrentWidget(self.Q_2)
#     elif self.Q1_C.isChecked():
#         quiz_Buttons.score_1 += 30
#         print(quiz_Buttons.score_1)
#         self.stackedWidget_quiz.setCurrentWidget(self.Q_2)
#     elif self.Q1_D.isChecked():
#         quiz_Buttons.score_1 += 40
#         print(quiz_Buttons.score_1)
#         self.stackedWidget_quiz.setCurrentWidget(self.Q_2)
#     elif self.Q1_E.isChecked():
#         quiz_Buttons.score_1 += 50
#         print(quiz_Buttons.score_1)
#         self.stackedWidget_quiz.setCurrentWidget(self.Q_2)
#
#
# def reset_Q_1(self):
#     quiz_Buttons.score_1 = 0
#     self.stackedWidget_quiz.setCurrentWidget(self.page_1)

#


# if text in ['10', '20', '30', '40']:
#     if radioBtn.isChecked()
#         quiz_Buttons.score_1 += quiz_Buttons.TEST[text]
#
# elif name == 'scores_2':
#     pass
#
# elif name == 'scores_3':
#     pass
#
# elif name == 'scores_4':
#     pass
# # 0 create a translator to translate records into values.
# # 1 add it to global record
# # 2 translate values from global record into values
#         radioBtn = self.sender()
#         text = radioBtn.text()
#         self.Q1_A.toggled.connect
#         # if radioBtn.isChecked():
#         #     self.label2.setText("You live in " + radioBtn.text())