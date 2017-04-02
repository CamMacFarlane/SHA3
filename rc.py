import numpy as np
import time
def rc(t):
    n = t%255
    if(n == 0):
        return 1
    R = np.array([1,0,0,0,0,0,0,0])
    for i in range (1,n):
        R = np.append([0],R)
        R[0] = R[0]^R[8]
        R[4] = R[4]^R[8]
        R[5] = R[5]^R[8]
        R[6] = R[6]^R[8]

        R = np.delete(R,8)
    return R[0]
    
#*******************************************************************#
#Test functions
def test():
    for i in range(0,255):
        print(rc(i))
        time.sleep(1)

