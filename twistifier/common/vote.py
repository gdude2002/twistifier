__author__ = 'Gareth Coles'

class Vote(object):
    service_name = None
    username = None
    address = None
    time_stamp = None

    def parse(self, string):
        split = string.strip().split("\n")

        if split[0] != "VOTE":
            raise ValueError("Decrypted data invalid or key mismatch")

        self.service_name = split[1]
        self.username = split[2]
        self.address = split[3]
        self.time_stamp = split[4]

    def __str__(self):
        if self.service_name is None:
            return "<Vote | No data>"

        return ("<Vote | Service: {0} | Username: {1} "
                "| Address: {2} | Timestamp: {3}".format(self.service_name,
                                                         self.username,
                                                         self.address,
                                                         self.time_stamp)
                )
