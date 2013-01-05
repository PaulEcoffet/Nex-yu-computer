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
        self.server.askContactsList()
        self.server.askConversationsList()

    def onContactsListReceived(self, contactsList):
        """
        callback triggered when the contactsList is received by the server.

        contactsList -- The contacts list
        """
        self.contactsList = contactsList

    def onConversationsListReceived(self, conversationsList):
        """
        callback triggered when the conversationsList is received by the server.

        contactsList -- The contacts list
        """
        self.conversationsList = conversationsList
        self.main.fillConversationsList(self.conversationsList)

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
        self.server.sendSMS(self.conversation["address"], message)

    def disconnected(self):
        self.main.deleteLater()
