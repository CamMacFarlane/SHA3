import copy
import matrixUtils as mu
import numpy as np
import rc 
import DataManipulationUtils as dmu
import iota
x_len = 5
y_len = 5



"""
"The effect of ι is to modify some of the bits of Lane (0, 0) in a manner that depends on the round
index i r . The other 24 lanes are not affected by ι."
"""
def iotaInverse(mat, ir):
    matp = copy.deepcopy(mat)
    w = len(mat[0][0])
    l_var = int(np.log2(w))
    RC = [0]*w
    
    for j in range(0, (l_var + 1)):
        RC[(2**j) - 1] = rc.rc(j + 7*ir)
    
    # RCR = RC[::-1]
    # print("for round ", ir, "RCtruncw = ", RC[:w])
    for z in range(0,w):
        matp[0][0][z] = matp[0][0][z] ^ int(RC[z])
    
    return matp


def test():
    b = 200

    
    ir = 2
    binaryList = dmu.generateRandomList(200)
    hexInput = dmu.formatBitsAsByteSplitHexString(binaryList, "")
    
    print("ir = ", ir)
    print("Input to Iota:", hexInput)
    
    # binaryList = dmu.fromHexToBits(hexInput)
    A = dmu.convertListToStateMatrix(binaryList)
    Ap = iota.iota(A, ir)
    binOutput = dmu.convertMatrixToList(Ap, b)
    hexOutput = dmu.formatBitsAsByteSplitHexString(binOutput, "")

    print("Output of 1 round of Iota:", hexOutput)
    
    App = iota.iota(Ap,ir) 
    # iotaInverse(A, ir)
    binOutput = dmu.convertMatrixToList(App, b)
    hexOutput = dmu.formatBitsAsByteSplitHexString(binOutput, "")
    
    print("Output of second round of Iota:",hexOutput)

# test()