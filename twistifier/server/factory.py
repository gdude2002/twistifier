__author__ = 'Gareth Coles'

from twistifier.server.protocol import VotifierClient
from twisted.internet.protocol import Factory


class VotifierFactory(Factory):
    privkey = None

    def __init__(self, privkey):
        self.privkey = privkey

    def buildProtocol(self, addr):
        return VotifierClient(self, self.privkey)
