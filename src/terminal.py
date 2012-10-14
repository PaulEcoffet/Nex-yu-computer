# -*- coding: utf-8 -*-

import string
from twisted.protocols import basic

class IOTerminal(basic.LineOnlyReceiver):
	from os import linesep as delimiter  # @UnusedImport

	def __init__(self):
		self.server = None
		self.defaultContact = {"name": "", "number": ""}
		self.lastSender = ""

	def connectionMade(self):
		self.write("")

	def lineReceived(self, line):
		if self.server is not None and line != "":
			if line.find('/') == 0:
				words = string.split(line, " ")
				command = words[0]
				if command == "/set":
					self.setDefaultConversation(string.join(words[1:], ' '))
				elif command == "/r":
					self.server.sendSMS(self.lastSender, string.join(words[1:], ' '))
			else:
				self.server.sendSMS(self.defaultContact["number"], line)
		else:
			self.transport.write("\nError (not connected or line empty).\n")
			self.transport.write(">>> ")
	
	def write(self, line):
		if(line is not None or line != ""):
			self.transport.write("\n" + str(line) + "\n")
		self.transport.write("{}>>> ".format(self.defaultContact["name"]))
		
	def setDefaultConversation(self, name):
		for contact in self.server.contactsList :
			if(contact["name"].find(name)):
				self.defaultContact["name"] = contact["name"]
				self.defaultContact["number"] = contact["phoneNumbers"][0]["number"]
				break
		self.write("{} with the phone number {} has been set as default contact".format(\
						self.defaultContact["name"], self.defaultContact["number"]))

	def displaySMS(self, message):
		# FIXME VERY UGLY FUNCTION !!!!
		self.lastSender = message["sender"]
		name = message["sender"]
		for contact in self.server.contactsList :
			if(contact["phoneNumbers"][0]["number"].find(name)):
				name = contact["name"]
		self.write("{} sent {}".format(name, message["body"]))
