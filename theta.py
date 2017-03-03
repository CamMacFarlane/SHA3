import copy
import matrixUtils as mu

w = 4
x_len = 5
y_len = 5
z_len = w

# coloumn parity
def C(mat, x, z):

    ret = mat[x][0][z]
    for y in range(1, y_len):
        ret = ret ^ mat[x][y][z]
    return ret

# collapsing function
def D(mat, x, z):
    return (C(mat, (x-1) % x_len, z) ^ C(mat, (x+1) % x_len, (z-1) % z_len))


#Theta function, performs theta function on matrix mat with dimensions x_len, y_len, z_len
def theta(mat):
    matp = copy.deepcopy(mat)
    for x in range(x_len):
        for y in range(y_len):
            for z in range(z_len):
                matp[x][y][z] = matp[x][y][z] ^ D(mat, x,z)
                
    return matp



def test():

    A = [[[0 for k in range(z_len)] for k in range(y_len)]
         for k in range(x_len)]

    mu.populate(A)

    Ap = theta(A) 
    print("    After theta (A') | Before theta (A)")
    mu.matPrint(Ap, 'c', True, True, A)

# test()