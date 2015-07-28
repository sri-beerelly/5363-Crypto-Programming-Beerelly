############################################
# Name: Srikanth Reddy Beerelly
# Class: CMPS 5363 Cryptography
# Date: 27 july 2015
# Program 2- Randomized vigenere
############################################

import random
#seed = 7487383487438734

symbols ="""!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~"""

# keywordFromSeed :
# Function to genrerate a secret keyword from the given seed
# @param int - seed: incoming secret integer for key generation
# @returns string - keyword for encryption and decryption

def keywordFromSeed(seed):
    Letters = []
    seed = int(seed)

    while seed > 0:
        Letters.insert(0,chr((seed % 100) % 26 + 65))
        seed = seed // 10
        
    return ''.join(Letters)

# buildVigenere :
# Function to build a 95x95 randomized vigenere using a particular keyword
# @param string - symbols of length 95
# @param int - seed: secret key for the random generation of each in symbols
# @returns list- randomized vigenere

def buildVigenere(symbols,seed):
    random.seed(seed)

    n = len(symbols)

    vigenere = [[0 for i in range(n)] for i in range(n)]
    
    symbols = list(symbols)
    random.shuffle(symbols)
    symbols = ''.join(symbols)
    #print('new symbols:')
    #print(symbols)
    #print(' ')
    
    for sym in symbols:
        random.seed(seed)
        myList = []
    
        for i in range(n):
            r = random.randrange(n)
            
            if r not in myList:
                myList.append(r)
            else:
                while(r in myList):
                    r = random.randrange(n)
            
                myList.append(r)
                               
            while(vigenere[i][r] != 0):
                r = (r + 1) % n
            
            vigenere[i][r] = sym
            
    return vigenere

# printMatrix :
# Function to create a 95x95 matrix from randomized vigenere
# @param v - takes a vigenere list
# prints a 95x95 randomized matrix

def printMatrix(v):
    i=0
    j=0
    k=0
    Line =''
    for i in range(95*95):
        Line += str(v[j][k])
        k +=1
        if k>=95:
            print(Line)
            Line = ''
            k =0
            j +=1

# encrypt :
# Function to encrypt a plain message using keyword throgh the randomized vigenere
# @param m - plain message
# @param s - secret integer to generate a randomized vigenere and a keyword for encryption
# @returns string - encrypted message

def encrypt(m,s):
    
    v = buildVigenere(symbols,s)
    
    k = keywordFromSeed(s)
    
    # en:
    # takes vigenere, plain message, keyword, keyword index and message index
    # returns a encrypted symbol from the randomized vigenere
    def en(v,m,k,mi,ki):
        
        temp1 = m[mi]
        col = 0
        for x in range(1):
            for y in range(len(symbols)):
                if (temp1 == v[x][y]):
                    col = y                    
        temp2 = k[ki]
        row = 0
        for p in range(len(symbols)):
            for q in range(1):
                if (temp2 == v[p][q]):
                    row = p

        return v[row][col]
    
    enc_text = "" 

    # generating encrypted text
    for i in range(len(m)):
        mi = i
        ki = i % len(k)
        
        enc_text = enc_text + en(v,m,k,mi,ki)
        
    #print(enc_text)
                
    return enc_text

# decrypt :
# Function to decrypt a message using the same key and same randomized vigenere
# @param em - decrypted message
# @param s - secret integer to generate a randomized vigenere and a keyword for decryption
# @returns string - decrypted message

def decrypt(em,s):
    
    v = buildVigenere(symbols,s)
    
    k = keywordFromSeed(s)
    

    # dc:
    # takes vigenere, keyword, encrypted message, encrypted message index andkeyword index 
    # returns a decrypted symbol from the randomized vigenere
    def dc(v,k,em,emi,eki):
        row = 0
        temp1 = k[eki]
        for x in range(1):
            for y in range(len(symbols)):
                if (temp1 == v[y][x]):
                     row = y
                     
        temp2 = em[emi]
        col = 0
        for z in range(len(symbols)):
            
            if (temp2 == v[row][z]):
                col = z
                
        return v[0][col]
                
    dec_text = ""

    # genearting decrypted text
    for i in range(len(em)):
        emi = i
        eki = i % len(k)
        
        dec_text = dec_text + dc(v,k,em,emi,eki)

    #print(dec_text)
        
    return dec_text



def main():

    message = 'srikanth is my name.'
    print('Plain text message: {}\n'.format(message))
    print(' ')

    
    
    keyWord = keywordFromSeed(seed)
    print('keyword :')
    print(keyWord)
    
    vig = buildVigenere(symbols)
    #print(vig)

    print('Vigenere Matrix:')
    #printMatrix(vig)
    print(' ')

    encryptedText = encrypt(message,keyWord)
    print(encryptedText)

    decryptedText= decrypt(encryptedText,keyWord)
    print(decryptedText)


if __name__ == '__main__':
    main()


    


