# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow/messageSent.ui'
#
# Created: Fri Jan 11 13:23:11 2013
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(603, 97)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(_fromUtf8("*\n"
"{\n"
"    background-color: white;\n"
"}"))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.messageSentTopLeftBorder = QtGui.QFrame(Form)
        self.messageSentTopLeftBorder.setStyleSheet(_fromUtf8("#messageSentTopLeftBorder\n"
"{\n"
"    color: #808080;\n"
"}"))
        self.messageSentTopLeftBorder.setFrameShadow(QtGui.QFrame.Plain)
        self.messageSentTopLeftBorder.setFrameShape(QtGui.QFrame.HLine)
        self.messageSentTopLeftBorder.setFrameShadow(QtGui.QFrame.Sunken)
        self.messageSentTopLeftBorder.setObjectName(_fromUtf8("messageSentTopLeftBorder"))
        self.horizontalLayout_2.addWidget(self.messageSentTopLeftBorder)
        self.messageSentDate = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messageSentDate.sizePolicy().hasHeightForWidth())
        self.messageSentDate.setSizePolicy(sizePolicy)
        self.messageSentDate.setStyleSheet(_fromUtf8("#messageSentDate\n"
"{\n"
"    color: #808080;\n"
"    margin-right: 2px;\n"
"    margin-left: 2px;\n"
"}"))
        self.messageSentDate.setTextFormat(QtCore.Qt.PlainText)
        self.messageSentDate.setObjectName(_fromUtf8("messageSentDate"))
        self.horizontalLayout_2.addWidget(self.messageSentDate)
        self.messageSentTopRightBorder = QtGui.QFrame(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messageSentTopRightBorder.sizePolicy().hasHeightForWidth())
        self.messageSentTopRightBorder.setSizePolicy(sizePolicy)
        self.messageSentTopRightBorder.setMinimumSize(QtCore.QSize(40, 0))
        self.messageSentTopRightBorder.setStyleSheet(_fromUtf8("#messageSentTopRightBorder\n"
"{\n"
"    color: #808080;\n"
"}"))
        self.messageSentTopRightBorder.setFrameShadow(QtGui.QFrame.Plain)
        self.messageSentTopRightBorder.setFrameShape(QtGui.QFrame.HLine)
        self.messageSentTopRightBorder.setFrameShadow(QtGui.QFrame.Sunken)
        self.messageSentTopRightBorder.setObjectName(_fromUtf8("messageSentTopRightBorder"))
        self.horizontalLayout_2.addWidget(self.messageSentTopRightBorder)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.messageSentRightBorder = QtGui.QFrame(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messageSentRightBorder.sizePolicy().hasHeightForWidth())
        self.messageSentRightBorder.setSizePolicy(sizePolicy)
        self.messageSentRightBorder.setMinimumSize(QtCore.QSize(5, 0))
        self.messageSentRightBorder.setStyleSheet(_fromUtf8("#messageSentRightBorder\n"
"{\n"
"    color: #09c;\n"
"    background-color: #09c\n"
"}"))
        self.messageSentRightBorder.setFrameShadow(QtGui.QFrame.Plain)
        self.messageSentRightBorder.setLineWidth(10)
        self.messageSentRightBorder.setMidLineWidth(0)
        self.messageSentRightBorder.setFrameShape(QtGui.QFrame.VLine)
        self.messageSentRightBorder.setFrameShadow(QtGui.QFrame.Sunken)
        self.messageSentRightBorder.setObjectName(_fromUtf8("messageSentRightBorder"))
        self.horizontalLayout.addWidget(self.messageSentRightBorder)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 2, 1)
        self.label = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/conversationMessage/right_arrow.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 2, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.messageSent = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messageSent.sizePolicy().hasHeightForWidth())
        self.messageSent.setSizePolicy(sizePolicy)
        self.messageSent.setStyleSheet(_fromUtf8("#messageSent\n"
"{\n"
"    color: #4d4d4d;\n"
"}"))
        self.messageSent.setTextFormat(QtCore.Qt.PlainText)
        self.messageSent.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.messageSent.setWordWrap(True)
        self.messageSent.setObjectName(_fromUtf8("messageSent"))
        self.horizontalLayout_3.addWidget(self.messageSent)
        self.messageSentStatut = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messageSentStatut.sizePolicy().hasHeightForWidth())
        self.messageSentStatut.setSizePolicy(sizePolicy)
        self.messageSentStatut.setText(_fromUtf8(""))
        self.messageSentStatut.setPixmap(QtGui.QPixmap(_fromUtf8(":/Statut/statut_sending.png")))
        self.messageSentStatut.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.messageSentStatut.setObjectName(_fromUtf8("messageSentStatut"))
        self.horizontalLayout_3.addWidget(self.messageSentStatut)
        self.horizontalLayout_3.setStretch(0, 1)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 3, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setRowStretch(3, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.messageSentDate.setText(_translate("Form", "Day, 11, 13:29", None))
        self.messageSent.setText(_translate("Form", "Message test", None))

import mainWindow_rc
