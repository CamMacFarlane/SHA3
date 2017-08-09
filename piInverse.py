import copy
import matrixUtils as mu
import DataManipulationUtils as dmu
import pi

x_len = 5
y_len = 5

def piInverse(mat):
    x_len = len(mat)
    y_len = len(mat[0])
    z_len = len(mat[0][0])
    matp = copy.deepcopy(mat)
    for x in range(x_len):
        for y in range(y_len):
            for z in range(z_len):
                matp[(x + 3*y)%x_len][x][z] = mat[x][y][z] 
                # print(x,y,z, "<-", ((x + 3*y)%x_len), x, z )
    return matp

b = 200
def test():
    hexInput = input()    
    
    binaryList = dmu.fromHexToBits(hexInput)
    A = dmu.convertListToStateMatrix(binaryList)
    
    Ap = piInverse(A)

    binOutput = dmu.convertMatrixToList(Ap, b)
    hexOutput = dmu.formatBitsAsByteSplitHexString(binOutput, "")
    
    print(hexOutput)


def test2():
    binaryList = dmu.generateRandomList(b)
    hexInput = dmu.formatBitsAsByteSplitHexString(binaryList, "")
    print("A = ", hexInput)
    A = dmu.convertListToStateMatrix(binaryList)
    Ap = pi.pi(A)
    binOutput = dmu.convertMatrixToList(Ap, b)
    hexOutput = dmu.formatBitsAsByteSplitHexString(binOutput, "")

    print("A':", hexOutput)
    App = piInverse(Ap) 
    # iotaInverse(A, ir)
    binOutput = dmu.convertMatrixToList(App, b)
    hexOutput = dmu.formatBitsAsByteSplitHexString(binOutput, "")
    
    print("A'':",hexOutput)
# test2()