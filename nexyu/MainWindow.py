# -*- coding: utf-8 -*-

from PyQt4 import QtGui
import ui.MainWindow.mainWindow as mw


class MainWindow(QtGui.QWidget, mw.Ui_nexyuMain):

    def __init__(self, interface, parent=None):
        super(MainWindow, self).__init__(parent)
        self.interface = interface
        self.setupUi(self)
        self.convBoxes = None

    def fillConversationsList(conversationsList):
        """
        Fill the conversations list with the items in the conversationsList
        variable.

        conversationsList -- The list of the conversations.
        """
        self.clearConvList()
        for conversation in conversationsList:
                self.convBoxes.append(convbox)
                self.drawConvBoxes()

