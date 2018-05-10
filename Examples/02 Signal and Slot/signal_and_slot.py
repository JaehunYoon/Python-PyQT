# coding: utf-8

import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5 import QtCore


class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("02.ui", self)
        self.ui.show()

    @QtCore.pyqtSlot()
    def slot_1st(self):
        self.ui.label.setText("1")

    @QtCore.pyqtSlot()
    def slot_2nd(self):
        self.ui.label.setText("2")

    @QtCore.pyqtSlot()
    def slot_3rd(self):
        self.ui.label.setText("3")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())
