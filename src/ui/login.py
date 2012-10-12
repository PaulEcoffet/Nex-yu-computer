# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Fri Oct 12 21:13:47 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_loginWindow(object):
    def setupUi(self, loginWindow):
        loginWindow.setObjectName(_fromUtf8("loginWindow"))
        loginWindow.setEnabled(True)
        loginWindow.resize(440, 433)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginWindow.sizePolicy().hasHeightForWidth())
        loginWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/login/NexYuLogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        loginWindow.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(loginWindow)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.TitleLayout = QtGui.QHBoxLayout()
        self.TitleLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
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
        self.verticalLayout.addLayout(self.TitleLayout)
        self.bodyLayout = QtGui.QVBoxLayout()
        self.bodyLayout.setObjectName(_fromUtf8("bodyLayout"))
        self.howToScan = QtGui.QLabel(loginWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.howToScan.sizePolicy().hasHeightForWidth())
        self.howToScan.setSizePolicy(sizePolicy)
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
        self.verticalLayout.addLayout(self.bodyLayout)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(loginWindow)
        QtCore.QMetaObject.connectSlotsByName(loginWindow)

    def retranslateUi(self, loginWindow):
        loginWindow.setWindowTitle(QtGui.QApplication.translate("loginWindow", "Nex yu - Login", None, QtGui.QApplication.UnicodeUTF8))
        self.howToScan.setText(QtGui.QApplication.translate("loginWindow", "<html><head/><body><p>Scan this code with the Nex yu application on your Android so as to pair your devices, the connection will be done automatically.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

import login_rc
