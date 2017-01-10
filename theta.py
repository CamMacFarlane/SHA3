import pprint
import copy
from random import randint
w = 4
x_len = 5
y_len = 5
z_len = w

A = [[[0 for k in range(z_len)] for k in range(y_len)]
     for k in range(x_len)]


def generateA(w):

    for x in range(x_len):
        for y in range(y_len):
            for z in range(z_len):
                A[x][y][z] = randint(0, 1)


# coloumn parity
def C(x, z):

    ret = A[x][0][z]
    for y in range(1, y_len):
        ret = ret ^ A[x][y][z]
    return ret

# collapsing function
def D(x, z):
    return (C((x-1) % 5, z) ^ C((x+1) % 5, (z-1) % z_len))


def theta():
    Ap = copy.deepcopy(A)
    for x in range(x_len):
        for y in range(y_len):
            for z in range(z_len):
                Ap[x][y][z] = D(x,z)
                
    return Ap

generateA(w)


Ap = theta()
pprint.pprint(A)

pprint.pprint('-------------------')

pprint.pprint(Ap)



