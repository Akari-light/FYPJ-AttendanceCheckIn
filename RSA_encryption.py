from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import os

# Generating the keys
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

public_key = private_key.public_key()

# Storing the public key into system env
pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
# os.environ['pubkey'] = pem.decode("utf-8").replace('\n', '\\n')
print(os.environ['pubkey'])
# with open('public_key.pem', 'wb') as f:
#     f.write(pem)