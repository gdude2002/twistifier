__author__ = 'Gareth Coles'

class Vote(object):
    service_name = None
    username = None
    address = None
    time_stamp = None

    def parse(self, string):
        split = string.split("\n")

        self.service_name = split[1]
        self.username = split[2]
        self.address = split[3]
        self.time_stamp = split[4]
