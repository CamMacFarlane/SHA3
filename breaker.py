import matrixUtils as mu
import theta, ro, pi, chi, l, pad
import rhoBreaker, chiBreaker, piBreaker, iotaBreaker, thetaBreaking
import DataManipulationUtils as dmu 
import random

b = 200

def RND(mat, roundIndex, verbose = False):

    Ap = theta.theta(mat)    

    if(verbose):
        Sp = dmu.convertMatrixToList(Ap,b)
        print("result of theta: ", dmu.formatBitsAsByteSplitHexString(Sp, " "))
    
    Ap = ro.ro(Ap)
    
    if(verbose):
        Sp = dmu.convertMatrixToList(Ap,b)
        print("result of rho: ", dmu.formatBitsAsByteSplitHexString(Sp, " "))
    
    Ap = pi.pi(Ap)
    
    if(verbose):
        Sp = dmu.convertMatrixToList(Ap,b)
        print("result of pi: ", dmu.formatBitsAsByteSplitHexString(Sp, " "))
    
    Ap = chi.chi(Ap)
    if(verbose):
        Sp = dmu.convertMatrixToList(Ap,b)
        print("result of chi: ", dmu.formatBitsAsByteSplitHexString(Sp, " "))
    
    Ap = l.l(Ap,roundIndex)
    
    if(verbose):
        Sp = dmu.convertMatrixToList(Ap,b)
        print("result of Iota: ", dmu.formatBitsAsByteSplitHexString(Sp, " "))
    

    return Ap

def undoRND(mat, roundIndex, verbose = False):
    # Ap = theta.theta(mat)    

    # Sp = dmu.convertMatrixToList(Ap,b)
    # print("result of theta: ", dmu.formatBitsAsByteSplitHexString(Sp, " "))
    
    Ap = iotaBreaker.iotaBreaker(mat,roundIndex)
    Ap = chiBreaker.chiBreaker(Ap)
    Ap = piBreaker.piBreaker(Ap)
    Ap = rhoBreaker.rhoBreaker(Ap)
    Ap = thetaBreaking.thetaBreaker(Ap)    
   

    return Ap

def test():

    ir = random.randint(0,24)
    
    plainTextBin = dmu.generateRandomList(b)
    planTextHex = dmu.formatBitsAsByteSplitHexString(plainTextBin, "")

    print("b = ",b, "ir = ", ir)
    print("Input to RND:", planTextHex)

    A = dmu.convertListToStateMatrix(plainTextBin)

    Ap = RND(A,ir)
    
    binOutput = dmu.convertMatrixToList(Ap, b)
    hexOutput = dmu.formatBitsAsByteSplitHexString(binOutput, "")
    
    print("Output of RND: ", hexOutput)

    RecoveredMatrix = undoRND(Ap, ir)
    
    binOutput2 = dmu.convertMatrixToList(RecoveredMatrix, b)
    hexOutput2 = dmu.formatBitsAsByteSplitHexString(binOutput2, "")
    
    print("Output of undoRND function: ", hexOutput2)

    if(hexOutput2 == planTextHex):
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

    
test()
