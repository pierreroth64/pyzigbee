#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QMainWindow, QApplication
from PyQt5.QtCore import QCoreApplication

from pyzigbee import __version__ as libversion

class PyZigBeeApp(QMainWindow):

    def __init__(self):
        super(PyZigBeeApp, self).__init__()
        self.initUI()

    def initUI(self):

        scan_btn = QPushButton('Scan', self)
        scan_btn.clicked.connect(QCoreApplication.instance().quit)
        scan_btn.resize(scan_btn.sizeHint())
        scan_btn.move(50, 50)

        self.setGeometry(200, 300, 500, 150)
        self.setWindowTitle('PyZigBee GUI - based on pyzigbee %s' % libversion)
        self.show()

        self.statusBar().showMessage('Ready')

if __name__ == '__main__':

    app = QApplication(sys.argv)
    zigbeeapp = PyZigBeeApp()
    sys.exit(app.exec_())
