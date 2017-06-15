#!/usr/bin/python
# -*- coding: utf-8 -*-

# a 100x60 spinbox
# when the spinbox clicked, a numpad shown
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from numpad import *


class spinBox(QSpinBox):
    def __init__(self, parent = None):
        super(spinBox, self).__init__(parent)
        #self.textedited.connect(self.clickHandler)
        self.setFixedSize(100, 60)
        #self.mouseReleaseEvent = self.clickHandler
    def clickHandler(self, event):
        n = numPad()
        n.show()

