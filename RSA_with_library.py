# pip uninstall crypto
# pip uninstall pycryptodome
# pip install pycryptodome
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

keyPair=RSA.generate(1024)
k=str(keyPair)


pubKey = keyPair.publickey()
print(pubKey)

pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))


privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))


msg=b'Ismile Academy'
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)
print(encrypted)
