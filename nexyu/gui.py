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

    def start(self):
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
        self.main.fillMessageList(server.getMessageList())

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
        pass
