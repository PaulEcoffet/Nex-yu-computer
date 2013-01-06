# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login/login.ui'
#
# Created: Sun Jan  6 16:11:03 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        loginWindow.setObjectName(_fromUtf8("loginWindow"))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginWindow.sizePolicy().hasHeightForWidth())
        loginWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/login/NexYuLogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        loginWindow.setWindowIcon(icon)
        self.WindowLayout = QtGui.QVBoxLayout(loginWindow)
        self.WindowLayout.setObjectName(_fromUtf8("WindowLayout"))
        self.TitleLayout = QtGui.QHBoxLayout()
        self.TitleLayout.setObjectName(_fromUtf8("TitleLayout"))
        self.logoTitle = QtGui.QLabel(loginWindow)
        self.logoTitle.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logoTitle.sizePolicy().hasHeightForWidth())
        self.logoTitle.setSizePolicy(sizePolicy)
        self.logoTitle.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.logoTitle.setText(_fromUtf8(""))
        self.logoTitle.setPixmap(QtGui.QPixmap(_fromUtf8(":/login/NexYuLogoFull.png")))
        self.logoTitle.setScaledContents(False)
        self.logoTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.logoTitle.setWordWrap(False)
        self.logoTitle.setObjectName(_fromUtf8("logoTitle"))
        self.TitleLayout.addWidget(self.logoTitle)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.TitleLayout.addItem(spacerItem)
        self.WindowLayout.addLayout(self.TitleLayout)
        self.bodyLayout = QtGui.QVBoxLayout()
        self.bodyLayout.setObjectName(_fromUtf8("bodyLayout"))
        self.howToScan = QtGui.QLabel(loginWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.howToScan.sizePolicy().hasHeightForWidth())
        self.howToScan.setSizePolicy(sizePolicy)
        self.howToScan.setScaledContents(False)
        self.howToScan.setWordWrap(True)
        self.howToScan.setObjectName(_fromUtf8("howToScan"))
        self.bodyLayout.addWidget(self.howToScan)
        self.qrCodeLayout = QtGui.QHBoxLayout()
        self.qrCodeLayout.setObjectName(_fromUtf8("qrCodeLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.qrCodeLayout.addItem(spacerItem1)
        self.qrCodeContainer = QtGui.QLabel(loginWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qrCodeContainer.sizePolicy().hasHeightForWidth())
        self.qrCodeContainer.setSizePolicy(sizePolicy)
        self.qrCodeContainer.setMinimumSize(QtCore.QSize(200, 200))
        self.qrCodeContainer.setText(_fromUtf8(""))
        self.qrCodeContainer.setObjectName(_fromUtf8("qrCodeContainer"))
        self.qrCodeLayout.addWidget(self.qrCodeContainer)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.qrCodeLayout.addItem(spacerItem2)
        self.bodyLayout.addLayout(self.qrCodeLayout)
        self.WindowLayout.addLayout(self.bodyLayout)
        self.WindowLayout.setStretch(1, 1)

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslateUi(self, loginWindow):
        loginWindow.setWindowTitle(_translate("loginWindow", "Nex yu - Login", None))
        self.howToScan.setText(_translate("loginWindow", "<html><head/><body><p>Scan this code with the Nex yu application on your Android so as to pair your devices, the connection will be done automatically.</p></body></html>", None))

import login_rc
