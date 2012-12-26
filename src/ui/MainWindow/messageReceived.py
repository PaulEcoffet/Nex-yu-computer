# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow/messageReceived.ui'
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

class Ui_messageReceivedContainer(object):
    def setupUi(self, messageReceivedContainer):
        messageReceivedContainer.setObjectName(_fromUtf8("messageReceivedContainer"))
        messageReceivedContainer.resize(707, 89)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(messageReceivedContainer.sizePolicy().hasHeightForWidth())
        messageReceivedContainer.setSizePolicy(sizePolicy)
        messageReceivedContainer.setMinimumSize(QtCore.QSize(0, 64))
        messageReceivedContainer.setStyleSheet(_fromUtf8("*\n"
"{\n"
"    background-color: white;\n"
"}"))
        self.gridLayout = QtGui.QGridLayout(messageReceivedContainer)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(10, 10, 5, 3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.messageReceivedLeftBorder = QtGui.QFrame(messageReceivedContainer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messageReceivedLeftBorder.sizePolicy().hasHeightForWidth())
        self.messageReceivedLeftBorder.setSizePolicy(sizePolicy)
        self.messageReceivedLeftBorder.setMinimumSize(QtCore.QSize(5, 0))
        self.messageReceivedLeftBorder.setStyleSheet(_fromUtf8("#messageReceivedLeftBorder\n"
"{\n"
"    background-color: #09c;\n"
"    color: #09c\n"
"}"))
        self.messageReceivedLeftBorder.setFrameShadow(QtGui.QFrame.Plain)
        self.messageReceivedLeftBorder.setLineWidth(0)
        self.messageReceivedLeftBorder.setFrameShape(QtGui.QFrame.VLine)
        self.messageReceivedLeftBorder.setFrameShadow(QtGui.QFrame.Sunken)
        self.messageReceivedLeftBorder.setObjectName(_fromUtf8("messageReceivedLeftBorder"))
        self.horizontalLayout_2.addWidget(self.messageReceivedLeftBorder)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.messageReceived = QtGui.QLabel(messageReceivedContainer)
        self.messageReceived.setStyleSheet(_fromUtf8("#messageReceived\n"
"{\n"
"    color: #4d4d4d;\n"
"}"))
        self.messageReceived.setTextFormat(QtCore.Qt.PlainText)
        self.messageReceived.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.messageReceived.setWordWrap(True)
        self.messageReceived.setObjectName(_fromUtf8("messageReceived"))
        self.gridLayout.addWidget(self.messageReceived, 1, 1, 2, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.messageReceivedTopLeftBorder = QtGui.QFrame(messageReceivedContainer)
        self.messageReceivedTopLeftBorder.setMinimumSize(QtCore.QSize(0, 0))
        self.messageReceivedTopLeftBorder.setStyleSheet(_fromUtf8("#messageReceivedTopLeftBorder\n"
"{\n"
"    color: #808080;\n"
"}"))
        self.messageReceivedTopLeftBorder.setFrameShadow(QtGui.QFrame.Plain)
        self.messageReceivedTopLeftBorder.setFrameShape(QtGui.QFrame.HLine)
        self.messageReceivedTopLeftBorder.setFrameShadow(QtGui.QFrame.Sunken)
        self.messageReceivedTopLeftBorder.setObjectName(_fromUtf8("messageReceivedTopLeftBorder"))
        self.horizontalLayout.addWidget(self.messageReceivedTopLeftBorder)
        self.messageReceivedDate = QtGui.QLabel(messageReceivedContainer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messageReceivedDate.sizePolicy().hasHeightForWidth())
        self.messageReceivedDate.setSizePolicy(sizePolicy)
        self.messageReceivedDate.setStyleSheet(_fromUtf8("#messageReceivedDate\n"
"{\n"
"    color: #808080;\n"
"    margin-right: 2px;\n"
"    margin-left: 2px;\n"
"}"))
        self.messageReceivedDate.setTextFormat(QtCore.Qt.PlainText)
        self.messageReceivedDate.setObjectName(_fromUtf8("messageReceivedDate"))
        self.horizontalLayout.addWidget(self.messageReceivedDate)
        self.messageReceivedTopRightBorder = QtGui.QFrame(messageReceivedContainer)
        self.messageReceivedTopRightBorder.setWindowModality(QtCore.Qt.NonModal)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messageReceivedTopRightBorder.sizePolicy().hasHeightForWidth())
        self.messageReceivedTopRightBorder.setSizePolicy(sizePolicy)
        self.messageReceivedTopRightBorder.setMinimumSize(QtCore.QSize(80, 0))
        self.messageReceivedTopRightBorder.setMaximumSize(QtCore.QSize(50, 16777215))
        self.messageReceivedTopRightBorder.setStyleSheet(_fromUtf8("#messageReceivedTopRightBorder\n"
"{\n"
"    color: #808080;\n"
"}"))
        self.messageReceivedTopRightBorder.setFrameShadow(QtGui.QFrame.Plain)
        self.messageReceivedTopRightBorder.setFrameShape(QtGui.QFrame.HLine)
        self.messageReceivedTopRightBorder.setFrameShadow(QtGui.QFrame.Sunken)
        self.messageReceivedTopRightBorder.setObjectName(_fromUtf8("messageReceivedTopRightBorder"))
        self.horizontalLayout.addWidget(self.messageReceivedTopRightBorder)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.icon = QtGui.QLabel(messageReceivedContainer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon.sizePolicy().hasHeightForWidth())
        self.icon.setSizePolicy(sizePolicy)
        self.icon.setText(_fromUtf8(""))
        self.icon.setPixmap(QtGui.QPixmap(_fromUtf8(":/conversationMessage/left_arrow.png")))
        self.icon.setObjectName(_fromUtf8("icon"))
        self.gridLayout.addWidget(self.icon, 0, 0, 2, 1)
        self.gridLayout.setRowStretch(2, 1)

        self.retranslateUi(messageReceivedContainer)
        QtCore.QMetaObject.connectSlotsByName(messageReceivedContainer)

    def retranslateUi(self, messageReceivedContainer):
        messageReceivedContainer.setWindowTitle(_translate("messageReceivedContainer", "Form", None))
        self.messageReceived.setText(_translate("messageReceivedContainer", "Message test pour tester quoi. Enfin, bref, le truc habituel, ça surprend personne en vrai, non, je me trompe ?", None))
        self.messageReceivedDate.setText(_translate("messageReceivedContainer", "Day, 11, 13:37", None))

import mainWindow_rc
