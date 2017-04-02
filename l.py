import copy
import matrixUtils as mu
import numpy as np
import rc 
x_len = 5
y_len = 5



"""
"The effect of ι is to modify some of the bits of Lane (0, 0) in a manner that depends on the round
index i r . The other 24 lanes are not affected by ι."
"""
def l(mat, ir):
    matp = copy.deepcopy(mat)
    w = len(mat[0][0])
    l_var = int(np.log2(w))
    RC = np.zeros(w)

    for j in range(0, l_var):
        RC[(2^j) - 1] = rc.rc(j + 7*ir)

    for z in range(w):
        matp[0][0][z] = matp[0][0][z] ^ int(RC[z])
    
    return matp


#*******************************************************************#
#Test Functions
w_test = 4
def test():
    print("start test...")
    A = [[[0 for k in range(w_test)] for k in range(y_len)] 
    for k in range(x_len)]
    l_var = int(np.log2(w_test))
    
    print("l is ", l_var)

    mu.populate(A)
    roundIndex = 10

    Ap = l(A, roundIndex)

    print("    After l (A')   | Before l (A)")
    mu.matPrint(Ap, 'l', True, True, A)                

# test()