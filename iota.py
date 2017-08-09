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
def iota(mat, ir):
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


#*******************************************************************#
#Test Functions
def frombits(bits):
    chars = []
    for b in range(int(len(bits) / 8)):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

def printStringAsHex(s):
    for i in range(0,len(s)):
        hexStr = hex(ord(s[i]))
        print(hexStr[2:], end = "")
    print()

w_test = 8
def test():
    print("start test...")
    A = [[[0 for k in range(w_test)] for k in range(y_len)] 
    for k in range(x_len)]
    mu.populate(A)
    l_var = int(np.log2(w_test))
    
    print("l is ", l_var)

    # mu.populate(A)
    maxRoundIndex = 2
    for roundIndex in range(0, maxRoundIndex):
        Ap = iota(A, roundIndex)
        print("    After l (A')   | Before l (A)")
        print(Ap[0][0], A[0][0], "\n")
        # mu.matPrint(Ap, 'l', True, True, A)                


# print(rc.rc(0))


# test()
# def convertListToString(l):
#      string = ''.join(str(i) for i in l)
#      return string

# def test2():
#     RC = [0]*64
#     l_var = 6
#     for ir in range(24):
#         for j in range(0, (l_var + 1)):
#             RC[(2**j) - 1] = rc.rc(j + 7*ir)
        
#         # print("RC[",ir,"] =", RC, )
#         RCR = reversed(RC)
#         string = convertListToString(RCR)
#         # print(string)
#         test = int(string,2)
#         print("RC[",ir,"] =", hex(test))