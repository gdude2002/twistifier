__author__ = 'Gareth Coles'

import os
import rsa

from twistifier.common.vote import Vote
from twisted.internet.protocol import Protocol, connectionDone


class VotifierClient(Protocol):
    factory = None
    privkey = None
    buffer = ""
    verbose = False

    version = 1.9  # Votifier version

    def __init__(self, factory, privkey, verbose=False):
        """
        :type privkey: rsa.PrivateKey
        """

        self.factory = factory
        self.privkey = privkey
        self.verbose = verbose

    def dataReceived(self, data):
        self.buffer += data

        if len(self.buffer) > 256:
            if self.verbose:
                print("Dropping connection: Data is longer than 256 bytes")

            self.transport.loseConnection()
            return

    def connectionLost(self, reason=connectionDone):
        if len(self.buffer) == 256:
            try:
                data = rsa.decrypt(self.buffer, self.privkey)

                vote = Vote()
                vote.parse(data)

                self.vote_received(vote)
            except Exception as e:
                if self.verbose:
                    print("Unable to decode: {0}".format(e))

    def connectionMade(self):
        self.transport.write(
            "VOTIFIER {0}{1}".format(self.version, os.linesep)
        )

    def vote_received(self, vote):
        print("Vote received: {0} at {1}".format(
            vote.username, vote.service_name
        ))


class DispatcherClient(VotifierClient):
    callback = None

    def __init__(self, factory, privkey, callback, verbose=False):
        VotifierClient.__init__(self, factory, privkey)
        self.callback = callback

    def vote_received(self, vote):
        self.callback(vote)