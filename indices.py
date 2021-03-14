from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer

import requests
from bs4 import BeautifulSoup


class RealTimeLabel(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

