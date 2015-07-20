vigenere = [[0 for i in range(26)] for i in range(26)]

#Build the vigenere matrix
row = 0
col = 0
for i in range(26*26):
    vigenere[row][col] = chr(((col+row)%26)+65)
    col = col + 1
    if col >= 26:
        col = 0
        row = row + 1

# encrypt
# param v : vigenere table
# param k : key
# param m : message
# param ki: key index
# param mi: message index
def encrypt(v,k,m,ki,mi):
    row = ord(m[mi]) - 65
    col = ord(k[ki]) - 65
    #print(row,col)
    return v[row][col]

# decrypt
# param v : vigenere table
# param k : key
# param em : encrypted message
# param ki: key index
# param mi: message index
def decrypt(v,k,em,ki,emi):
    col = ord(k[ki])-65
    msg = em[emi]
    i = 0
    #while(i<26):
    for i in range(26):
        if v[i][col] == msg:
            return v[i][0]
        #i += 1

# printMatrix
def printMatrix(v):
    i=0
    j=0
    k=0
    line = ""

    for i in range(26*26):
        line = line + v[j][k]
        j = j + 1
        if j >= 26:
            print(line)
            line = ""
            j = 0
            k = k + 1


key = "I love crypto"
print("Key--> %s"%key)
print('')
key = key.upper()
key = key.replace(" ", "")

print("Cleared key is: %s" % key)
print('')

message = "We are going to invade europe tomorrow"
#message = " crypto"
print("Message--> %s"%message)
print('')
message = message.upper()
print("Cleared message is: %s" % message)
print('')

cipherText = ""

# Encryption:
for i in range(len(message)):
    mi = i
    ki = i % len(key)
    #print(message[i])
    if ord(message[i]) == 32:
        cipherText = cipherText + ' '
    else:
        cipherText = cipherText + encrypt(vigenere,key,message,ki,mi)


print("Ciphertext --> %s"%cipherText)
print('')

Dec_Text = ""

# Decryption:
for i in range(len(cipherText)):
    mi = i
    ki = i % len(key)
    #print(message[i])
    if ord(cipherText[i]) == 32:
        Dec_Text = Dec_Text + ' '
    else:
        Dec_Text = Dec_Text + decrypt(vigenere,key,cipherText,ki,mi)
        
print("Plaintext by decryption --> %s" %Dec_Text)
