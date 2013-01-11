# -*- coding: utf-8 -*-

from PyQt4 import QtGui
import ui.MainWindow.mainWindow as mw
from convBox import ConvBox


class MainWindow(QtGui.QWidget, mw.Ui_nexyuMain):

    def __init__(self, interface, parent=None):
        super(MainWindow, self).__init__(parent)
        self.interface = interface
        self.convBoxes = {}
        self.update = False
        self.setupUi(self)

    def createConvBox(self, id, conversation):
        """
        Create a convBox
        """
        self.convBoxes[id] = ConvBox(conversation)

    def addConvBox(self, convBox_id, before_id):
        """
        Draw the conversation box with the id convBox_id before the
        conversation box with the id before_id. if  before_id is negative,
        then the convBox is set at the end of the list.
        """
        if before_id >= 0:
            self.ConversationBoxesLayout.insertWidget(
                self.ConversationBoxesLayout.indexOf(self.convBoxes[before_id]),
                self.convBoxes[convBox_id])
        else:
            self.ConversationBoxesLayout.addWidget(self.convBoxes[convBox_id])

    def removeConvBox(self, convBox_id):
        """
        Remove the conversation box at the id convBox_id
        """
        self.ConversationBoxesLayout.removeWidget(self.convBoxes[convBox_id])

    def moveConvBox(self, convBox_id, position):
        """
        Move the conversation box to the given position
        """
        self.removeConvBox(convBox_id)
        self.ConversationBoxesLayout.insertWidget(position,
                                                  self.convBoxes[convBox_id])
