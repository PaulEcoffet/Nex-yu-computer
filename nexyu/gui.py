# -*- coding: utf-8 -*-
import LoginWindow
import MainWindow


class GuiInterface():
    """Gui interface for nexyu computer"""

    def __init__(self):
        self.login = LoginWindow.LoginWindow()
        self.main = None

    def start(self, server):
        self.login = LoginWindow.LoginWindow()
        self.login.setQrCode(server.genUri())
        self.login.show()

    def onConnectionSuccess(self):
        self.login.deleteLater()
        self.main = MainWindow.MainWindow()
