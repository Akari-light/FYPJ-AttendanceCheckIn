from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from pathlib import Path
import os


class SetUp:
    def __init__(self):
        self.current_path = Path(__file__)
        self.current_dir = self.current_path.parent.absolute()

    def getCredentials(self):
        return
    
    # Generating the keys
    def keyGen(self):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        self.public_key = self.private_key.public_key()

    # Saving PK
    def generatePEM(self):
        pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        with open(self.current_dir+'\public_key.pem', 'wb') as f:
            f.write(pem)

    # Encrypt Credentials
    '''
    def Encrypting(self):


        encrypted = self.public_key.encrypt(
            credentials,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
    '''

    def __str__(self) -> str:
        return 'Current Path:\n{}\n\nCurrent Dir\n{}'.format(self.current_path, self.current_dir)
