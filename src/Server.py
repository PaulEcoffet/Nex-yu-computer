# -*- coding: utf-8 -*-

from twisted.internet import protocol
from twisted.internet import reactor
from twisted.protocols import basic
from twisted.internet import stdio
import json
import string

class NexYuServProtocol(basic.Int32StringReceiver):

	def stringReceived(self, line):
		send = {"type": "error", "data": None}
		disconnect = False
		try:
			networkMessage = json.loads(line)
		except:
			print("Wrong JSON")
		else:
			if self.verified is True:
				if networkMessage["type"] == "message":
					message = networkMessage["data"]
					print("{} sent {}".format(message["sender"], message["body"]))
					send["type"] = "ok"
				elif networkMessage["type"] == "SMSSent":
					smsSent = networkMessage["data"]
					if smsSent["result"] == 0 :
						print("{} is a success".format(smsSent["id"]))
						send["type"] = "ok"
					else:
						print("{} has failed".format(smsSent["id"]))
				elif networkMessage["type"] == "ContactsList":
					print(line.decode("utf-8"))
			elif networkMessage["type"] == "verifCode":
				if(networkMessage["data"] == self.factory.verifCode):
					self.verified = True
					send["type"] = "ok"
				else:
					send["type"] = "error"
					send["data"] = {"message": "Wrong verifCode"}
					disconnect = True

			self.sendString(json.dumps(send))
			if disconnect is True:
				self.transport.loseConnection()


	def sendSMS(self, number, body):
		sms = {"recipient": unicode(number), "body":unicode(body), "id": int(self.factory.smsId)}
		self.factory.smsId += 1
		self.sendString(json.dumps({"type":"messageToCell", "data":sms}))


	def connectionMade(self):
		self.factory.io.server = self
		self.verified = False
		self.factory.connections += 1

		if(self.factory.connections == 1):
			print("Connected")
			self.sendString(json.dumps({"type":"askVerifCode", "data":None}))
		else:
			self.transport.loseConnection()
			
			
	def connectionLost(self, reason):
		print("Disconnected")
		self.factory.io.server = None
		self.factory.connections -= 1
		

class NexYuServFactory(protocol.ServerFactory):
	protocol = NexYuServProtocol

	def __init__(self, io):
		self.io = io
		self.smsId = 1
		self.connections = 0
		self.verifCode = "TEST"

### FOR DEBUGGING PURPOSE
class Echo(protocol.Protocol):
	def dataReceived(self, data):
		print(data)

class EchoFactory(protocol.Factory):
	def buildProtocol(self, addr):
		return Echo()

class IO(basic.LineOnlyReceiver):
	from os import linesep as delimiter #@UnusedImport

	def __init__(self):
		self.server = None

	def connectionMade(self):
		self.transport.write('>>> ')

	def lineReceived(self, line):
		if self.server is not None and line != '':
			words = string.split(line, " ")
			number = words[0]
			self.server.sendSMS(number, string.join(words[1:], " "))
		else:
			self.transport.write('\nError (not connected or line empty).\n')
			self.transport.write('>>> ')

### END OF DEBUGGING BLOC


class Server:
	def __init__(self):
		io = IO()
		server = NexYuServFactory(io)
		stdio.StandardIO(io)
		reactor.listenTCP(34340, server) #@UndefinedVariable
		reactor.run() #@UndefinedVariable
