import copy
import matrixUtils as mu

x_len = 5
y_len = 5

def chi(mat):
    matp = copy.deepcopy(mat)
    w = len(mat[0][0])
    for x in range(x_len):
        for y in range(y_len):
            for z in range(w):
                matp[x][y][z] = (mat[x][y][z]) ^ ((mat[(x+1)%5][y][z] ^ 1) & mat[(x+2)%5][y][z] )
    return matp


#*******************************************************************#
#Test functions
z_len = 4
def test():
    A = [[[0 for k in range(z_len)] for k in range(y_len)]
         for k in range(x_len)]

    print("start")

    mu.populate(A)

    Ap = chi(A)   
    print("    After chi (A')   | Before chi (A)")
    mu.matPrint(Ap, 'r', True, True, A)                

# test()