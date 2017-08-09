import time
import DataManipulationUtils as dmu
def rc(t):
    n = t%255
    if(n == 0):
        return 1
    R = [1,0,0,0,0,0,0,0]
    for i in range (1,(n+1)):
        R = [0] + R 
        R[0] = R[0]^R[8]
        R[4] = R[4]^R[8]
        R[5] = R[5]^R[8]
        R[6] = R[6]^R[8]

        R = R[:8] 

    return R[0]
    
#*******************************************************************#
#Test functions
def test():
    for i in range(0,24):
        print(rc(i))
        time.sleep(1)

def test2():
    RC = [0]*64
    for i in range(0,24):
        for j in range(0, (6 + 1)):
            RC[(2**j) - 1] = rc(j + 7*i)
            hexs = dmu.formatBitsAsByteSplitHexString(RC,"")
        print(hexs)
        # print(RC)

    # For j from 0 to l, let RC[2 j – 1] = rc(j + 7i r ).
# test2()