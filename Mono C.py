alphaPT = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphaCT = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

def mono_encrypt(msg):
    ct = ""
    for m in msg:
        temp = alphaCT[alphaPT.index(m.lower())]
        ct += temp.upper() if m.isupper() else temp
    return ct

def mono_decrypt(msg):
    pt = ""
    for m in msg:
        temp = alphaPT[alphaCT.index(m.lower())]
        pt += temp.upper() if m.isupper() else temp
    return pt


msg = input("Enter Message to Encrypt: ")
ct = mono_encrypt(msg)
print("Encrypted Message: " + ct)
pt = mono_decrypt(ct)
print("Decrypted Message: " + pt)
