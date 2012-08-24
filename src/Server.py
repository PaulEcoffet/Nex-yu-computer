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
                messages = data["data"]
                for message in messages:
                    print(message["sender"] + " sent " + message["body"])
                send["type"] = "ok"
        self.sendString(json.dumps(send))

    def sendSMS(self, number, body):
        print("{} : {}".format(number, body))
        self.sendString(json.dumps({"type":"xd", "data":None}))
        
    def connectionMade(self):
        self.factory.io.server = self
        print("Connected")
        self.sendString(json.dumps({"type":"ok", "data":None}))



class NexYuServFactory(protocol.ServerFactory):
    protocol = NexYuServProtocol
    
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
        if self.server is not None:
            words = string.split(line, " ")
            number = words[0]
            self.server.sendSMS(number, string.join(words[1:], " "))
        else:
            self.transport.write('Not connected yet.\n')
        self.transport.write('>>> ')


### END OF DEBUGGING BLOC


class Server:
    def __init__(self):
        io = IO()
        server = NexYuServFactory(io)
        stdio.StandardIO(io)
        reactor.listenTCP(34340, server) #@UndefinedVariable
        reactor.run() #@UndefinedVariable
