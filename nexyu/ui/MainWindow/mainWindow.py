# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow/mainWindow.ui'
#
# Created: Thu Jan 10 15:41:14 2013
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
"#conversationsToolbar, #conversationToolbar\n"
"{\n"
"    border-bottom: 1px solid #808080;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:1 rgba(232, 234, 255, 255), stop:0 rgba(243, 244, 255, 255));\n"
"}\n"
"\n"
"#conversationsToolbar\n"
"{\n"
"    border-right: 1px solid #808080\n"
"}"))
        self.gridLayout = QtGui.QGridLayout(nexyuMain)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.conversationsToolbar = QtGui.QFrame(nexyuMain)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conversationsToolbar.sizePolicy().hasHeightForWidth())
        self.conversationsToolbar.setSizePolicy(sizePolicy)
        self.conversationsToolbar.setMinimumSize(QtCore.QSize(200, 46))
        self.conversationsToolbar.setMaximumSize(QtCore.QSize(400, 16777215))
        self.conversationsToolbar.setStyleSheet(_fromUtf8("#newMessageButton, #searchButton\n"
"{\n"
"    border: none;\n"
"}\n"
""))
        self.conversationsToolbar.setFrameShape(QtGui.QFrame.NoFrame)
        self.conversationsToolbar.setFrameShadow(QtGui.QFrame.Plain)
        self.conversationsToolbar.setLineWidth(0)
        self.conversationsToolbar.setObjectName(_fromUtf8("conversationsToolbar"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.conversationsToolbar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.newMessageButton = QtGui.QPushButton(self.conversationsToolbar)
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
        self.searchButton = QtGui.QPushButton(self.conversationsToolbar)
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
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addWidget(self.conversationsToolbar, 0, 0, 1, 1)
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
        self.messagesList = QtGui.QListWidget(self.conversationContentContainer)
        self.messagesList.setStyleSheet(_fromUtf8("#messagesList\n"
"{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.03, y2:0, stop:0 rgba(242, 242, 242, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}"))
        self.messagesList.setFrameShape(QtGui.QFrame.NoFrame)
        self.messagesList.setFrameShadow(QtGui.QFrame.Plain)
        self.messagesList.setObjectName(_fromUtf8("messagesList"))
        self.verticalLayout.addWidget(self.messagesList)
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
        self.label.setMaximumSize(QtCore.QSize(39, 38))
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
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
        self.messageEdit.setStyleSheet(_fromUtf8("#messageEdit\n"
"{\n"
"    border: none;\n"
"    background-color: white;\n"
"    color: #black;\n"
"}"))
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
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
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
        self.messageEditGrid.setColumnStretch(1, 1)
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
        spacerItem3 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
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
        spacerItem4 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.horizontalLayout_2.addWidget(self.optionToolbar)
        self.horizontalLayout_2.setStretch(0, 1)
        self.gridLayout.addWidget(self.conversationToolbar, 0, 1, 1, 1)
        self.conversationBoxesList = QtGui.QListWidget(nexyuMain)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conversationBoxesList.sizePolicy().hasHeightForWidth())
        self.conversationBoxesList.setSizePolicy(sizePolicy)
        self.conversationBoxesList.setAutoFillBackground(False)
        self.conversationBoxesList.setStyleSheet(_fromUtf8("#conversationBoxesList\n"
"{\n"
"    background-color: #fff;\n"
"    border-right: 1px solid #808080;\n"
"}"))
        self.conversationBoxesList.setFrameShape(QtGui.QFrame.NoFrame)
        self.conversationBoxesList.setFrameShadow(QtGui.QFrame.Plain)
        self.conversationBoxesList.setProperty("showDropIndicator", False)
        self.conversationBoxesList.setUniformItemSizes(True)
        self.conversationBoxesList.setObjectName(_fromUtf8("conversationBoxesList"))
        self.gridLayout.addWidget(self.conversationBoxesList, 1, 0, 1, 1)
        self.gridLayout.setColumnMinimumWidth(0, 200)
        self.gridLayout.setColumnMinimumWidth(1, 300)
        self.gridLayout.setRowMinimumHeight(1, 200)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setRowStretch(1, 1)

        self.retranslateUi(nexyuMain)
        QtCore.QMetaObject.connectSlotsByName(nexyuMain)

    def retranslateUi(self, nexyuMain):
        nexyuMain.setWindowTitle(_translate("nexyuMain", "Nex yu", None))

import mainWindow_rc
