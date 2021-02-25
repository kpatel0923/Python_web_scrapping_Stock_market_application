import sys
import subprocess
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


test  = 0
#Used for installing any missing packages
class Install():
    def main(self):
        #Get the list on current package on system
        reqs = subprocess.check_output([sys.executable, '-m', 'pip','freeze'])
        installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

        #Another way to install packages but the one on the bottom is faster
        #subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirments.txt"])

        #Get the packages required for the project using the provided TXT file created by us
        required = []
        with open("requirement.txt","r") as file:
            for package in file:
                required.append(package.split("==")[0])

        #Looping over the packages to see which ones are missing and install them
        for package in required:
            if package not in installed_packages:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])




class common_Buttons(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

    def home_screen(self):
        # PAGE home
        self.btn_home.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.home_page))

    def login_screen(self):
        # PAGE login
        self.btn_login_signup.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.login_page))

    def signup_screen(self):
        # PAGE signup
        self.btn_signup.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.signup_page))