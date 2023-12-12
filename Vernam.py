def vernam_encrypt(msg, key):
    result = ""
    for i in range(len(msg)):
        m, k = msg[i], key[i]
        m_case = 'A' if m.isupper() else 'a'
        k_case = 'A' if k.isupper() else 'a'
        m_code = ord(m) - ord(m_case)
        k_code = ord(k) - ord(k_case)
        result += chr((m_code + k_code)%26 + ord(m_case))
    return result

def vernam_decrypt(msg, key):
    result = ""
    for i in range(len(msg)):
        m, k = msg[i], key[i]
        m_case = 'A' if m.isupper() else 'a'
        k_case = 'A' if k.isupper() else 'a'
        m_code = ord(m) - ord(m_case)
        k_code = ord(k) - ord(k_case)
        result += chr((m_code - k_code + 26)%26 + ord(m_case))
    return result

msg = input("Enter Message to Encrypt: ")
key = input("Enter Key for Encryption: ")
if len(msg) != len(key):
    print("Key length must be same as length of message.")
    exit(0)
ct = vernam_encrypt(msg, key)
print("Encrypted Message: " + ct)
pt = vernam_decrypt(ct, key)
print("Decrypted Message: " + pt)