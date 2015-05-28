__author__ = 'Gareth Coles'

import os
import rsa

from twistifier.common.vote import Vote
from twisted.internet.protocol import Protocol, connectionDone


class VotifierClient(Protocol):
    factory = None
    privkey = None
    buffer = ""

    version = 1.9  # Votifier version

    def __init__(self, factory, privkey):
        """
        :type privkey: rsa.PrivateKey
        """

        self.factory = factory
        self.privkey = privkey

    def dataReceived(self, data):
        self.buffer += data

        if len(self.buffer) > 256:
            self.transport.loseConnection()
            return

    def connectionLost(self, reason=connectionDone):
        if len(self.buffer) == 256:
            data = rsa.decrypt(self.buffer, self.privkey)

            vote = Vote()
            vote.parse(data)

            self.vote_received(vote)

    def connectionMade(self):
        self.transport.write(
            "VOTIFIER {0}{1}".format(self.version, os.linesep)
        )

    def vote_received(self, vote):
        print("Vote received: {0} at {1}".format(
            vote.username, vote.service_name
        ))
