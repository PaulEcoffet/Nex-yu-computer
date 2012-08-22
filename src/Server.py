# -*- coding: utf-8 -*-

from twisted.internet import protocol
from twisted.internet import reactor
from twisted.protocols import basic
import json

class NexYuServProtocol(basic.Int32StringReceiver):
    def stringReceived(self, line):
        send = {"type": "error"}
        try:
            data = json.loads(line)
        except:
            print("Wrong JSON")
        else:
            if(data["type"] == "ping"):
                send["type"] = "pong"
            elif(data["type"] == "messages"):
                messages = data["data"]
                for message in messages:
                    print(message["sender"] + " sent " + message["body"])
                send["type"] = "ok"

        self.sendString(json.dumps(send))

class NexYuServFactory(protocol.ServerFactory):
    protocol = NexYuServProtocol

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        print(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

class Server:
    def __init__(self):
        reactor.listenTCP(34340, NexYuServFactory()) #@UndefinedVariable
        reactor.run() #@UndefinedVariable
