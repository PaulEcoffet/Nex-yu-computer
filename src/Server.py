# -*- coding: utf-8 -*-

from twisted.internet import protocol
from twisted.internet import reactor
from twisted.protocols import basic
from twisted.internet import stdio
import json
import string

class NexYuServProtocol(basic.Int32StringReceiver):
		def stringReceived(self, line):
				send = {"type": "error"}
				try:
						data = json.loads(line)
				except:
						print("Wrong JSON")
				else:
						if(data["type"] == "messages"):
								message = data["data"]
								print("% sent %".format(message.sender, message.body))
								send["type"] = "ok"
				self.sendString(json.dumps(send))

		def sendSMS(self, number, body):
				sms = {"recipient": unicode(number), "body":unicode(body), "id": int(self.factory.smsId)}
				self.factory.smsId += 1
				self.sendString(json.dumps({"type":"messageToSend", "data":sms}))

		def connectionMade(self):
				self.factory.io.server = self
				print("Connected")
				self.sendString(json.dumps({"type":"ok", "data":None}))
				
		def connectionLost(self, reason):
			print("Disconnected")
			self.factory.io.server = None



class NexYuServFactory(protocol.ServerFactory):
		protocol = NexYuServProtocol
		smsId = 0

		def __init__(self, io):
				self.io = io



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
