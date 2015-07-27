
# Function to build a 96x96 randomized vigenere using a particular key
def buildVigenere(symbols):
    random.seed(seed)

    n = len(symbols)

    vigenere = [[0 for i in range(n)] for i in range(n)]
    symbols = list(symbols)
    random.shuffle(symbols)
    symbols = ''.join(symbols)
    print('new symbols:')
    print(symbols)
    print(' ')
    
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
