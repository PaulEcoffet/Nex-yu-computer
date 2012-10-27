# -*- coding: utf-8 -*-

from twisted.internet import protocol, ssl
from twisted.protocols import basic
from twisted.internet import stdio
import json
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
            if self.verified:
                if networkMessage["type"] == "message":
                    message = networkMessage["data"]
                    self.factory.io.displaySMS(message)
                    send["type"] = "ok"
                elif networkMessage["type"] == "SMSSent":
                    smsSent = networkMessage["data"]
                    if smsSent["result"] == 0:
                        self.factory.io.write("{} is a success".format(
                                                        smsSent["id"]), False)
                        send["type"] = "ok"
                    else:
                        self.factory.io.write("{} has failed".format(
                                                        smsSent["id"]), False)
                elif networkMessage["type"] == "ContactsList":
                    self.contactsList = networkMessage["data"]
                    send["type"] = "ok"
                    self.factory.io.write("Contact list received", False)
            elif networkMessage["type"] == "verifCode":
                if networkMessage["data"] == self.factory.verifCode:
                    self.verified = True
                    self.factory.io.write("verified", False)
                    send["type"] = "askContacts"
                else:
                    self.factory.io.write("Wrong verifCode", False)
                    send["type"] = "error"
                    send["data"] = {"message": "Wrong verifCode"}
                    disconnect = True
            else:
                self.factory.io.write("unknown message:" + line, False)
            self.sendString(json.dumps(send))
            if disconnect:
                self.disconnect()

    def disconnect(self):
        self.transport.loseConnection()

    def sendSMS(self, number, body):
        if number:
            sms = {"recipient": str(number), "body": str(body),
                   "id": int(self.factory.smsId)}
            self.factory.smsId += 1
            self.sendString(json.dumps({"type": "messageToCell", "data": sms}))
        else:
            self.factory.io.write("Invalid recipient")

    def connectionMade(self):
        self.factory.io.server = self
        self.verified = False
        self.factory.connections += 1
        self.factory.io.write("Connected", False)
        if(self.factory.connections == 1):
            self.transport.setTcpKeepAlive(1)
            self.sendString(json.dumps({"type": "askVerifCode", "data": None}))
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
                self.reactor.listenSSL(self.port, self.nexServer,
                    ssl.ClientContextFactory())
                #self.reactor.listenTCP(self.port, self.nexServer)
            except:
                self.port += 1

            else:
                success = True
                print "Listening to port", self.port

    def genUri(self):
        # TODO ip is found with an ugly workaround
        ip = socket.gethostbyname(socket.gethostname())
        return "nexyu://" + ip + ":" + str(self.port) +\
             "?verif=" + self.nexServer.verifCode
