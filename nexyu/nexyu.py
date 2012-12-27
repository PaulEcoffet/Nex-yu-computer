#!/bin/python
# -*- coding: utf-8 -*-
"""
Main file of nexyu.
"""
import sys
import Server
from twisted.internet import stdio
import terminal
import gui
from PyQt4 import QtGui


def main():
    """Main function"""
    app = QtGui.QApplication(sys.argv)
    import qt4reactor
    qt4reactor.install()
    from twisted.internet import reactor

    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        interface = terminal.TerminalInterface()
        stdio.StandardIO(interface)
    else:
        interface = gui.GuiInterface()
    server = Server.Server(reactor, interface)
    interface.start(server)
    reactor.runReturn()
    app.exec_()
    reactor.stop()

if __name__ == "__main__":
    main()
