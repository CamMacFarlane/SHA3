import copy
import matrixUtils as mu
# import chiBreaker
import DataManipulationUtils as dmu
x_len = 5
y_len = 5

def chi(mat):
    matp = copy.deepcopy(mat)
    w = len(mat[0][0])
    for x in range(x_len):
        for y in range(y_len):
            for z in range(w):
                matp[x][y][z] = ((mat[x][y][z]) ^ ((mat[(x+1)%5][y][z] ^ 1) & mat[(x+2)%5][y][z]))
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
def testChi(row):
    rowp = row
    for i in range(5):
        rowp[i] = (row[i] ^ ((row[(i+1)%5] ^ 1) & row[(i+2)%5]))
    # print(rowp)
    return(rowp)



testRow = [1,0,0,0,1]

def test2():
    count = 0
    for i in range(2**5):
        row = bin(i)[2:]
        row = row.zfill(5)
        row = list(row)

        for j in range(5):
            row[j] = int(row[j])
        print(i, row, "\n")
        row = testChi(row)
        # print(" ->", (row))
        # binStr = dmu.convertListToString(row)
        # newBinStr =  chiBreaker.reverseChiRow(binStr)
        # newrow = list(newBinStr)
        # print(" ->", newBinStr)
        
# tesot2()
# testChi(testRow)






