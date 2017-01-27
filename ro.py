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

#generates a 5 x 5 x w matrix with random 1's and 0's 
def generate(w):

    for x in range(x_len):
        for y in range(y_len):
            for z in range(z_len):
                A[x][y][z] = randint(0, 1)
    return A
    
#shifts lanes by offset
def ro(mat):
    matp = copy.deepcopy(mat)
    z = 0
    y = 0
    x = 1
    global w
    
    for t in range(24):
        for z in range(w):
            offset = ((t+1)*(t+2)/2)
            offset = int(offset)
            matp[x][y][z] = mat[x][y][(z - offset)%w]
        swap = y
        y = (2*x + 3*y)%5 #ah ha!
        x = swap
        print(x , y, (z - offset) % w)
    

    return matp

A = generate(w)

Ap = ro(A)
mu.matPrint(Ap, 'l', True, True, A)
        