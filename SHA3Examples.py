import matrixUtils as mu
import theta
import ro
import pi
import chi
import l
import pad
import DataManipulationUtils as dmu 
# import fullRoundInversion
#keccackf takes a string b and a number of rounds nr
def keccackf(b, nr):
    A = dmu.convertListToStateMatrix(b)
    l = dmu.getL(len(b))
    print("range = ",(12 + 2*l - nr), " to ", (12 + 2*l))
    for ir in range((12 + 2*l - nr), (12 + 2*l )):
        A = RND(A,ir)
        Sp = dmu.convertMatrixToList(A,len(b))
    # exit()
    return Sp

#keccackp takes a string b and a number of rounds nr
def keccackp(b, nr):
    A = dmu.convertListToStateMatrix(b)
    l = dmu.getL(len(b))
    for ir in range((0), (nr)):
        A = RND(A,ir)
        Sp = dmu.convertMatrixToList(A,len(b))
    return Sp

def keccackRCNRM(r, c, nr, m):
    b = r + c
    d = 80
    print("r = ", r, "c = ", c, "nr = ", nr)
    print("original message: ", dmu.formatsBitsAsHexString(m))
    #Step 1
    P = m + pad.pad(r,len(m))
    print("Padded message ", dmu.formatsBitsAsHexString(P))   

    #Step 2
    n = len(P)/r
    print("n = ", n)

    if((n % 1) == 0):
        n = int(n)
    else:
        print("error in keccackSponge len(P)/r is not an integer")
    
    #Step 3
    #c = b - r
    #This exists for my sanity rn but C = c
    
    #Step 4
    Plist = [0] * n
    print("Step 4: P = ", P )
    for i in range(0,n):
         Plist[i] = P[(i*r):(i*r + r)]
         
    
    #Step 5
    S = [0] * b
    print("step 5: S = ", S)
    #Step 6
    print("step 6, for i in range(0,n):")
    for i in range(0,n):
        print("i = ",i)
        inputTof = Plist[i] + ([0] * c)
        
        if (len(inputTof) != b):
            print("len(inputTof) != b")
            print("len(inputTof) = ", len(inputTof))
            print("b = ", b)
            exit()
        
        for j in range(0,b):
            inputTof[j] = int(S[j]) ^ int(inputTof[j]) 
        print("input to f = ", dmu.formatBitsAsByteSplitHexString(inputTof, " "))
        # exit()
        # print(i)
        S = keccackp(inputTof, nr) 
        print("result of f: ", dmu.formatBitsAsByteSplitHexString(S, " "))

    #Step 7
    Z = []
    #Steps 8 - 10
    Z += S[:r]

    while True:
        if d <= len(Z):
            # matrix = dmu.convertListToStateMatrix(S)
            # mu.printLanesHex(matrix, True)
            # hexString = dmu.formatsBitsAsHexString(Z)
            # print(hexString)
            return Z[:d] #return TRUNKd(Z)
        else:
            # print(dmu.formatsBitsAsHexString(Z))
            # matrix = dmu.convertListToStateMatrix(S)
            # mu.printLanesHex(matrix, True)
            print("d > len(Z) so squeeze: ")
            S = keccackp(S, nr) 
            Z += S[:r]
            # print("d = ", d, "len Z = ", len(Z))


#Sponge construction using Keccak
#Set desired r for rate and b for width of Keccak function 
def KeccakC(C, N, d):
    b = 1600 #Width of f
    r = b - C  #Rate, 10 is nonstandard!
    
    #Step 1
    P = N + pad.pad(r,len(N))
    # print("result of pad: ", pad.pad(r,len(N)))
    # print("Padded input:", P)
    
    #Step 2
    n = len(P)/r
    print("n = ", n)

    if((n % 1) == 0):
        n = int(n)
    else:
        print("error in keccackSponge len(P)/r is not an integer")
    
    #Step 3
    c = b - r
    #This exists for my sanity rn but C = c
    
    #Step 4
    Plist = [0] * n
    for i in range(0,n):
         Plist[i] = P[(i*r):(i*r + r)]
         # print("i = ", i )
    
    #Step 5
    S = [0] * b
    
    #Step 6
    for i in range(0,n):
        inputTof = Plist[i] + ([0] * c)
        
        if (len(inputTof) != b):
            print("len(inputTof) != b")
            print("len(inputTof) = ", len(inputTof))
            print("b = ", b)
            exit()
        
        for j in range(0,b):
            inputTof[j] = int(S[j]) ^ int(inputTof[j]) 
        # print(len(inputTof))
        # exit()
        # print(i)
        S = keccackf(inputTof, 24) 

    #Step 7
    Z = []
    #Steps 8 - 10
    Z += S[:r]
    
    while True:
        if d <= len(Z):
            return Z[:d] #return TRUNKd(Z)
        else:
            S = keccackf(S, 24) 
            Z += S[:r]
def RND(mat, roundIndex):
    Ap = theta.theta(mat)    

    Sp = dmu.convertMatrixToList(Ap,200)
    print("result of theta: ", dmu.formatBitsAsByteSplitHexString(Sp, " "))
    
    Ap = ro.ro(Ap)
    
    Sp = dmu.convertMatrixToList(Ap,200)
    print("result of rho: ", dmu.formatBitsAsByteSplitHexString(Sp, " "))
    
    Ap = pi.pi(Ap)
    
    Sp = dmu.convertMatrixToList(Ap,200)
    print("result of pi: ", dmu.formatBitsAsByteSplitHexString(Sp, " "))
    
    Ap = chi.chi(Ap)

    Sp = dmu.convertMatrixToList(Ap,200)
    print("result of chi: ", dmu.formatBitsAsByteSplitHexString(Sp, " "))
    
    Ap = l.l(Ap,roundIndex)
    
    Sp = dmu.convertMatrixToList(Ap,200)
    print("result of Iota: ", dmu.formatBitsAsByteSplitHexString(Sp, " "))
    

    return Ap


def SHA3_224(M):
    print("input: ", M)
    
    # myhexStr = dmu.getStringAsHex(M)
    # print(myhexStr)    
    
    rawInput = dmu.formatStringAsBits(M)

    # print("input as bits: ", rawInput)
    inputBitList = rawInput + [0,1]
    # print("input to KeccakC", inputBitList)

    # print("begin KeccakC")
    rawDigest = KeccakC(448, inputBitList, 224)
    
    print(dmu.formatsBitsAsHexString(rawDigest))

    #Swap endianness to match test vectors
    
def SHA3_256(M):
    print("input: ", M)

    rawInput = dmu.tobits(M)
    rawInput = dmu.myEndiannessSwap(rawInput)
    # print(rawInput, " ", len(rawInput))
    

    # print("input as bits: ", rawInput)
    inputBitList = rawInput + [0,1]
    # print("input to KeccakC", inputBitList)

    # print("begin KeccakC")
    rawDigest = KeccakC(512, inputBitList, 256)
    

    #Swap endianness to match test vectors
    rawDigest = dmu.myEndiannessSwap(rawDigest) 
    stringDigest = dmu.convertListToString(rawDigest)
    
    #convert from binary string to hex string
    hexDigest = hex(int(stringDigest,2)) 

    # print(len(hexDigest))
    print(hexDigest[2:])

