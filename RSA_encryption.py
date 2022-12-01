from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from pathlib import Path
import os


class SetUp:
    def __init__(self):
        self.credentials = self.getCredentials()
        self.file_path = Path(__file__)
        self.current_dir = self.file_path.parent.absolute()

    # Retrive user creds
    def getCredentials(self):
        with open(str(self.current_dir)+'\credentials.txt', 'r'):
            credentials = 1

        # Delete credentials.txt
        os.remove(str(self.current_dir)+'\credentials.txt')

        return credentials
   
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

        with open(str(self.current_dir)+'\public_key.pem', 'wb') as f:
            f.write(pem)

    # Encrypt Credentials
    def Encrypting(self):
        encrypted = self.public_key.encrypt(
            self.credentials,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )



    def __str__(self) -> str:
        return 'Setup File'

if __name__ == '__main__':
    file_path = Path(__file__)
    current_dir = file_path.parent.absolute()
    with open(str(current_dir)+'\credentials.txt', 'r') as f:
        a = f.read()
        print(type(a))

    # Delete credentials.txt
    # os.remove(str(current_dir)+'\credentials.txt')
    pass