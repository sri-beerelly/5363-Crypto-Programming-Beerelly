plain_text = "hug everyone"
cipher_text = ""
dec_text = ""

print(plain_text)

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

key = 3

frequency = {"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0}

# Encryption
def caesar(letter , key):
    
    letter = letter.upper()
    
    if(letter in letters):
        """
        letter = ord(letter) - 65
        letter = (letter + key) % 26
        letter = chr(letter+65)
        """
        num = letters.find(letter)
        num = num + key
        
        if num > 25:
            num = num % 26
        letter = letters[num]
        return letter
    
    return letter

# Decryption
def Decaesar(letter , key):
    
    letter = letter.upper()
    
    if(letter in letters):
        """
        letter = ord(letter) - 65
        letter = (letter + key) % 26
        letter = chr(letter+65)
        """
        num = letters.find(letter)
        num = num - key
        
        if num < 0:
            num = num + 26
        letter = letters[num]
        return letter
    
    return letter

for i in range(len(plain_text)):
   
    cipher_text = cipher_text + caesar(plain_text[i],key)
    
for i in range(len(cipher_text)):
   
    dec_text = dec_text + Decaesar(cipher_text[i],key)

print("Cipher tecxt: %s" % cipher_text)

print("Plain text: %s" % dec_text)

for i in range(len(plain_text)):
    u = plain_text[i].upper()
    if(u in letters):
        frequency[u] = frequency[plain_text[i].upper()] + 1

print(frequency)
