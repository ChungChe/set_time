#!/usr/bin/python
# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
class button(QPushButton):
    def __init__(self, parent = None):
        super(button, self).__init__(parent)
    def __init__(self, text, parent = None):
        super(button, self).__init__(text, parent)
        self.setFixedSize(60, 60)
        self.clicked.connect(self.clickHandler)
    def clickHandler(self):
        if self.text() == u"\u232B":
            print("Backspace")
        elif self.text() == u"\u23CE":
            print("Enter")
        else:
            print(self.text())

class numPad(QWidget):
    def __init__(self, parent=None):
        super(numPad, self).__init__(parent)
        self.createWidgets()
    def createWidgets(self):
       
        # create buttons
        grid = QGridLayout()
        grid.addWidget(button('7'), 1, 1)
        grid.addWidget(button('8'), 1, 2)
        grid.addWidget(button('9'), 1, 3)
        
        grid.addWidget(button('4'), 2, 1)
        grid.addWidget(button('5'), 2, 2)
        grid.addWidget(button('6'), 2, 3)
        
        grid.addWidget(button('1'), 3, 1)
        grid.addWidget(button('2'), 3, 2)
        grid.addWidget(button('3'), 3, 3)
        
        grid.addWidget(button('0'), 4, 1)
        grid.addWidget(button(u"\u232B"), 4, 2)
        grid.addWidget(button(u"\u23CE"), 4, 3)

        self.setWindowTitle(u"數字輸入盤")
        self.setLayout(grid)

