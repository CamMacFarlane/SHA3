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
def generateA(w):

    for x in range(x_len):
        for y in range(y_len):
            for z in range(z_len):
                A[x][y][z] = randint(0, 1)


# coloumn parity
def C(mat, x, z):

    ret = mat[x][0][z]
    for y in range(1, y_len):
        ret = ret ^ mat[x][y][z]
    return ret

# collapsing function
def D(mat, x, z):
    return (C(mat, (x-1) % 5, z) ^ C(mat, (x+1) % 5, (z-1) % z_len))


#Theta function, performs theta function on matrix mat with dimensions x_len, y_len, z_len
def theta(mat):
    matp = copy.deepcopy(mat)
    for x in range(x_len):
        for y in range(y_len):
            for z in range(z_len):
                matp[x][y][z] = matp[x][y][z] ^ D(mat, x,z)
                
    return matp



mu.setZLen(w)

generateA(w)

Ap = theta(A)   

mu.matPrint(Ap, 'c', True, True, A)

