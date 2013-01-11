# -*- coding: utf-8 -*-
import LoginWindow
import MainWindow
from utils.watchedStructures import WatchedDict


class GuiInterface():
    """Gui interface for nexyu computer"""

    def __init__(self):
        """
        """
        self.login = LoginWindow.LoginWindow()
        self.main = None
        self.contacts = WatchedDict()
        self.conversations = WatchedDict()
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
        self.server.askConversationsList()
        self.server.askContactsList()

    def onContactReceived(self, contact):
        """
        callback triggered when a contact is received by the server.

        contact -- The contact received
        """
        self.contacts[contact["id"]] = contact

    def onConversationReceived(self, conversation):
        """
        callback triggered when a conversation is received by the server.

        conversation -- The conversation received
        """
        self.conversations[conversation["thread_id"]] = conversation
        self.main.fillConversationsList(self.conversations.values())

    def setConversation(self, conversationId):
        """
        Set the conversation with the conversationId as active

        contactId -- The id of the contact to set as active
        """
        self.conversation = self.conversations[conversationId]

    def sendMessage(self, message):
        """
        Send a message to the actual conversation

        message -- The message to send
        """
        self.server.sendSMS(self.conversation["address"], message)

    def disconnected(self):
        self.main.deleteLater()
