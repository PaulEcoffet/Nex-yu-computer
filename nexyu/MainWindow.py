# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import ui.MainWindow.mainWindow as mw
import convBox


class MainWindow(QtGui.QWidget, mw.Ui_nexyuMain):

    def __init__(self, interface, parent=None):
        super(MainWindow, self).__init__(parent)
        self.interface = interface
        self.convBoxes = []
        self.timerSet = False
        self.convList = []
        self.update = False
        self.setupUi(self)

    def fillConversationsList(self, conversationsList):
        """
        Fill the conversations list with the items in the conversationsList
        variable. It has a cooldown of 1 second.

        conversationsList -- The list of the conversations.
        """
        self.convList = conversationsList
        self.update = True
        if not self.timerSet:
            self._updateConvBoxesList(False)
            QtCore.QTimer.singleShot(1000, self._updateConvBoxesList)
            self.timerSet = True

    def _updateConvBoxesList(self, triggered=True):
        """
        Update the conversation boxes list
        """
        if self.update:
            self.clearConvBoxesList()
            for conversation in self.convList:
                convbox = convBox.ConvBox(conversation)
                self.convBoxes.append(convbox)
            self.drawConvBoxes()
            self.update = False
        if triggered:
            self.timerSet = False

    def clearConvBoxesList(self):
        for convBox in self.convBoxes:
            self.ConversationBoxesLayout.removeWidget(convBox)
            convBox.deleteLater()
        del self.convBoxes[:]

    def drawConvBoxes(self):
        """
        Draw the conversation boxes.
        """
        for convbox in self.convBoxes:
            self.ConversationBoxesLayout.addWidget(convbox)
