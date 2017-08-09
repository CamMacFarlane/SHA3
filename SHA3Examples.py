import matrixUtils as mu
import theta
import rho
import pi
import chi
import iota
import pad
import DataManipulationUtils as dmu 


#keccackf takes a string b and a number of rounds nr
#KECCAK-f [b] = KECCAK -p[b, 12 + 2l].
def keccackf(b, nr, verbose=False):
    A = dmu.convertListToStateMatrix(b)
    l = dmu.getL(len(b))
    # print("range = ",(12 + 2*l - nr), " to ", (12 + 2*l))
    for ir in range((12 + 2*l - nr), (12 + 2*l )):
        A = RND(A,ir, verbose)
        Sp = dmu.convertMatrixToList(A,len(b))
    return Sp

#keccackp takes a string b and a number of rounds nr
def keccackp(b, nr):
    A = dmu.convertListToStateMatrix(b)
    l = dmu.getL(len(b))
    for ir in range((0), (nr)):
        A = RND(A,ir)
        Sp = dmu.convertMatrixToList(A,len(b))
    return Sp

#This function mainly exists for testing, allows choice of r and c
def keccackRCNRM(r, c, nr, m,verbose=False):
    b = r + c
    d = 80
    if verbose:
        print("r = ", r, "c = ", c, "nr = ", nr)
        print("original message: ", dmu.formatsBitsAsHexString(m))
    
    #Step 1
    P = m + pad.pad(r,len(m))
    if verbose:
        print("Padded message ", dmu.formatsBitsAsHexString(P))   

    #Step 2
    n = len(P)/r
    if verbose:
        print("n = ", n)

    if((n % 1) == 0):
        n = int(n)
    else:
        print("error in keccackSponge len(P)/r is not an integer")
    
    #Step 3
    #c = b - r
    #This is already true

    #Step 4
    Plist = [0] * n
    if verbose:
        print("Step 4: P = ", P )
    for i in range(0,n):
         Plist[i] = P[(i*r):(i*r + r)]
         
    
    #Step 5
    S = [0] * b
    if verbose:
        print("step 5: S = ", S)
    #Step 6
    if verbose:
        print("step 6, for i in range(0,n):")
    for i in range(0,n):
        if verbose:
            print("i = ",i)
        inputTof = Plist[i] + ([0] * c)
        
        if (len(inputTof) != b):
            print("len(inputTof) != b")
            print("len(inputTof) = ", len(inputTof))
            print("b = ", b)
            exit()
        
        for j in range(0,b):
            inputTof[j] = int(S[j]) ^ int(inputTof[j]) 
        if verbose:
            print("input to f = ", dmu.formatBitsAsByteSplitHexString(inputTof, " "))
        # exit()
        # print(i)
        S = keccackp(inputTof, nr) 
        if verbose:
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
            if verbose:
                print("d > len(Z) so squeeze: ")
            S = keccackp(S, nr) 
            Z += S[:r]
            # print("d = ", d, "len Z = ", len(Z))


#Sponge construction using Keccak
#Set desired r for rate and b for width of Keccak function 
def KeccakC(C, N, d, verbose=False):
    b = 1600 #Width of f
    r = b - C  #Rate, 10 is nonstandard!
    
    #Step 1
    P = N + pad.pad(r,len(N))
    if verbose:
        print("result of pad: ", pad.pad(r,len(N)))
        print("Padded input:", P)
    
    #Step 2
    n = len(P)/r
    
    if verbose:
        print("n = ", n)

    if((n % 1) == 0):
        n = int(n)
    else:
        print("error in keccackSponge len(P)/r is not an integer")
    
    #Step 3
    c = b - r
    #This exists for clarity but C = c
    
    #Step 4
    Plist = [0] * n
    for i in range(0,n):
         Plist[i] = P[(i*r):(i*r + r)]
         if verbose:
            print("i = ", i )
    
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
        S = keccackf(inputTof, 24, verbose) 

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

#Perform RND function on state matrix mat
#If verbose is set to true funciton will print result of each sub function
def RND(mat, roundIndex, verbose = False):
    Ap = theta.theta(mat)    


    if verbose:
        b = len(mat[0][0]*25)
        print(b)
        Sp = dmu.convertMatrixToList(Ap,b)
        print("result of theta: ", dmu.formatBitsAsByteSplitHexString(Sp, " "))
    
    Ap = rho.rho(Ap)
    
    if verbose:
        Sp = dmu.convertMatrixToList(Ap,b)
        print("result of rho: ", dmu.formatBitsAsByteSplitHexString(Sp, " "))
    
    Ap = pi.pi(Ap)
    
    if verbose:
        Sp = dmu.convertMatrixToList(Ap,b)
        print("result of pi: ", dmu.formatBitsAsByteSplitHexString(Sp, " "))
    
    Ap = chi.chi(Ap)

    if verbose:
        Sp = dmu.convertMatrixToList(Ap,b)
        print("result of chi: ", dmu.formatBitsAsByteSplitHexString(Sp, " "))
    
    Ap = iota.iota(Ap,roundIndex)
    
    if verbose:
        Sp = dmu.convertMatrixToList(Ap,b)
        print("result of Iota: ", dmu.formatBitsAsByteSplitHexString(Sp, " "))
    

    return Ap

#SHA-224 as defined in section 6.1 of FIPS 202
def SHA3_224(M, verbose=False):
    print("input: ", M)
    
    # myhexStr = dmu.getStringAsHex(M)
    # print(myhexStr)    
    
    rawInput = dmu.formatStringAsBits(M)

    # print("input as bits: ", rawInput)
    inputBitList = rawInput + [0,1]
    # print("input to KeccakC", inputBitList)

    # print("begin KeccakC")
    rawDigest = KeccakC(448, inputBitList, 224, verbose)
    
    print(dmu.formatsBitsAsHexString(rawDigest))

    #Swap endianness to match test vectors

#SHA-256 as defined in section 6.1 of FIPS 202  
def SHA3_256(M, verbose=False):
    print("input: ", M)

    #convert input to bits and swap endianness
    rawInput = dmu.tobits(M)
    rawInput = dmu.myEndiannessSwap(rawInput)
    
    #Add suffex 01 to the message for Domain Seperation see Section 6.1 in FIPS 202
    inputBitList = rawInput + [0,1]

    #Perform Keccak[512](Message||01, 256)
    rawDigest = KeccakC(512, inputBitList, 256, verbose)
    

    #Swap endianness to match test vectors
    rawDigest = dmu.myEndiannessSwap(rawDigest) 
    stringDigest = dmu.convertListToString(rawDigest)
    
    #Convert from binary string to hex string
    hexDigest = hex(int(stringDigest,2)) 

    #Print the hexDigest without the "0x"
    print(hexDigest[2:])

#SHA-384 as defined in section 6.1 of FIPS 202
def SHA3_384(M, verbose=False):
    print("input: ", M)

    #convert input to bits and swap endianness
    rawInput = dmu.tobits(M)
    rawInput = dmu.myEndiannessSwap(rawInput)
    
    #Add suffex 01 to the message for Domain Seperation see Section 6.1 in FIPS 202
    inputBitList = rawInput + [0,1]

    #Perform Keccak[768](Message||01, 384)
    rawDigest = KeccakC(768, inputBitList, 384, verbose)
    

    #Swap endianness to match test vectors
    rawDigest = dmu.myEndiannessSwap(rawDigest) 
    stringDigest = dmu.convertListToString(rawDigest)
    
    #Convert from binary string to hex string
    hexDigest = hex(int(stringDigest,2)) 

    #Print the hexDigest without the "0x"
    print(hexDigest[2:])

#SHA-512 as defined in section 6.1 of FIPS 202
def SHA3_512(M, verbose=False):
    print("input: ", M)

    #convert input to bits and swap endianness
    rawInput = dmu.tobits(M)
    rawInput = dmu.myEndiannessSwap(rawInput)
    
    #Add suffex 01 to the message for Domain Seperation see Section 6.1 in FIPS 202
    inputBitList = rawInput + [0,1]

    #Perform Keccak[512](Message||01, 256)
    rawDigest = KeccakC(1024, inputBitList, 512, verbose)
    

    #Swap endianness to match test vectors
    rawDigest = dmu.myEndiannessSwap(rawDigest) 
    stringDigest = dmu.convertListToString(rawDigest)
    
    #Convert from binary string to hex string
    hexDigest = hex(int(stringDigest,2)) 

    #Print the hexDigest without the "0x"
    print(hexDigest[2:])

def test():
    print("Provide input for SHA-512: ",end="")
    M = input()
    SHA3_512(M,True)
test()