import pprint
import copy
from random import randint
import matrixUtils as mu

w = 4
x_len = 5
y_len = 5
z_len = w

A = [[[0 for k in range(z_len)] for k in range(y_len)]
     for k in range(x_len)]

mu.populate(A)

#shifts lanes by offset
def ro(mat):
    matp = copy.deepcopy(mat)
    z = 0
    y = 0
    x = 1
    global w
    
    #for t = 0 to t = 23
    for t in range(24):
        for z in range(w):
            offset = ((t+1)*(t+2)/2)
            offset = int(offset)
            matp[x][y][z] = mat[x][y][(z - offset)%w]
        swap = y
        y = (2*x + 3*y)%y_len 
        x = swap
        print(x , y, (z - offset) % w)
    

    return matp

Ap = ro(A)
mu.matPrint(Ap, 'l', True, True, A)
        