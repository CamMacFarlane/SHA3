import random #for generateRandomString

#returns w value for different approved String lengths
def getW(lengthOfString):
    return{
    25:1,
    50:2,
    100:4,
    200:8,
    400:16,
    800:32,
    1600:64 
    }.get(lengthOfString, -1);

#returns l value for different approved String lengths
def getL(lengthOfString):
    return{
    25:0,
    50:1,
    100:2,
    200:3,
    400:4,
    800:5,
    1600:6 
    }.get(lengthOfString, -1);

def convertMatrixToList(A, lLen):
    AaL = list('x' * lLen)
    w = getW(lLen)
    for x in range(5):
        for y in range(5):
            for z in range(w):
               AaL[w*(5*y + x) + z] = str(A[x][y][z])
    return AaL


#converts a list to a 3d state matrix
def convertListToStateMatrix(b):
    #get our z dimension
    w = getW(len(b))
    
    #Ensure w is valid 
    if(w == -1):
        print("Invalid string length", len(b), "exiting now")
        exit()
    
    #create empty 5 by 5 by w matrix
    A = [[[0 for k in range(w)] for k in range(5)]
        for k in range(5)]
    
    #populate A with contents of b
    for x in range(5):
        for y in range(5):
            for z in range(w):
                A[x][y][z] = int(b[w*(5*y + x) + z])
    
    #returns pointer to A
    return A

def convertListToString(l):
     string = ''.join(str(i) for i in l)
     return string

def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def frombits(bits):
    chars = []
    for b in range(int(len(bits) / 8)):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

def printStringAsHex(s):
    for i in range(0,len(s)):
        hexStr = hex(ord(s[i]))
        print(hexStr[2:], end = "")
    print()


def getStringAsHex(s):
    ret = ""
    for i in range(0,len(s)):
        hexStr = hex(ord(s[i]))
        ret = ret + hexStr[2:]    
    
    return ret


def chunkList(myList, chunkSize):
    chunks = []
    for i in range(0, len(myList), chunkSize):
        chunks = chunks + [myList[i:i+chunkSize]]
    return chunks

#reverses each byte
def myEndiannessSwap(myBinList):
    chunks = chunkList(myBinList,8)
    ret = []
    numChunks = len(chunks)
    old = 0

    for chunk in chunks:
        ret = ret + chunk[::-1]
    return ret

#returns a list of bits of the string 
def formatStringAsBits(string):
    bits = tobits(string)
    bits = myEndiannessSwap(bits)
    return bits

#returns a hex string of the bits input with a space between each byte
def formatBitsAsByteSplitHexString(bits,splitString):
    bits = myEndiannessSwap(bits) 
    stringDigest = convertListToString(bits)
    hexDigest = hex(int(stringDigest,2)) 
    if (len(stringDigest)/4) % 1 == 0:    
        hexDigest = hexDigest[2:].zfill(len(stringDigest)//4)
    else:
        hexDigest = hexDigest[2:].zfill((len(stringDigest)//4) + 1)
        
    for i in range(2, len(hexDigest) + len(hexDigest)//2, 3):
        hexDigest = hexDigest[:i] + splitString + hexDigest[i:]

    return hexDigest

#returns a hex string of the bits input
def formatsBitsAsHexString(bits):
    bits = myEndiannessSwap(bits) 
    stringDigest = convertListToString(bits)
    hexDigest = hex(int(stringDigest,2)) 
    return hexDigest[2:]

def generateRandomList(listLen):
    binList = [random.SystemRandom().choice([0,1])]
    for i in range(listLen-1):
        binList += [(random.SystemRandom().choice([0,1]))]
    return binList