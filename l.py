import copy
import matrixUtils as mu
import numpy as np
import rc 
w = 4
x_len = 5
y_len = 5
z_len = w


l_var = int(np.log2(w))

def l(mat, ir):
    matp = copy.deepcopy(mat)
    RC = np.zeros(w)

    for j in range(0, l_var):
        RC[(2^j) - 1] = rc.rc(j + 7*ir)

    for z in range(z_len):
        matp[0][0][z] = matp[0][0][z] ^ int(RC[z])
    
    return matp

def test():
    print("start test...")
    A = [[[0 for k in range(z_len)] for k in range(y_len)] 
    for k in range(x_len)]
    print("l is ", l_var)

    mu.populate(A)
    roundIndex = 10

    Ap = l(A, roundIndex)

    print("    After l (A')   | Before l (A)")
    mu.matPrint(Ap, 'l', True, True, A)                

# test()