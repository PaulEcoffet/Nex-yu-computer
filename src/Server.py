# -*- coding: utf-8 -*-

from twisted.internet import protocol
from twisted.protocols import basic
from twisted.internet import stdio
import json
import string
import utils
import socket
import terminal

class NexYuServProtocol(basic.Int32StringReceiver):

	def __init__(self):
		self.contactsList = None

	def stringReceived(self, line):
		send = {"type": "error", "data": None}
		disconnect = False
		try:
			networkMessage = json.loads(line)
		except:
				self.factory.io.write("Wrong JSON")
		else:
			if self.verified is True:
				if networkMessage["type"] == "message":
					message = networkMessage["data"]
					self.factory.io.displaySMS(message)
					send["type"] = "ok"
				elif networkMessage["type"] == "SMSSent":
					smsSent = networkMessage["data"]
					if smsSent["result"] == 0 :
						self.factory.io.write("{} is a success".format(smsSent["id"]))
						send["type"] = "ok"
					else:
						self.factory.io.write("{} has failed".format(smsSent["id"]))
				elif networkMessage["type"] == "ContactsList":
					self.contactsList = networkMessage["data"]
					self.factory.io.write("Contact list received")
			elif networkMessage["type"] == "verifCode":
				if(networkMessage["data"] == self.factory.verifCode):
					self.verified = True
					self.factory.io.write("verified")
					send["type"] = "askContacts"
				else:
					self.factory.io.write("Wrong verifCode")
					send["type"] = "error"
					send["data"] = {"message": "Wrong verifCode"}
					disconnect = True
			self.sendString(json.dumps(send))
			if disconnect is True:
				self.transport.loseConnection()


	def sendSMS(self, number, body):
		if number is not None and number != "":
			sms = {"recipient": unicode(number), "body":unicode(body), "id": int(self.factory.smsId)}
			self.factory.smsId += 1
			self.sendString(json.dumps({"type":"messageToCell", "data":sms}))
		else:
			self.factory.io.write("Invalid recipient")


	def connectionMade(self):
		self.factory.io.server = self
		self.verified = False
		self.factory.connections += 1
		self.factory.io.write("Connected")
		if(self.factory.connections == 1):
			self.sendString(json.dumps({"type":"askVerifCode", "data":None}))
		else:
			self.transport.loseConnection()
					
					
	def connectionLost(self, reason):
		self.factory.io.write("Disconnected")
		self.factory.connections -= 1
		if self.factory.connections < 1:
			self.factory.io.server = None

			

class NexYuServFactory(protocol.ServerFactory):
	protocol = NexYuServProtocol

	def __init__(self, io):
		self.io = io
		self.smsId = 1
		self.connections = 0
		self.verifCode = utils.code_generator()


class Server:
	def __init__(self, _reactor):
		self.reactor = _reactor
		self.port = 34340
		io = terminal.IOTerminal()
		self.nexServer = NexYuServFactory(io)
		stdio.StandardIO(io)
		success = False
		while not success:
			try:
				self.reactor.listenTCP(self.port, self.nexServer) #@UndefinedVariable
			except:
				self.port += 1
			else:
				success = True
				print "Listening to port", self.port
	
	def genUri(self):
		ip = socket.gethostbyname(socket.gethostname()) #TODO Ugly workaround, 
														#shouldn't work everywhere. 
														#Will be fix with global IP and uPnP
		return "nexyu://" + ip + ":" + str(self.port) + "?verif=" + self.nexServer.verifCode
