from twisted.internet import protocol
from twisted.internet import reactor
from twisted.protocols import basic

class FingerProtocol(basic.LineReceiver):
    def lineReceived(self, line):
        self.transport.write("No such user: {}\r\n".format(line))
        self.transport.loseConnection()
class FingerFactory(protocol.ServerFactory):
    protocol = FingerProtocol

reactor.listenTCP(1079, FingerFactory())
reactor.run()
