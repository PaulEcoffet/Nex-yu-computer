'''
Created on 28 oct. 2012

Inspired from http://skippylovesmalorie.wordpress.com/

@author: Paul Ecoffet
'''

from OpenSSL import crypto
import os.path
from socket import gethostname

CERT_FILE = "nexyu.crt"
KEY_FILE = "nexyu.key"


def get_self_signed_cert(cert_dir):
    """
    If datacard.crt and datacard.key don't exist in cert_dir, create a new
    self-signed cert and keypair and write them into that directory.
    """
    if not os.path.exists(cert_dir):
        os.mkdir(cert_dir)
    if not os.path.exists(os.path.join(cert_dir, CERT_FILE)) \
            or not os.path.exists(os.path.join(cert_dir, KEY_FILE)):
        # create a key pair
        k = crypto.PKey()
        k.generate_key(crypto.TYPE_RSA, 1024)

        # create a self-signed cert
        cert = crypto.X509()
        cert.get_subject().C = "FR"
        cert.get_subject().L = "."
        cert.get_subject().O = "."
        cert.get_subject().OU = "."
        cert.get_subject().CN = gethostname()
        cert.set_serial_number(1000)
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(10 * 365 * 24 * 60 * 60)
        cert.set_issuer(cert.get_subject())
        cert.set_pubkey(k)
        cert.sign(k, 'sha1')
        print cert.digest('sha1')

        open(os.path.join(cert_dir, CERT_FILE), "wt").write(
            crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
        open(os.path.join(cert_dir, KEY_FILE), "w+").write(
            crypto.dump_privatekey(crypto.FILETYPE_PEM, k))
    return (os.path.join(cert_dir, CERT_FILE),
            os.path.join(cert_dir, KEY_FILE))
