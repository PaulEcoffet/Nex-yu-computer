# -*- coding: utf-8 -*-

from PyQt4 import QtGui
import ui.MainWindow.mainWindow as mw
#import convBox


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
        self.clearConvList()
        for conversation in conversationsList:
            print conversation["address"]
            print conversation["snippet"]
            print conversation["date"]
            print "--------------------"
#            convbox = convBox.convBox(conversation)
#            self.convBoxes.append(convbox)
#            self.drawConvBoxes()
