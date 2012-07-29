# -*- coding: utf-8 -*-

from twisted.internet import protocol
from twisted.internet import reactor
from twisted.protocols import basic
import json

class PongProtocol(basic.Int32StringReceiver):
    def stringReceived(self, line):
        data = json.loads(line)
        send = {"type": "error"}
        if(data["type"] == "ping"):
            send["type"] = "pong"
        self.sendString(json.dumps(send))
        self.transport.loseConnection()

class PongFactory(protocol.ServerFactory):
    protocol = PongProtocol

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        print(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

class Server:
    def __init__(self):
        reactor.listenTCP(4242, PongFactory())
        reactor.run()
