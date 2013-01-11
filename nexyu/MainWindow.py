# -*- coding: utf-8 -*-

from PyQt4 import QtGui
import ui.MainWindow.mainWindow as mw
import convBox


class MainWindow(QtGui.QWidget, mw.Ui_nexyuMain):

    def __init__(self, interface, parent=None):
        super(MainWindow, self).__init__(parent)
        self.interface = interface
        self.convBoxes = []
        self.convList = []
        self.update = False
        self.setupUi(self)

    def fillConversationsList(self, conversationsList):
        """
        Fill the conversations list with the items in the conversationsList
        variable. It has a cooldown of 1 second.

        conversationsList -- The list of the conversations.
        """
        self.clearConvBoxesList()
        for conversation in self.convList:
            convbox = convBox.ConvBox(conversation)
            self.convBoxes.append(convbox)
        self.drawConvBoxes()

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
