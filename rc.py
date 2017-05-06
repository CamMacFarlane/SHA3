import time
def rc(t):
    n = t%255
    if(n == 0):
        return 1
    R = [1,0,0,0,0,0,0,0]
    for i in range (1,(n+1)):
        R = [0] + R          # R = 0||R
        R[0] = R[0]^R[8]
        R[4] = R[4]^R[8]
        R[5] = R[5]^R[8]
        R[6] = R[6]^R[8]

        R = R[:8] #np.delete(R,8)
        # print(len(R))
        # print(R)
    return R[0]
    
#*******************************************************************#
#Test functions
def test():
    for i in range(0,255):
        print(rc(i))
        time.sleep(1)
# test()