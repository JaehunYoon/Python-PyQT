# coding: utf-8

import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5 import QtCore

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("scheduler.ui", self)
        self.text = QtWidgets.QTextBrowser()
        self.ui.show()

    @QtCore.pyqtSlot()
    def slot(self):
        self.text.setText("1")