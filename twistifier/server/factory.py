__author__ = 'Gareth Coles'

from twistifier.server.protocol import VotifierClient
from twisted.internet.protocol import Factory


class VotifierFactory(Factory):
    privkey = None
    verbose = False
    protocol_class = VotifierClient

    def __init__(self, privkey, verbose=False, protocol_class=VotifierClient):
        self.privkey = privkey
        self.verbose = verbose
        self.protocol_class = protocol_class

    def buildProtocol(self, addr):
        return self.protocol_class(self, self.privkey, verbose=self.verbose)
