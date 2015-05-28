__author__ = 'Gareth Coles'

import rsa


def create_keys():
    """
    Generate a new public key and private key, large enough to store the
    Votifier data.

    :returns: a tuple (:py:class:`rsa.PublicKey`, :py:class:`rsa.PrivateKey`)
    """

    return rsa.newkeys(2048)  # The size Votifier generates


def save_keys(public, private, location):
    """
    Save a public and private key to id_rsa.pub and id_rsa in the specified
    location.

    :param public: Public key to save
    :param private: Private key to save
    :param location: Location to save keys

    :type public: rsa.PublicKey
    :type private: rsa.PrivateKey
    :type location: str
    """

    with open("{0}/id_rsa.pub".format(location), "w") as pubfile:
        pubfile.write(public.save_pkcs1())

    with open("{0}/id_rsa".format(location), "w") as privfile:
        privfile.write(private.save_pkcs1())


def load_keys(location):
    """
    Load a public and private key from a specified location.

    :param location: Location to load keys from
    :type location: str
    :returns: a tuple (:py:class:`rsa.PublicKey`, :py:class:`rsa.PrivateKey`)
    """

    return (
        rsa.PublicKey.load_pkcs1(
            open("{0}/id_rsa.pub".format(location), "r").read()
        ), rsa.PrivateKey.load_pkcs1(
            open("{0}/id_rsa".format(location), "r").read()
        )
    )


def save_new_keys(location):
    """
    Generate and save a new public and private key.

    :param location: Location to save keys
    :type location: str
    :returns: a tuple (:py:class:`rsa.PublicKey`, :py:class:`rsa.PrivateKey`)
    """

    pub, priv = create_keys()
    save_keys(pub, priv, location)
    return pub, priv
