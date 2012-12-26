# -*- coding: utf-8 -*-

from PyQt4 import QtGui
import ui.MainWindow.mainWindow as mw
import pyqrcode

class MainWindow(QtGui.QWidget, mw.Ui_nexyuMain):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.setupUi(self)

