# -*- coding: utf-8 -*-

from PyQt4 import QtGui
import ui.login
import pyqrcode
from PIL import ImageQt


class LoginWindow(QtGui.QWidget, ui.login.Ui_loginWindow):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)

    def setQrCode(self, uri):
        qrcode = ImageQt.ImageQt(pyqrcode.MakeQRImage(uri, block_in_pixels=5,
                            border_in_blocks=0))
        pixmap = QtGui.QPixmap.fromImage(qrcode)
        self.qrCodeContainer.setPixmap(pixmap)
