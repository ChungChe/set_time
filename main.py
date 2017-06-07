#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from datetime import datetime

class setTimeWidget(QWidget):
    def __init__(self, parent=None):
        super(setTimeWidget, self).__init__(parent)
        self.setGeometry(100,100,500,200)
        self.createWidgets()
        self.setWindowTitle(u"設定時間")
    def createWidgets(self):
        dt = datetime.now()

        hbox_bottom = QHBoxLayout()
        ok_button = QPushButton(u"確定")
        ok_button.setFixedHeight(60)
        cancel_button = QPushButton(u"取消")
        cancel_button.setFixedHeight(60)
        hbox_bottom.addWidget(ok_button)
        hbox_bottom.addWidget(cancel_button)

        year_label = QLabel(self)
        year_label.setText(u"年:")
        year_input = QSpinBox(self)
        year_input.setFixedSize(100, 60)
        year_input.setRange(1900, 3000)
        year_input.setValue(dt.year)

        month_label = QLabel(self)
        month_label.setText(u"月:")
        month_input = QSpinBox(self)
        month_input.setFixedSize(100, 60)
        month_input.setRange(1, 12)
        month_input.setValue(dt.month)

        day_label = QLabel(self)
        day_label.setText(u"日:")
        day_input = QSpinBox(self)
        day_input.setFixedSize(100, 60) 
        day_input.setRange(1, 31)
        day_input.setValue(dt.day)

        hbox_top = QHBoxLayout()
        
        hbox_top.addWidget(year_label)
        hbox_top.addWidget(year_input)
        hbox_top.addWidget(month_label)
        hbox_top.addWidget(month_input)
        hbox_top.addWidget(day_label)
        hbox_top.addWidget(day_input)
        
        hr_label = QLabel(self)
        hr_label.setText(u"時:")
        hr_input = QSpinBox(self)
        hr_input.setFixedSize(100, 60)
        hr_input.setRange(1, 23)
        hr_input.setValue(dt.hour)

        min_label = QLabel(self)
        min_label.setText(u"分:")
        min_input = QSpinBox(self)
        min_input.setFixedSize(100, 60)
        min_input.setRange(1, 59)
        min_input.setValue(dt.minute)

        sec_label = QLabel(self)
        sec_label.setText(u"秒:")
        sec_input = QSpinBox(self)
        sec_input.setFixedSize(100, 60)
        sec_input.setRange(1, 59)
        sec_input.setValue(dt.second)

        hbox_mid = QHBoxLayout()
        hbox_mid.addWidget(hr_label)
        hbox_mid.addWidget(hr_input)
        hbox_mid.addWidget(min_label)
        hbox_mid.addWidget(min_input)
        hbox_mid.addWidget(sec_label)
        hbox_mid.addWidget(sec_input)
        
        vbox = QVBoxLayout()
        vbox.addLayout(hbox_top);
        vbox.addLayout(hbox_mid);
        vbox.addLayout(hbox_bottom);
        self.setLayout(vbox)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    widget = setTimeWidget()
    widget.setGeometry(100,100,500,200)
    widget.show()
    sys.exit(app.exec_())
