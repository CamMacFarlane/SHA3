import copy
import matrixUtils as mu
import theta
import ro
import pi
import chi
import l
import random
import time
def verboseTest(IR):
    testString = generateRandomString(100)
    A = convertStringToStateMatrix(testString)

    mu.populate(A)

    Ap = theta.theta(A)
    print("\n    After theta (A') | Before theta (A)")
    mu.matPrint(Ap, 'c', True, True, A)

    A = Ap
    Ap = ro.ro(Ap)
    print("\n           After Ro | Before Ro")
    mu.matPrint(Ap, 'l', True, True, A)


    AFIPS = mu.matToFIPS(Ap)
    A = Ap
    Ap = pi.pi(Ap)

    AFIPS = mu.matToFIPS(A)
    ApFIPS = mu.matToFIPS(Ap)
    mu.printSheet(AFIPS , ApFIPS, "A", "A'")

    A = Ap
    Ap = chi.chi(Ap)
    print("\n    After chi (A')   | Before chi (A)")
    mu.matPrint(Ap, 'r', True, True, A)                

    A = Ap
    Ap = l.l(Ap, IR)
    print("\n    After l (A')   | Before l (A)")
    mu.matPrint(Ap, 'l', True, True, A)   

    print("\nSingle round, with:\nRound index = ", IR, "\nw = ", len(A[0][0]), "\nstring lenght = ", len(testString))   
    Sp = convertMatrixToString(Ap,len(testString))
    print("Inital String: ", testString)
    print("Result String: ", Sp)


def RND(mat, roundIndex):
    A = copy.deepcopy(mat)
    Ap = copy.deepcopy(mat)
    Ap = l.l(chi.chi(pi.pi(ro.ro(theta.theta(mat)))),roundIndex)
    
    AFIPS = mu.matToFIPS(A)
    ApFIPS = mu.matToFIPS(Ap)
    
    return Ap
    # mu.matPrint(Ap, 'r', False, True)

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

#generates a random binary string of length len
def generateRandomString(len):
    str = ''.join(random.SystemRandom().choice(['0','1']) for _ in range(len))
    return str

#converts string b to state matrix as per 3.1.2 in FIPS SHA3 document
def convertStringToStateMatrix(b):
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

def convertMatrixToString(A, strlen):
    w = getW(strlen)
    SaL = list('x' * strlen)

    for x in range(5):
        for y in range(5):
            for z in range(w):
               SaL[w*(5*y + x) + z] = str(A[x][y][z])
    
    SaS = "".join(SaL)
    return SaS

#keccackp takes a string b and a number of rounds nr
def keccackp(b, nr):
    A = convertStringToStateMatrix(b)
    l = getL(b)

    for ir in range((12 + 2*l - nr), (12 + 2*l -1)):
        A = RND(A,ir)
        Sp = convertMatrixToString(A,len(b))
        # print("round: ", ir, "S = ", Sp)    
    return Sp

def keccackpTestRandString(strLen):
    testString = generateRandomString(strLen)  
    result = keccackp(testString, 12 + 2*getL(len(testString)))    
    print("inital string: ", testString)
    print("result string: ", result)

def keccackpTestString(inputString):
    result = keccackp(inputString, 12 + 2*getL(len(inputString)))    
    print("inital string: ", inputString)
    print("result string: ", result)

def timeTest(inputString):
    t1 = time.time()
    for i in range(100): keccackp(inputString, 12 + 2*getL(len(inputString)))    
    t2 = time.time()
    avg = (t2 - t1)/100
    print("avg run time = ",avg)

keccackpTestRandString(100)
# keccackpTestString("1000000100000101111111100101000011001001010010110010010100011110010101101000000001101010000000000110")
# timeTest("1000000100000101111111100101000011001001010010110010010100011110010101101000000001101010000000000110")
# verboseTest(0)

