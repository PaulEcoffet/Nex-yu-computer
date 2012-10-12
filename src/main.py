#!/bin/python
import sys
import Server
import pyqrcode
import LoginWindow
from PyQt4 import QtCore, QtGui

def main():
	"""Main function"""
	app = QtGui.QApplication(sys.argv)
	import qt4reactor
	qt4reactor.install()
	from twisted.internet import reactor

	server = Server.Server(reactor)
	loginWindow = LoginWindow()
	loginWindow.show()
	reactor.runReturn() #@UndefinedVariable
	app.exec_()
	reactor.stop()
	
if __name__ == "__main__":
	main()


