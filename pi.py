import copy
import matrixUtils as mu

w = 4
x_len = 5
y_len = 5
z_len = w

def pi(mat):
    x_len = len(mat)
    y_len = len(mat[0])
    z_len = len(mat[0][0])
    matp = copy.deepcopy(mat)
    for x in range(x_len):
        for y in range(y_len):
            for z in range(z_len):
                matp[x][y][z] = mat[(x + 3*y)%x_len][x][z]
    return matp

A = [[[0 for k in range(z_len)] for k in range(y_len)]
     for k in range(x_len)]

mu.populate(A)

Ap = pi(A)

mu.printSheet(Ap, A)
#mu.matPrint(Ap, 'r', True, True, A )