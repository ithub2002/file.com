import random
import math

def isPrime(n):
    if n == 2: return True
    if n > 2:
        for i in range(2, (n//2)+1):
            if n%i == 0:
                return False
        return True
    return False

def generate_prime():
    while True:
        num = random.getrandbits(8)
        if isPrime(num): return num

class RSA:
    def __init__(self):
        self.n = 0
        self.public_key = 2
        self.private_key = 2

    def generate_keys(self):
        p = generate_prime()
        q = generate_prime()
        self.n = p*q
        phi = (p-1)*(q-1)
        while math.gcd(self.public_key, phi) != 1:
            self.public_key = random.randrange(2, phi)
        for d in range(2, phi):
            if (self.public_key*d)%phi == 1:
                self.private_key = d
                break
        return True

    def encrypt(self, msg):
        result = ""
        for m in msg:
            result += chr(pow(ord(m), self.public_key, self.n))
        return result
    
    def decrypt(self, msg):
        result = ""
        for m in msg:
            result += chr(pow(ord(m), self.private_key, self.n))
        return result

rsa = RSA()
rsa.generate_keys()

message = input("Enter Message to Encrypt: ")
encrypted_message = rsa.encrypt(message)
print("Encrypted Message: " + encrypted_message)
decrypted_message = rsa.decrypt(encrypted_message)
print("Decrypted Message: " + decrypted_message)