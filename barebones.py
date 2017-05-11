import matrixUtils as mu
import theta
import ro
import pi
import chi
import l
import pad
import DataManipulationUtils as dmu 

#keccackp takes a string b and a number of rounds nr
def keccackp(b, nr):
    A = dmu.convertListToStateMatrix(b)
    l = dmu.getL(len(b))
    print("range = ",(12 + 2*l - nr), " to ", (12 + 2*l))
    for ir in range((12 + 2*l - nr), (12 + 2*l )):
        A = RND(A,ir)
        Sp = dmu.convertMatrixToList(A,len(b))
        digest = dmu.frombits(Sp[:224])
        # print(ir)
        # printStringAsHex(digest)
    # exit()
    return Sp


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
        S = keccackp(inputTof, 24) 

    #Step 7
    Z = []
    #Steps 8 - 10
    Z += S[:r]
    
    while True:
        if d <= len(Z):
            return Z[:d] #return TRUNKd(Z)
        else:
            S = keccackp(S, 24) 
            Z += S[:r]
            print("d = ", d, "len Z = ", len(Z))

def RND(mat, roundIndex):
    Ap = l.l(chi.chi(pi.pi(ro.ro(theta.theta(mat)))),roundIndex)    
    return Ap


def SHA3_224(M):
    print("input: ", M)
    myhexStr = dmu.getStringAsHex(M)
    # print(myhexStr)
    rawInput = dmu.tobits(M)
    rawInput = dmu.myEndiannessSwap(rawInput)
    # print(rawInput, " ", len(rawInput))
    

    # print("input as bits: ", rawInput)
    inputBitList = rawInput + [0,1]
    # print("input to KeccakC", inputBitList)

    # print("begin KeccakC")
    rawDigest = KeccakC(448, inputBitList, 224)
    

    #Swap endianness to match test vectors
    rawDigest = dmu.myEndiannessSwap(rawDigest) 
    stringDigest = dmu.convertListToString(rawDigest)
    
    #convert from binary string to hex string
    hexDigest = hex(int(stringDigest,2)) 

    # print(len(hexDigest))
    print(hexDigest[2:])


myStr = 'abc'
SHA3_224(myStr)
