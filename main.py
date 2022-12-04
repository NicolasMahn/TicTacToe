from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import *
import sys
import window


def main():
    app = QApplication([])

    win = window.TicTacToe()

    win.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()