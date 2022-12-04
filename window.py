from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import *
import sys


class TicTacToe(QMainWindow):
    def __init__(self):
        super(TicTacToe, self).__init__()
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle("TicTacToe")
        self.initUI()

    def initUI(self):
        self.l_test = QLabel(self)
        self.l_test.setText("Test")
        self.l_test.move(400, 400)

        self.b_test = QPushButton(self)
        self.b_test.setText("test")
        self.b_test.clicked.connect(self.clicked)

    def clicked(self):
        self.l_test.setText("Clicked___________________")
        self.update()

    def update(self):
        self.l_test.adjustSize()
