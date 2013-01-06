# -*- coding: utf-8 -*-

from PyQt4 import QtGui
import ui.MainWindow.mainWindow as mw
import convBox


class MainWindow(QtGui.QWidget, mw.Ui_nexyuMain):

    def __init__(self, interface, parent=None):
        super(MainWindow, self).__init__(parent)
        self.interface = interface
        self.setupUi(self)
        self.convBoxes = []

    def fillConversationsList(self, conversationsList):
        """
        Fill the conversations list with the items in the conversationsList
        variable.

        conversationsList -- The list of the conversations.
        """
        self.clearConvBoxesList()
        print self.convBoxes
        for conversation in conversationsList:
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
        print "drawing"
        for convbox in self.convBoxes:
            self.ConversationBoxesLayout.addWidget(convbox)
