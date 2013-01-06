# -*- coding: utf-8 -*-

from PyQt4 import QtGui
import ui.MainWindow.conversationBox as cb


class ConvBox(QtGui.QWidget, cb.Ui_conversationBox):
    def __init__(self, conversation, parent=None):
        """
        Constructor of the conversation box

        conversation -- The conversation used for this conversation box.
        """
        super(ConvBox, self).__init__(parent)
        self.setupUi(self)
        self.name.setText(conversation["address"])
        self.phoneNumber.setText(conversation["address"])
        snippet = self.cutSnippet(conversation["snippet"])
        self.excerpt.setText(snippet)

    def cutSnippet(self, snippet):
        if len(snippet) > 40:
            snippet = snippet[0:40]
        snippet = snippet + u"…"
        return snippet

    def setName(self, name):
        """
        Set a name for the conversation

        name -- The name of the contact for the conversation
        """
        self.name.setText(name)
