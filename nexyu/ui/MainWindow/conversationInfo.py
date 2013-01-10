# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow/conversationInfo.ui'
#
# Created: Thu Jan 10 21:38:19 2013
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

class Ui_conversationInfo(object):
    def setupUi(self, conversationInfo):
        conversationInfo.setObjectName(_fromUtf8("conversationInfo"))
        conversationInfo.resize(439, 46)
        conversationInfo.setMaximumSize(QtCore.QSize(16777215, 46))
        self.verticalLayout = QtGui.QVBoxLayout(conversationInfo)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.icon = QtGui.QLabel(conversationInfo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon.sizePolicy().hasHeightForWidth())
        self.icon.setSizePolicy(sizePolicy)
        self.icon.setMinimumSize(QtCore.QSize(26, 26))
        self.icon.setMaximumSize(QtCore.QSize(26, 26))
        self.icon.setStyleSheet(_fromUtf8("#icon\n"
"{\n"
"    border: 1px solid #7d7b7b;\n"
"    border-radius: 2px;\n"
"    background-color: white;\n"
"}"))
        self.icon.setObjectName(_fromUtf8("icon"))
        self.horizontalLayout.addWidget(self.icon)
        self.name = QtGui.QLabel(conversationInfo)
        self.name.setStyleSheet(_fromUtf8("#name\n"
"{\n"
"    font-size: 18px;\n"
"    font-family: Roboto;\n"
"}"))
        self.name.setTextFormat(QtCore.Qt.PlainText)
        self.name.setObjectName(_fromUtf8("name"))
        self.horizontalLayout.addWidget(self.name)
        self.phoneNumber = QtGui.QLabel(conversationInfo)
        self.phoneNumber.setStyleSheet(_fromUtf8("#phoneNumber\n"
"{\n"
"    color: #4d4d4d;\n"
"    font-size: 11px;\n"
"    font-family: Roboto;\n"
"}"))
        self.phoneNumber.setTextFormat(QtCore.Qt.PlainText)
        self.phoneNumber.setObjectName(_fromUtf8("phoneNumber"))
        self.horizontalLayout.addWidget(self.phoneNumber)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(conversationInfo)
        QtCore.QMetaObject.connectSlotsByName(conversationInfo)

    def retranslateUi(self, conversationInfo):
        conversationInfo.setWindowTitle(_translate("conversationInfo", "Form", None))
        self.name.setText(_translate("conversationInfo", "First Last", None))
        self.phoneNumber.setText(_translate("conversationInfo", "(+3368989781)", None))

import mainWindow_rc
