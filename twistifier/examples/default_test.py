__author__ = 'Gareth Coles'


from twistifier.server.factory import VotifierFactory
from twistifier.common.keys import save_new_keys

from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor


print "Generating keys. This may take a moment."
pub, priv = save_new_keys(".")

print "Starting server.."
endpoint = TCP4ServerEndpoint(reactor, 8192)
endpoint.listen(VotifierFactory(priv))

print "Started."
reactor.run()
