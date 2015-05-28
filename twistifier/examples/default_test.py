__author__ = 'Gareth Coles'


from twistifier.server.factory import VotifierFactory
from twistifier.common.keys import save_new_keys, has_keys, load_keys

from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

if __name__ == "__main__":
    if not has_keys("."):
        print "Generating keys. This may take a moment."
        _, priv = save_new_keys(".")
    else:
        _, priv = load_keys(".")

    del _

    print "Starting server.."
    endpoint = TCP4ServerEndpoint(reactor, 8192)
    endpoint.listen(VotifierFactory(priv, verbose=True))

    print "Started."
    reactor.run()
