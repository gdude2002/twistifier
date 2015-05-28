__author__ = 'Gareth Coles'

from twistifier.server.protocol import VotifierClient
from twisted.internet.protocol import Factory


class VotifierFactory(Factory):
    privkey = None
    verbose = False

    def __init__(self, privkey, verbose=False):
        self.privkey = privkey
        self.verbose = verbose

    def buildProtocol(self, addr):
        return VotifierClient(self, self.privkey, verbose=self.verbose)
