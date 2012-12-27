# -*- coding: utf-8 -*-
import LoginWindow
import MainWindow


class GuiInterface():
    """Gui interface for nexyu computer"""

    def __init__(self):
        """
        """
        self.login = LoginWindow.LoginWindow()
        self.main = None
        self.contactsList = None
        self.conversationsList = None
        self.server = None
        self.conversation = None

    def start(self, server):
        """
        Function that must be called to start this interface

        server -- A reference to the Server object of the application
        """
        self.login = LoginWindow.LoginWindow()
        self.login.setQrCode(server.genUri())
        self.login.show()

    def connectionSuccess(self):
        """
        Callback triggered when the connection is successfull, display the main window
        """
        self.login.deleteLater()
        self.main = MainWindow.MainWindow(self)
        self.main.show()
        self.conversationsList = self.server.getConversationsList()
        self.contactsList = self.server.getContactsList()
        self.main.fillconversationList(self.conversationsList)

    def setConversation(self, conversationId):
        """
        Set the conversation with the conversationId as active

        contactId -- The id of the contact to set as active
        """
        self.conversation = self.conversationsList[conversationId]

    def sendMessage(self, message):
        """
        Send a message to the actual conversation

        message -- The message to send
        """
        server.sendSMS(conversation.number, message)

    def disconnected(self):
        self.main.deleteLater()
