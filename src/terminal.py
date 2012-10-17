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
        self.prompt()

    def lineReceived(self, line):
        line = line.encode('raw_unicode_escape').decode('utf-8')
        message = ""
        if self.server and line:
            if line.find('/') == 0:
                words = string.split(line, " ")
                command = words[0]
                if command == "/set":
                    message = self.setDefaultConversation(string.join(words[1:], ' '))
                elif command == "/r":
                    self.server.sendSMS(self.lastSender, string.join(words[1:], ' '))
            else:
                self.server.sendSMS(self.defaultContact["number"], line)
        else:
            message = "Error (not connected or line empty)."
        self.write(message)

    def write(self, line=None, userinput=True):
        if not userinput:
            self.transport.write("\n")
        if line:
            self.transport.write(str(line) + "\n")
        self.prompt()

    def prompt(self):
        self.transport.write("{}>>> ".format(self.defaultContact["name"]))

    def setDefaultConversation(self, name):
        for contact in self.server.contactsList:
            if name in contact["name"]:
                self.defaultContact["name"] = contact["name"]
                self.defaultContact["number"] = contact["phoneNumbers"][0]["number"]
                break
        return "{} with the phone number {} has been set as default contact".format(
                        self.defaultContact["name"], self.defaultContact["number"])

    def displaySMS(self, message):
        # FIXME VERY UGLY FUNCTION !!!!
        self.lastSender = message["sender"]
        name = message["sender"]
        for contact in self.server.contactsList:
            if name in contact["phoneNumbers"][0]["number"]:
                name = contact["name"]
        self.write("{} sent {}".format(name, message["body"]), False)
