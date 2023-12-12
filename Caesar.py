def caesar_encrypt(msg, k):
    ct = ""
    for m in msg:
        temp = ord("a") if m.islower() else ord("A")
        ct += chr((ord(m) - temp + k)%26 + temp)
    return ct

def caesar_decrypt(msg, k):
    pt = ""
    for m in msg:
        temp = ord("a") if m.islower() else ord("A")
        pt += chr((ord(m) - temp - k + 26)%26 + temp)
    return pt

msg = input("Enter Message to Encrypt: ")
k = int(input("Enter Key Size: "))
ct = caesar_encrypt(msg, k)
print("Encrypted Message: " + ct)
pt = caesar_decrypt(ct, k)
print("Decrypted Message: " + pt)