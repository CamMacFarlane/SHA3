import copy
import matrixUtils as mu

x_len = 5
y_len = 5

def pi(mat):
    x_len = len(mat)
    y_len = len(mat[0])
    z_len = len(mat[0][0])
    matp = copy.deepcopy(mat)
    for x in range(x_len):
        for y in range(y_len):
            for z in range(z_len):
                matp[x][y][z] = mat[(x + 3*y)%x_len][x][z]
                # print(x,y,z, "<-", ((x + 3*y)%x_len), x, z )
    return matp


#*******************************************************************#
#Test functions
z_len = 4
def test():
    A = [[[0 for k in range(z_len)] for k in range(y_len)]
         for k in range(x_len)]

    mu.populate(A)

    Ap = pi(A)

    AFIPS = mu.matToFIPS(A)
    ApFIPS = mu.matToFIPS(Ap)

    print("THESE SHEETS HAVE BEEN REORGANIZED TO MATCH THE INDEXING IN FIGRURE 2 OF THE FIPS SHA3 DOCUMENT")
    mu.printSheet(AFIPS , ApFIPS, "A", "A'")
# test()    
    # uncomment the lines below for easier verificaiton of the pi funtion
    # At = [[[0 for k in range(z_len)] for k in range(y_len)]
    #      for k in range(x_len)]

    # mu.populateTemp(At)
    # Atp = pi(At)
    # AtFIPS = mu.matToFIPS(At)
    # AtpFIPS = mu.matToFIPS(Atp)
    # mu.printSheet(AtFIPS , AtpFIPS, "A", "A'")