import copy
import matrixUtils as mu

w = 4
x_len = 5
y_len = 5
z_len = w

def chi(mat):
    matp = copy.deepcopy(mat)
    for x in range(x_len):
        for y in range(y_len):
            for z in range(z_len):
                matp[x][y][z] = (mat[x][y][z]) ^ ((mat[(x+1)%5][y][z] ^ 1) & mat[(x+2)%5][y][z] )
    return matp

def test():
    A = [[[0 for k in range(z_len)] for k in range(y_len)]
         for k in range(x_len)]

    print("start")

    mu.populate(A)

    Ap = chi(A)   
    print("    After chi (A')   | Before chi (A)")
    mu.matPrint(Ap, 'r', True, True, A)                

# test()