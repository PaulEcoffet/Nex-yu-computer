# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow/mainWindow.ui'
#
# Created: Wed Dec 26 19:57:40 2012
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

class Ui_nexyuMain(object):
    def setupUi(self, nexyuMain):
        nexyuMain.setObjectName(_fromUtf8("nexyuMain"))
        nexyuMain.resize(740, 561)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/windowDecorators/icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        nexyuMain.setWindowIcon(icon)
        nexyuMain.setStyleSheet(_fromUtf8("*\n"
"{\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"}\n"
"#contactsToolbar, #conversationToolbar\n"
"{\n"
"    border-bottom: 1px solid #808080;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:1 rgba(232, 234, 255, 255), stop:0 rgba(243, 244, 255, 255));\n"
"}\n"
"\n"
"#contactsToolbar\n"
"{\n"
"    border-right: 1px solid #808080\n"
"}"))
        self.gridLayout = QtGui.QGridLayout(nexyuMain)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.contactsBoxListContainer = QtGui.QFrame(nexyuMain)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contactsBoxListContainer.sizePolicy().hasHeightForWidth())
        self.contactsBoxListContainer.setSizePolicy(sizePolicy)
        self.contactsBoxListContainer.setMinimumSize(QtCore.QSize(200, 0))
        self.contactsBoxListContainer.setMaximumSize(QtCore.QSize(250, 16777215))
        self.contactsBoxListContainer.setStyleSheet(_fromUtf8("#contactsBoxListContainer\n"
"{\n"
"    background-color: white;\n"
"    border-right: 1px solid #808080\n"
"}"))
        self.contactsBoxListContainer.setFrameShape(QtGui.QFrame.NoFrame)
        self.contactsBoxListContainer.setFrameShadow(QtGui.QFrame.Plain)
        self.contactsBoxListContainer.setLineWidth(0)
        self.contactsBoxListContainer.setObjectName(_fromUtf8("contactsBoxListContainer"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.contactsBoxListContainer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.scrollArea = QtGui.QScrollArea(self.contactsBoxListContainer)
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtGui.QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.contactsBoxList = QtGui.QWidget()
        self.contactsBoxList.setGeometry(QtCore.QRect(0, 0, 199, 515))
        self.contactsBoxList.setStyleSheet(_fromUtf8("#contactsBoxList\n"
"{\n"
"    background-color:white;\n"
"}"))
        self.contactsBoxList.setObjectName(_fromUtf8("contactsBoxList"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.contactsBoxList)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.scrollArea.setWidget(self.contactsBoxList)
        self.horizontalLayout_4.addWidget(self.scrollArea)
        self.gridLayout.addWidget(self.contactsBoxListContainer, 1, 0, 1, 1)
        self.contactsToolbar = QtGui.QFrame(nexyuMain)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contactsToolbar.sizePolicy().hasHeightForWidth())
        self.contactsToolbar.setSizePolicy(sizePolicy)
        self.contactsToolbar.setMinimumSize(QtCore.QSize(200, 46))
        self.contactsToolbar.setMaximumSize(QtCore.QSize(250, 16777215))
        self.contactsToolbar.setStyleSheet(_fromUtf8("#newMessageButton, #searchButton\n"
"{\n"
"    border: none;\n"
"}\n"
""))
        self.contactsToolbar.setFrameShape(QtGui.QFrame.NoFrame)
        self.contactsToolbar.setFrameShadow(QtGui.QFrame.Plain)
        self.contactsToolbar.setLineWidth(0)
        self.contactsToolbar.setObjectName(_fromUtf8("contactsToolbar"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.contactsToolbar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.newMessageButton = QtGui.QPushButton(self.contactsToolbar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newMessageButton.sizePolicy().hasHeightForWidth())
        self.newMessageButton.setSizePolicy(sizePolicy)
        self.newMessageButton.setMaximumSize(QtCore.QSize(55, 38))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbars/new_message.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newMessageButton.setIcon(icon1)
        self.newMessageButton.setIconSize(QtCore.QSize(55, 38))
        self.newMessageButton.setObjectName(_fromUtf8("newMessageButton"))
        self.horizontalLayout.addWidget(self.newMessageButton)
        self.searchButton = QtGui.QPushButton(self.contactsToolbar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
        self.searchButton.setMaximumSize(QtCore.QSize(54, 38))
        self.searchButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbars/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchButton.setIcon(icon2)
        self.searchButton.setIconSize(QtCore.QSize(54, 38))
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.horizontalLayout.addWidget(self.searchButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout.addWidget(self.contactsToolbar, 0, 0, 1, 1)
        self.conversationContentContainer = QtGui.QFrame(nexyuMain)
        self.conversationContentContainer.setStyleSheet(_fromUtf8("#conversationContentContainer\n"
"{\n"
"    background-color: white;\n"
"}"))
        self.conversationContentContainer.setFrameShape(QtGui.QFrame.NoFrame)
        self.conversationContentContainer.setFrameShadow(QtGui.QFrame.Plain)
        self.conversationContentContainer.setLineWidth(0)
        self.conversationContentContainer.setObjectName(_fromUtf8("conversationContentContainer"))
        self.verticalLayout = QtGui.QVBoxLayout(self.conversationContentContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea_2 = QtGui.QScrollArea(self.conversationContentContainer)
        self.scrollArea_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea_2.setFrameShadow(QtGui.QFrame.Plain)
        self.scrollArea_2.setLineWidth(0)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.conversationContent = QtGui.QWidget()
        self.conversationContent.setGeometry(QtCore.QRect(0, 0, 540, 393))
        self.conversationContent.setAutoFillBackground(False)
        self.conversationContent.setStyleSheet(_fromUtf8("#conversationContent\n"
"{\n"
"    background-color:white;\n"
"}"))
        self.conversationContent.setObjectName(_fromUtf8("conversationContent"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.conversationContent)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        spacerItem3 = QtGui.QSpacerItem(20, 390, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.scrollArea_2.setWidget(self.conversationContent)
        self.verticalLayout.addWidget(self.scrollArea_2)
        self.messageEditGrid = QtGui.QGridLayout()
        self.messageEditGrid.setSpacing(0)
        self.messageEditGrid.setContentsMargins(10, -1, 0, 0)
        self.messageEditGrid.setObjectName(_fromUtf8("messageEditGrid"))
        self.label = QtGui.QLabel(self.conversationContentContainer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/editMessage/keyboard_ic.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.messageEditGrid.addWidget(self.label, 0, 0, 2, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.messageEditLeftBorder = QtGui.QFrame(self.conversationContentContainer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messageEditLeftBorder.sizePolicy().hasHeightForWidth())
        self.messageEditLeftBorder.setSizePolicy(sizePolicy)
        self.messageEditLeftBorder.setMinimumSize(QtCore.QSize(5, 0))
        self.messageEditLeftBorder.setStyleSheet(_fromUtf8("#messageEditLeftBorder\n"
"{\n"
"    color: #ffbb33;\n"
"}"))
        self.messageEditLeftBorder.setFrameShadow(QtGui.QFrame.Plain)
        self.messageEditLeftBorder.setLineWidth(4)
        self.messageEditLeftBorder.setFrameShape(QtGui.QFrame.VLine)
        self.messageEditLeftBorder.setFrameShadow(QtGui.QFrame.Sunken)
        self.messageEditLeftBorder.setObjectName(_fromUtf8("messageEditLeftBorder"))
        self.horizontalLayout_5.addWidget(self.messageEditLeftBorder)
        self.messageEditGrid.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.messageEdit = QtGui.QPlainTextEdit(self.conversationContentContainer)
        self.messageEdit.setMaximumSize(QtCore.QSize(16777215, 100))
        self.messageEdit.setStyleSheet(_fromUtf8(""))
        self.messageEdit.setFrameShape(QtGui.QFrame.NoFrame)
        self.messageEdit.setFrameShadow(QtGui.QFrame.Plain)
        self.messageEdit.setObjectName(_fromUtf8("messageEdit"))
        self.messageEditGrid.addWidget(self.messageEdit, 1, 1, 2, 1)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(-1, 16, -1, 0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.messageEditTopBar = QtGui.QFrame(self.conversationContentContainer)
        self.messageEditTopBar.setBaseSize(QtCore.QSize(0, 0))
        self.messageEditTopBar.setStyleSheet(_fromUtf8("#messageEditTopBar\n"
"{\n"
"    color: #808080;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(179, 179, 179, 255), stop:0.0452261 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
""))
        self.messageEditTopBar.setFrameShadow(QtGui.QFrame.Plain)
        self.messageEditTopBar.setLineWidth(1)
        self.messageEditTopBar.setFrameShape(QtGui.QFrame.HLine)
        self.messageEditTopBar.setFrameShadow(QtGui.QFrame.Sunken)
        self.messageEditTopBar.setObjectName(_fromUtf8("messageEditTopBar"))
        self.verticalLayout_5.addWidget(self.messageEditTopBar)
        self.messageEditGrid.addLayout(self.verticalLayout_5, 0, 1, 1, 2)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 5)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.cancelSending = QtGui.QPushButton(self.conversationContentContainer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelSending.sizePolicy().hasHeightForWidth())
        self.cancelSending.setSizePolicy(sizePolicy)
        self.cancelSending.setMinimumSize(QtCore.QSize(39, 28))
        self.cancelSending.setStyleSheet(_fromUtf8("#cancelSending\n"
"{\n"
"    background-color: none;\n"
"    border: none;\n"
"}"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/editMessage/cancelSending2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancelSending.setIcon(icon3)
        self.cancelSending.setIconSize(QtCore.QSize(39, 28))
        self.cancelSending.setFlat(False)
        self.cancelSending.setObjectName(_fromUtf8("cancelSending"))
        self.verticalLayout_6.addWidget(self.cancelSending)
        self.messageEditGrid.addLayout(self.verticalLayout_6, 1, 2, 2, 1)
        self.messageEditGrid.setRowStretch(2, 1)
        self.verticalLayout.addLayout(self.messageEditGrid)
        self.verticalLayout.setStretch(0, 1)
        self.gridLayout.addWidget(self.conversationContentContainer, 1, 1, 1, 1)
        self.conversationToolbar = QtGui.QFrame(nexyuMain)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conversationToolbar.sizePolicy().hasHeightForWidth())
        self.conversationToolbar.setSizePolicy(sizePolicy)
        self.conversationToolbar.setMinimumSize(QtCore.QSize(0, 46))
        self.conversationToolbar.setMaximumSize(QtCore.QSize(16777215, 46))
        self.conversationToolbar.setFrameShape(QtGui.QFrame.NoFrame)
        self.conversationToolbar.setFrameShadow(QtGui.QFrame.Plain)
        self.conversationToolbar.setLineWidth(0)
        self.conversationToolbar.setObjectName(_fromUtf8("conversationToolbar"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.conversationToolbar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.contactInfo = QtGui.QFrame(self.conversationToolbar)
        self.contactInfo.setFrameShape(QtGui.QFrame.NoFrame)
        self.contactInfo.setFrameShadow(QtGui.QFrame.Plain)
        self.contactInfo.setLineWidth(0)
        self.contactInfo.setObjectName(_fromUtf8("contactInfo"))
        self.horizontalLayout_2.addWidget(self.contactInfo)
        self.optionToolbar = QtGui.QFrame(self.conversationToolbar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.optionToolbar.sizePolicy().hasHeightForWidth())
        self.optionToolbar.setSizePolicy(sizePolicy)
        self.optionToolbar.setStyleSheet(_fromUtf8("#optionToolbar\n"
"{\n"
"    background-image: url(:/toolbars/LeftBorder.png);\n"
"    background-repeat: none;\n"
"    padding-left: 20 px;\n"
"}"))
        self.optionToolbar.setFrameShape(QtGui.QFrame.NoFrame)
        self.optionToolbar.setFrameShadow(QtGui.QFrame.Plain)
        self.optionToolbar.setObjectName(_fromUtf8("optionToolbar"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.optionToolbar)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem5 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.optionButton = QtGui.QPushButton(self.optionToolbar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.optionButton.sizePolicy().hasHeightForWidth())
        self.optionButton.setSizePolicy(sizePolicy)
        self.optionButton.setMinimumSize(QtCore.QSize(29, 36))
        self.optionButton.setMaximumSize(QtCore.QSize(29, 36))
        self.optionButton.setStyleSheet(_fromUtf8("#optionButton\n"
"{\n"
"    background-color: none;\n"
"    border: none;\n"
"}"))
        self.optionButton.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbars/options.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.optionButton.setIcon(icon4)
        self.optionButton.setIconSize(QtCore.QSize(29, 38))
        self.optionButton.setAutoDefault(False)
        self.optionButton.setDefault(False)
        self.optionButton.setFlat(False)
        self.optionButton.setObjectName(_fromUtf8("optionButton"))
        self.horizontalLayout_3.addWidget(self.optionButton)
        self.disconnectButton = QtGui.QPushButton(self.optionToolbar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.disconnectButton.sizePolicy().hasHeightForWidth())
        self.disconnectButton.setSizePolicy(sizePolicy)
        self.disconnectButton.setMinimumSize(QtCore.QSize(32, 36))
        self.disconnectButton.setMaximumSize(QtCore.QSize(32, 36))
        self.disconnectButton.setStyleSheet(_fromUtf8("#disconnectButton\n"
"{\n"
"    border:none;\n"
"    background: none;\n"
"}"))
        self.disconnectButton.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/toolbars/disconnect.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.disconnectButton.setIcon(icon5)
        self.disconnectButton.setIconSize(QtCore.QSize(32, 36))
        self.disconnectButton.setObjectName(_fromUtf8("disconnectButton"))
        self.horizontalLayout_3.addWidget(self.disconnectButton)
        spacerItem6 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.horizontalLayout_2.addWidget(self.optionToolbar)
        self.horizontalLayout_2.setStretch(0, 1)
        self.gridLayout.addWidget(self.conversationToolbar, 0, 1, 1, 1)

        self.retranslateUi(nexyuMain)
        QtCore.QMetaObject.connectSlotsByName(nexyuMain)

    def retranslateUi(self, nexyuMain):
        nexyuMain.setWindowTitle(_translate("nexyuMain", "Nex yu", None))

import mainWindow_rc
