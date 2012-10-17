#!/bin/python
# -*- coding: utf-8 -*-

import sys
import Server
import LoginWindow
from PyQt4 import QtGui


def main():
    """Main function"""
    app = QtGui.QApplication(sys.argv)
    import qt4reactor
    qt4reactor.install()
    from twisted.internet import reactor

    server = Server.Server(reactor)
    loginWindow = LoginWindow.LoginWindow()
    loginWindow.setQrCode(server.genUri())
    loginWindow.show()
    reactor.runReturn()
    app.exec_()
    reactor.stop()

if __name__ == "__main__":
    main()
