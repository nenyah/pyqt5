# coding:utf-8

import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

win = QWidget()
win.resize(450, 150)
win.move(0, 300)
win.setWindowTitle('州的先生Zmister.com GUI教程')
win.show()

sys.exit(app.exec_())
