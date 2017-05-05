import copy
import matrixUtils as mu

x_len = 5
y_len = 5


#shifts lanes by offset
def ro(mat):
    matp = copy.deepcopy(mat)
    z = 0
    y = 0
    x = 1
    w = len(mat[0][0])
    #for t = 0 to t = 23
    for t in range(0,24):
        for z in range(0,w):
            offset = ((t+1)*(t+2)/2)
            offset = int(offset)
            matp[x][y][z] = mat[x][y][(z - offset)%w]
        swap = y
        y = (2*x + 3*y)%y_len 
        x = swap
    

    return matp

#*******************************************************************#
#Test functions

z_len = 4
def test():
    A = [[[0 for k in range(z_len)] for k in range(y_len)]
         for k in range(x_len)]

    mu.populate(A)

    Ap = ro(A)
    print("           After Ro | Before Ro")
    mu.matPrint(Ap, 'l', True, True, A)
