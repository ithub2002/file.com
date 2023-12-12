def railfence_encrypt(msg, depth):
    result = ""
    rf = [""]*depth
    row, dir = 0, 1
    for m in msg:
        rf[row] += m
        dir = 1 if row==0 else dir
        dir = -1 if row==(depth-1) else dir
        row += dir
    for m in rf: result += m
    return result

def railfence_decrypt(msg, depth):
    result = ""
    rf_num = [0]*depth
    rf_txt = [""]*depth
    row, dir = 0, 1
    for m in msg:
        rf_num[row] += 1
        dir = 1 if row==0 else dir
        dir = -1 if row==(depth-1) else dir
        row += dir
    dir = 0
    for i in range(depth):
        rf_txt[i] = msg[dir:dir+rf_num[i]]
        dir += rf_num[i]
    row, dir = 0, 1
    for m in msg:
        if rf_txt[row] != "":
            result += rf_txt[row][0]
            rf_txt[row] = rf_txt[row][1:]
        dir = 1 if row==0 else dir
        dir = -1 if row==(depth-1) else dir
        row += dir
    return result

msg = input("Enter Message to Encrypt: ")
depth = int(input("Enter Depth: "))
ct = railfence_encrypt(msg, depth)
print("Encrypted Message: " + ct)
pt = railfence_decrypt(ct, depth)
print("Decrypted Message: " + pt)