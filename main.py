#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from datetime import datetime
from numpad import *
from spinbox import *
import os

class setTimeWidget(QWidget):
    def __init__(self, parent=None):
        super(setTimeWidget, self).__init__(parent)
        
        self.year_input = None
        self.month_input = None
        self.day_input = None
        self.hr_input = None
        self.min_input = None
        self.sec_input = None
        
        self.setGeometry(0,0,500,200)
        self.createWidgets()
        self.setWindowTitle(u"設定時間")
        cp = QDesktopWidget().availableGeometry().center()
        self.move(cp.x() - self.width() / 2, cp.y() - self.height() / 2)

    def okHandler(self):
        print("OK")
        time_str = '{}/{}/{} {}:{}:{}'.format(self.year_input.value(),
                    self.month_input.value(),
                    self.day_input.value(),
                    self.hr_input.value(),
                    self.min_input.value(),
                    self.sec_input.value())
        command = "sudo date +'%Y/%m/%d %H:%M:%S' -s '{}'".format(time_str)
        print(command)
        os.system(command)
        
    def cancelHandler(self):
        print("Cancel")
        QCoreApplication.instance().quit()
    def createWidgets(self):
        dt = datetime.now()

        hbox_bottom = QHBoxLayout()
        ok_button = QPushButton(u"確定")
        ok_button.setFixedHeight(60)
        ok_button.clicked.connect(self.okHandler)
        cancel_button = QPushButton(u"取消")
        cancel_button.setFixedHeight(60)
        cancel_button.clicked.connect(self.cancelHandler)
        hbox_bottom.addWidget(ok_button)
        hbox_bottom.addWidget(cancel_button)

        year_label = QLabel(self)
        year_label.setText(u"年:")
        self.year_input = spinBox(self)
        self.year_input.setRange(1900, 3000)
        self.year_input.setValue(dt.year)

        month_label = QLabel(self)
        month_label.setText(u"月:")
        self.month_input = spinBox(self)
        self.month_input.setRange(1, 12)
        self.month_input.setValue(dt.month)

        day_label = QLabel(self)
        day_label.setText(u"日:")
        self.day_input = spinBox(self)
        self.day_input.setRange(1, 31)
        self.day_input.setValue(dt.day)

        hbox_top = QHBoxLayout()
        
        hbox_top.addWidget(year_label)
        hbox_top.addWidget(self.year_input)
        hbox_top.addWidget(month_label)
        hbox_top.addWidget(self.month_input)
        hbox_top.addWidget(day_label)
        hbox_top.addWidget(self.day_input)
        
        hr_label = QLabel(self)
        hr_label.setText(u"時:")
        self.hr_input = spinBox(self)
        self.hr_input.setRange(1, 23)
        self.hr_input.setValue(dt.hour)

        min_label = QLabel(self)
        min_label.setText(u"分:")
        self.min_input = spinBox(self)
        self.min_input.setRange(1, 59)
        self.min_input.setValue(dt.minute)

        sec_label = QLabel(self)
        sec_label.setText(u"秒:")
        self.sec_input = spinBox(self)
        self.sec_input.setRange(1, 59)
        self.sec_input.setValue(dt.second)

        hbox_mid = QHBoxLayout()
        hbox_mid.addWidget(hr_label)
        hbox_mid.addWidget(self.hr_input)
        hbox_mid.addWidget(min_label)
        hbox_mid.addWidget(self.min_input)
        hbox_mid.addWidget(sec_label)
        hbox_mid.addWidget(self.sec_input)
        
        vbox = QVBoxLayout()
        vbox.addLayout(hbox_top);
        vbox.addLayout(hbox_mid);
        vbox.addLayout(hbox_bottom);
        self.setLayout(vbox)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    widget = setTimeWidget()
    #widget.setGeometry(100,100,500,200)
    widget.show()
    
    
    sys.exit(app.exec_())

