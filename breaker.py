import matrixUtils as mu
import theta, ro, pi, chi, l, pad
import rhoBreaker, chiBreaker, piBreaker, iotaBreaker
import DataManipulationUtils as dmu 
import random

b = 200

def partRND(mat, roundIndex, verbose = False):
    # Ap = theta.theta(mat)    

    # Sp = dmu.convertMatrixToList(Ap,b)
    # print("result of theta: ", dmu.formatBitsAsByteSplitHexString(Sp, " "))
    
    Ap = ro.ro(mat)
    
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

def undoPartRND(mat, roundIndex, verbose = False):
    # Ap = theta.theta(mat)    

    # Sp = dmu.convertMatrixToList(Ap,b)
    # print("result of theta: ", dmu.formatBitsAsByteSplitHexString(Sp, " "))
    
    Ap = iotaBreaker.iotaBreaker(mat,roundIndex)
    Ap = chiBreaker.chiBreaker(Ap)
    Ap = piBreaker.piBreaker(Ap)
    Ap = rhoBreaker.rhoBreaker(Ap)
    
   

    return Ap

def test():

    ir = random.randint(0,24)
    
    plainTextBin = dmu.generateRandomList(b)
    planTextHex = dmu.formatBitsAsByteSplitHexString(plainTextBin, "")

    print("b = ",b, "ir = ", ir)
    print("Input to partRND:", planTextHex)

    A = dmu.convertListToStateMatrix(plainTextBin)

    Ap = partRND(A,ir)
    
    binOutput = dmu.convertMatrixToList(Ap, b)
    hexOutput = dmu.formatBitsAsByteSplitHexString(binOutput, "")
    
    print("Output of partRND: ", hexOutput)

    RecoveredMatrix = undoPartRND(Ap, ir)
    
    binOutput2 = dmu.convertMatrixToList(RecoveredMatrix, b)
    hexOutput2 = dmu.formatBitsAsByteSplitHexString(binOutput2, "")
    
    print("Output of undoPartRND function: ", hexOutput2)

    if(hexOutput2 == planTextHex):
        print("Successful recovery")
    else:

        print("Fail!")
        exit()

#One of the main issues with reversing SHA/Keccak is that the digest we get is a tuncated version of the state, so we really only know 80/200 bits :/
#Maybe collision will be easier ?


test()
