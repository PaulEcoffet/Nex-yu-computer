#!/bin/python
if __name__ == "__main__":
	import sys
	import Server
	from PyQt4 import QtCore, QtGui
	app = QtGui.QApplication(sys.argv)
	import qt4reactor
	qt4reactor.install()
	from twisted.internet import reactor

	server = Server.Server(reactor)
	
	but = QtGui.QPushButton("Disconnect")
	but.clicked.connect(app.exit())
	but.show()
	
	reactor.runReturn() #@UndefinedVariable
	sys.exit(app.exec_())

