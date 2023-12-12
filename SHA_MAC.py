import hashlib

txt1 = b"Ismile"
txt2 = b"Esmile"

hash1 = hashlib.sha256(txt1)
hash2 = hashlib.sha256(txt2)

digest1 = hash1.hexdigest()
digest2 = hash2.hexdigest()

print("First MAC: " + digest1)
print("Second MAC: " + digest2)

if digest1 == digest2:
    print("Both digest are equal so there is integrity.")
else:
    print("Both digest are not equal so there is no integrity.")