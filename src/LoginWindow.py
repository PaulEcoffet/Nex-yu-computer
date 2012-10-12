from PyQt4 import QtGui
import ui.login

class LoginWindow(QtGui.QWidget, ui.login.Ui_loginWindow):
	def __init__(self, parent=None):
		super(LoginWindow, self).__init__(parent)
		self.setupUi(self)
		