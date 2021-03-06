# -*- coding: utf-8 -*-

from twisted.internet import protocol, ssl
from twisted.protocols import basic
import json
import socket
import sslHelper
from twisted.internet.error import CannotListenError
import os.path


class NexYuServProtocol(basic.Int32StringReceiver):

    def __init__(self):
        pass

    def stringReceived(self, line):
        disconnect = False
        try:
            networkMessage = json.loads(line)
        except:
            print "Wrong JSON:", line
        else:
            if networkMessage["type"] == "ready":
                self.transport.setTcpKeepAlive(1)
            elif networkMessage["type"] == "message":
                message = networkMessage["data"]
                self.factory.interface.displaySMS(message)
            elif networkMessage["type"] == "SMSSent":
                self.onSMSSent(networkMessage)
            elif networkMessage["type"] == "contact":
                self.manageContactReceived(networkMessage)
            elif networkMessage["type"] == "conversation":
                self.manageConversationReceived(networkMessage)
            else:
                print("unknown message:", line)
            if disconnect:
                self.disconnect()

    def onSMSSent(self, networkMessage):
        smsSent = networkMessage["data"]
        if smsSent["result"] == 0:
            self.factory.interface.smsSuccess(smsSent["id"])
        else:
            self.factory.interface.smsFailed(smsSent["id"])

    def manageContactReceived(self, networkMessage):
        if networkMessage["type"] != "contact":
            raise Exception("Expecting a contact")
        self.factory.interface.onContactReceived(networkMessage["data"])

    def manageConversationReceived(self, networkMessage):
        if networkMessage["type"] != "conversation":
            raise Exception("Expecting a conversation")

        self.factory.interface.onConversationReceived(networkMessage["data"])

    def disconnect(self):
        self.transport.loseConnection()
        self.factory.interface.disconnected()

    def sendSMS(self, number, body):
        if number:
            sms = {"recipient": unicode(number), "body": unicode(body),
                   "id": int(self.factory.smsId)}
            self.factory.smsId += 1
            self.sendString(json.dumps({"type": "messageToCell", "data": sms}))
        else:
            self.factory.interface.invalidRecipientError()

    def askContactsList(self):
        """
        Ask the client to send its contacts list
        """
        self.sendString(json.dumps({"type": "askContactsList", "data": None}))

    def askConversationsList(self):
        """
        Ask the client to send its contacts list
        """
        self.sendString(json.dumps({"type": "askConversationsList", "data": None}))

    def connectionMade(self):
        self.factory.interface.server = self
        self.factory.connections += 1
        self.factory.interface.connectionSuccess()
        if(self.factory.connections != 1):
            self.disconnect()
        else:
            self.sendString(json.dumps({"type": "ok", "data": None}))

    def connectionLost(self, reason):
        self.factory.interface.connectionLost()
        reason.printTraceback()
        self.factory.connections -= 1
        if self.factory.connections < 1:
            self.factory.interface.server = None


class NexYuServFactory(protocol.ServerFactory):
    protocol = NexYuServProtocol

    def __init__(self, interface):
        self.interface = interface
        self.smsId = 1
        self.connections = 0


class Server:
    def __init__(self, _reactor, interface):
        self.reactor = _reactor
        self.port = 34340
        self.nexServer = NexYuServFactory(interface)
        path = os.path.join("res", "ssl")
        certificateFileName, privateKeyFileName = \
            sslHelper.get_self_signed_cert(path)
        success = False
        while not success:
            try:
                ctxfactory = ssl.DefaultOpenSSLContextFactory(
                    privateKeyFileName, certificateFileName)
                self.reactor.listenSSL(self.port, self.nexServer, ctxfactory)
            except CannotListenError:
                self.port += 1
            else:
                success = True
                print "Listening to port", self.port

    def genUri(self):
        # TODO ip is found with an ugly workaround
        ip = socket.gethostbyname(socket.gethostname())
        return "nexyu://" + ip + ":" + str(self.port) +\
            "?f=" + sslHelper.get_cert_fingerprint(os.path.join(
                "res", "ssl/nexyu.crt"))
