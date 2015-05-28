__author__ = 'Gareth Coles'

import os
import rsa
import multiprocessing


def create_keys(cores=None):
    """
    Generate a new public key and private key, large enough to store the
    Votifier data.

    :returns: a tuple (:py:class:`rsa.PublicKey`, :py:class:`rsa.PrivateKey`)
    """

    if cores is None:
        cores = multiprocessing.cpu_count()

    return rsa.newkeys(2048, poolsize=cores)  # The size Votifier generates


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


def has_keys(location):
    """
    Check whether a keypair exists in the specified location.

    :param location: Location to check for keys
    :return:
    """

    return (os.path.exists("{0}/id_rsa.pub".format(location)) and
            os.path.exists("{0}/id_rsa".format(location)))


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


def save_new_keys(location, cores=None):
    """
    Generate and save a new public and private key.

    :param location: Location to save keys
    :type location: str
    :returns: a tuple (:py:class:`rsa.PublicKey`, :py:class:`rsa.PrivateKey`)
    """

    pub, priv = create_keys(cores=cores)
    save_keys(pub, priv, location)
    return pub, priv
