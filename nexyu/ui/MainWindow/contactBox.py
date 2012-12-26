# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow/contactBox.ui'
#
# Created: Wed Dec 26 18:13:53 2012
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

class Ui_contactBox(object):
    def setupUi(self, contactBox):
        contactBox.setObjectName(_fromUtf8("contactBox"))
        contactBox.resize(269, 80)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(contactBox.sizePolicy().hasHeightForWidth())
        contactBox.setSizePolicy(sizePolicy)
        contactBox.setMinimumSize(QtCore.QSize(0, 80))
        contactBox.setMaximumSize(QtCore.QSize(16777215, 80))
        contactBox.setStyleSheet(_fromUtf8("#contactBox\n"
"{\n"
"    background-color: white;\n"
"    border-bottom: 1px solid #323232;\n"
"}"))
        self.verticalLayout = QtGui.QVBoxLayout(contactBox)
        self.verticalLayout.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.icon = QtGui.QLabel(contactBox)
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
        self.name = QtGui.QLabel(contactBox)
        self.name.setStyleSheet(_fromUtf8("#name\n"
"{\n"
"    font-size: 14px;\n"
"    font-family: Roboto;\n"
"}"))
        self.name.setTextFormat(QtCore.Qt.PlainText)
        self.name.setObjectName(_fromUtf8("name"))
        self.horizontalLayout.addWidget(self.name)
        self.phoneNumber = QtGui.QLabel(contactBox)
        self.phoneNumber.setStyleSheet(_fromUtf8("#phoneNumber\n"
"{\n"
"    color: #4d4d4d;\n"
"    font-size: 10px;\n"
"    font-family: Roboto;\n"
"}"))
        self.phoneNumber.setTextFormat(QtCore.Qt.PlainText)
        self.phoneNumber.setObjectName(_fromUtf8("phoneNumber"))
        self.horizontalLayout.addWidget(self.phoneNumber)
        self.messageAlert = QtGui.QLabel(contactBox)
        self.messageAlert.setStyleSheet(_fromUtf8("#messageAlert\n"
"{\n"
"    margin-top: -4px;\n"
"}"))
        self.messageAlert.setText(_fromUtf8(""))
        self.messageAlert.setPixmap(QtGui.QPixmap(_fromUtf8(":/contactBox/newMessageAlert.png")))
        self.messageAlert.setMargin(0)
        self.messageAlert.setObjectName(_fromUtf8("messageAlert"))
        self.horizontalLayout.addWidget(self.messageAlert)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.excerpt = QtGui.QLabel(contactBox)
        self.excerpt.setStyleSheet(_fromUtf8("#excerpt\n"
"{\n"
"    margin-left: 10px;\n"
"    color: #4d4d4d;\n"
"    font-size: 11px;\n"
"    font-family: Roboto;\n"
"}"))
        self.excerpt.setTextFormat(QtCore.Qt.PlainText)
        self.excerpt.setWordWrap(True)
        self.excerpt.setObjectName(_fromUtf8("excerpt"))
        self.verticalLayout.addWidget(self.excerpt)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(contactBox)
        QtCore.QMetaObject.connectSlotsByName(contactBox)

    def retranslateUi(self, contactBox):
        self.name.setText(_translate("contactBox", "First Last", None))
        self.phoneNumber.setText(_translate("contactBox", "(+3368989781)", None))
        self.excerpt.setText(_translate("contactBox", "An excerpt which is so long, that the wordWrap must be enabled and ellipsis would be added…", None))

import mainWindow_rc
