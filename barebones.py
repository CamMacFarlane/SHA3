import random
import copy
import matrixUtils as mu
import theta
import ro
import pi
import chi
import l
import pad

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
#generates a list of random bits of a desired length
def generateRandomList(listLen):
    binList = [random.SystemRandom().choice([0,1])]
    for i in range(listLen-1):
        binList += [(random.SystemRandom().choice([0,1]))]
    return binList

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

#keccackp takes a string b and a number of rounds nr
def keccackp(b, nr):
    A = convertListToStateMatrix(b)
    l = getL(len(b))

    for ir in range((12 + 2*l - nr), (12 + 2*l -1)):
        A = RND(A,ir)
        Sp = convertMatrixToList(A,len(b))
        # print("round: ", ir, "S = ", Sp)    
    return Sp

def keccackSponge(N, d):
    r = 10  #Rate, 10 is nonstandard!
    b = 100 #Width of f
    #Step 1
    P = N + pad.pad(r,len(N))
    print("result of pad: ", pad.pad(r,len(N)))
    print("Padded input:", P)
    
    #Step 2
    n = len(P)/r

    if((n % 1) == 0):
        n = int(n)
    else:
        print("error in keccackSponge len(P)/r is not an integer")
    
    #Step 3
    c = b - r
    
    #Step 4
    Plist = [0] * n
    for i in range(0,n):
         Plist[i] = P[(i*r):(i*r + r)]
         print("Plist[",i,"]",Plist[i])
    
    #Step 5
    S = [0] * b
    
    #Step 6
    for i in range(0,n-1):
        inputTof = Plist[i] + ([0] * c)
        print("input to f:", inputTof)
        if (len(inputTof) != b):
            print("len(inputTof) != b")
            print("len(inputTof) = ", len(inputTof))
            print("b = ", b)
            exit()
        for j in range(0,b):
            inputTof[j] = int(S[j]) ^ int(inputTof[j]) 
        S = keccackp(inputTof, 12 + 2*getL(len(inputTof))) 
    Z = []
    Z += S[:r]
    while True:
        if d <= len(Z):
            return Z[:d]
        else:
            S = keccackp(S, 12 + 2*getL(len(S))) 
            Z += S[:r]

def RND(mat, roundIndex):
    A = copy.deepcopy(mat)
    Ap = copy.deepcopy(mat)
    Ap = l.l(chi.chi(pi.pi(ro.ro(theta.theta(mat)))),roundIndex)
    
    return Ap

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
    for b in range(len(bits) / 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

myList = tobits("abc")
print("raw input", myList)
# myList = generateRandomList(100)
output = keccackSponge(myList, 50)
text = convertListToString(output)
print(convertListToString(output))
blah = int(text,2)
print(hex(blah))