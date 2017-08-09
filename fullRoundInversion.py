import matrixUtils as mu
import theta, ro, pi, chi, l, pad
import rhoInverse, chiInverse, piInverse, iotaInverse, thetaInverse
import DataManipulationUtils as dmu 
import random

b = 200

def RND(mat, roundIndex, verbose = False):

    Ap = theta.theta(mat)    

    if(verbose):
        Sp = dmu.convertMatrixToList(Ap,b)
        print("result of theta: ", dmu.formatBitsAsByteSplitHexString(Sp, ""))
    
    Ap = ro.ro(Ap)
    
    if(verbose):
        Sp = dmu.convertMatrixToList(Ap,b)
        print("result of rho: ", dmu.formatBitsAsByteSplitHexString(Sp, ""))
    
    Ap = pi.pi(Ap)
    
    if(verbose):
        Sp = dmu.convertMatrixToList(Ap,b)
        print("result of pi: ", dmu.formatBitsAsByteSplitHexString(Sp, ""))
    
    Ap = chi.chi(Ap)
    if(verbose):
        Sp = dmu.convertMatrixToList(Ap,b)
        print("result of chi: ", dmu.formatBitsAsByteSplitHexString(Sp, ""))
    
    Ap = l.l(Ap,roundIndex)
    
    if(verbose):
        Sp = dmu.convertMatrixToList(Ap,b)
        print("result of Iota: ", dmu.formatBitsAsByteSplitHexString(Sp, ""))
    

    return Ap

def undoRND(mat, roundIndex, verbose = False):
    # Ap = theta.theta(mat)    

    # Sp = dmu.convertMatrixToList(Ap,b)
    # print("result of theta: ", dmu.formatBitsAsByteSplitHexString(Sp, ""))
    
    Ap = iotaInverse.iotaInverse(mat,roundIndex)
    
    if(verbose):
        Sp = dmu.convertMatrixToList(Ap,b)
        print("result of Iota^-1: ", dmu.formatBitsAsByteSplitHexString(Sp, ""))
    
    Ap = chiInverse.chiInverse(Ap)
    
    if(verbose):
        Sp = dmu.convertMatrixToList(Ap,b)
        print("result of chi^-1: ", dmu.formatBitsAsByteSplitHexString(Sp, ""))

    Ap = piInverse.piInverse(Ap)
    
    if(verbose):
        Sp = dmu.convertMatrixToList(Ap,b)
        print("result of pi^-1: ", dmu.formatBitsAsByteSplitHexString(Sp, ""))

    Ap = rhoInverse.rhoInverse(Ap)

    if(verbose):
        Sp = dmu.convertMatrixToList(Ap,b)
        print("result of rho^-1: ", dmu.formatBitsAsByteSplitHexString(Sp, ""))
    

    Ap = thetaInverse.thetaInverse(Ap)

    if(verbose):
        Sp = dmu.convertMatrixToList(Ap,b)
        print("result of theta^-1: ", dmu.formatBitsAsByteSplitHexString(Sp, ""))    
   

    return Ap
def test3():
    nr = 2
    plainTextBin = dmu.generateRandomList(b)
    plainTextHex = dmu.formatBitsAsByteSplitHexString(plainTextBin, "")
    print("BEGIN EXAMPLE")
    print("Parameters: b = ",b, "nr = ", nr)
    print("Plane text (input):", plainTextHex, "\n")
    print("BEGIN keccak-p[",b,",",nr,"]:")
 
    inputToRND = plainTextHex
    A = dmu.convertListToStateMatrix(plainTextBin)
    for i in range(nr):
        # print("ir = ", i)
        # print("Input to RND:", inputToRND)

        A = RND(A,i, True)
    
        binOutput = dmu.convertMatrixToList(A, b)
        hexOutput = dmu.formatBitsAsByteSplitHexString(binOutput, "")
        inputToRND = hexOutput
        # print("Output of RND(A,",i,"): ", hexOutput,"\n")
    
    print("Result of ", nr, "rounds:", hexOutput)
    print("-----------------------------")
    print("Begin inversion:")    

    inputToUndoRND = hexOutput
    for i in range(nr-1,-1,-1):
        # print("ir = ", i)
        # print("Input to RND^-1:", inputToUndoRND)

        A = undoRND(A,i, True)
    
        binOutput2 = dmu.convertMatrixToList(A, b)
        hexOutput2 = dmu.formatBitsAsByteSplitHexString(binOutput2, "")
    
        # print("Output of RND-1(b, ",i,"): ", hexOutput2, "\n")
        inputToUndoRND = hexOutput2

    print("Result of ", nr, "inverse rounds:", hexOutput2)
    if(hexOutput2 == plainTextHex):
        print("Successful recovery")
    
def test():

    ir = random.randint(0,24)
    
    plainTextBin = dmu.generateRandomList(b)
    plainTextHex = dmu.formatBitsAsByteSplitHexString(plainTextBin, "")

    print("b = ",b, "ir = ", ir)
    print("Input to RND:", plainTextHex)

    A = dmu.convertListToStateMatrix(plainTextBin)

    Ap = RND(A,ir)
    
    binOutput = dmu.convertMatrixToList(Ap, b)
    hexOutput = dmu.formatBitsAsByteSplitHexString(binOutput, "")
    
    print("Output of RND: ", hexOutput)

    RecoveredMatrix = undoRND(Ap, ir)
    
    binOutput2 = dmu.convertMatrixToList(RecoveredMatrix, b)
    hexOutput2 = dmu.formatBitsAsByteSplitHexString(binOutput2, "")
    
    print("Output of undoRND function: ", hexOutput2)

    if(hexOutput2 == plainTextHex):
        print("Successful recovery")
    else:
        print("Fail!")
        exit()

def test2():
    hexInput = "024a5518e1e95db53219000000000000000000000000000000"
    binaryList = dmu.fromHexToBits(hexInput)

    print(hexInput)

    Ap = dmu.convertListToStateMatrix(binaryList)
    RecoveredMatrix = undoRND(Ap, 1)
    RecoveredMatrix = undoRND(RecoveredMatrix, 0)

    binOutput2 = dmu.convertMatrixToList(RecoveredMatrix, b)
    hexOutput2 = dmu.formatBitsAsByteSplitHexString(binOutput2, "")
    
    print("Output of undoRND function: ", hexOutput2)

    
test3()
