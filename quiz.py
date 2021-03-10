from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class quiz_Buttons(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    score_1 = 0
    score_2 = 0
    score_3 = 0
    score_4 = 0
    score_5 = 0
    score_6 = 0
    score_7 = 0
    score_8 = 0
    score_9 = 0
    score_10 = 0
    score_11 = 0

    def quiz_next_screen(self):
        # PAGES next
        self.btn_Q_1.clicked.connect(lambda: self.stackedWidget_quiz.setCurrentWidget(self.Q_1))
        self.btn_Q_2.clicked.connect(lambda: quiz_Buttons.Q_1(self))
        self.btn_Q_3.clicked.connect(lambda: self.stackedWidget_quiz.setCurrentWidget(self.Q_3))
        self.btn_Q_4.clicked.connect(lambda: self.stackedWidget_quiz.setCurrentWidget(self.Q_4))
        self.btn_Q_5.clicked.connect(lambda: self.stackedWidget_quiz.setCurrentWidget(self.Q_5))
        self.btn_Q_6.clicked.connect(lambda: self.stackedWidget_quiz.setCurrentWidget(self.Q_6))
        self.btn_Q_7.clicked.connect(lambda: self.stackedWidget_quiz.setCurrentWidget(self.Q_7))
        self.btn_Q_8.clicked.connect(lambda: self.stackedWidget_quiz.setCurrentWidget(self.Q_8))
        self.btn_Q_9.clicked.connect(lambda: self.stackedWidget_quiz.setCurrentWidget(self.Q_9))
        self.btn_Q_10.clicked.connect(lambda: self.stackedWidget_quiz.setCurrentWidget(self.Q_10))
        self.btn_Q_11.clicked.connect(lambda: self.stackedWidget_quiz.setCurrentWidget(self.Q_11))
        self.btn_result.clicked.connect(lambda: self.stackedWidget_quiz.setCurrentWidget(self.result))

    def quiz_back_screen(self):
        # PAGES back
        self.btn_back_quiz.clicked.connect(lambda: self.stackedWidget_quiz.setCurrentWidget(self.signup_page))
        self.btn_back_Q1.clicked.connect(lambda: quiz_Buttons.reset_Q_1(self))
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
        quiz_Buttons.score_1 = 0
        if self.Q1_A.isChecked():
            quiz_Buttons.score_1 += 10
            print(quiz_Buttons.score_1)
            self.stackedWidget_quiz.setCurrentWidget(self.Q_2)
        elif self.Q1_B.isChecked():
            quiz_Buttons.score_1 += 20
            print(quiz_Buttons.score_1)
            self.stackedWidget_quiz.setCurrentWidget(self.Q_2)
        elif self.Q1_C.isChecked():
            quiz_Buttons.score_1 += 30
            print(quiz_Buttons.score_1)
            self.stackedWidget_quiz.setCurrentWidget(self.Q_2)
        elif self.Q1_D.isChecked():
            quiz_Buttons.score_1 += 40
            print(quiz_Buttons.score_1)
            self.stackedWidget_quiz.setCurrentWidget(self.Q_2)
        elif self.Q1_E.isChecked():
            quiz_Buttons.score_1 += 50
            print(quiz_Buttons.score_1)
            self.stackedWidget_quiz.setCurrentWidget(self.Q_2)

    def reset_Q_1(self):
        quiz_Buttons.score_1 = 0
        self.stackedWidget_quiz.setCurrentWidget(self.page_1)


    # score_list = [score_1, score_2, score_3, score_4, score_5, score_6, score_7, score_8, score]
    # for question in range(10):
    #    quiz_Buttons.score = 0
    #    if

