import copy
import matrixUtils as mu
import DataManipulationUtils as dmu
import ro
x_len = 5
y_len = 5


#shifts lanes by offset
def rhoInverse(mat):
    matp = copy.deepcopy(mat)
    z = 0
    y = 0
    x = 1
    w = len(mat[0][0])
    #for t = 0 to t = 23
    for t in range(0,24):
        for z in range(0,w):
            offset = ((t+1)*(t+2)/2)
            offset = int(offset)
            matp[x][y][(z - offset)%w] = mat[x][y][z]
        swap = y
        y = (2*x + 3*y)%y_len 
        x = swap
    

    return matp

#*******************************************************************#
#Test functions
b = 200

#Test that takes input
def test():
    print("b must be set in the script! b is ", b)
    print("input to rho (hex): ",end="")
    hexInput = input()    
    
    binaryList = dmu.fromHexToBits(hexInput)
    A = dmu.convertListToStateMatrix(binaryList)
    Ap = rhoInverse(A)

    binOutput = dmu.convertMatrixToList(Ap, b)
    hexOutput = dmu.formatBitsAsByteSplitHexString(binOutput, "")
    
    print(hexOutput)

#Test that generates input
def test2():
    binaryInput = dmu.generateRandomList(b)    
    hexInputTxt = dmu.formatBitsAsByteSplitHexString(binaryInput, "")
    print("b must be set in the script! b is ", b)
    print("input to rho : ", hexInputTxt)
    print(binaryInput)
    A = dmu.convertListToStateMatrix(binaryInput)
    Ap = ro.ro(A)
    binOutput = dmu.convertMatrixToList(Ap, b)
    hexOutputTxt = dmu.formatBitsAsByteSplitHexString(binOutput, "")
    print("Output from rho: ", hexOutputTxt)
    print(binOutput)
    App = rhoInverse(Ap)
    binOutput2 = dmu.convertMatrixToList(App, b)
    hexOutput2 = dmu.formatBitsAsByteSplitHexString(binOutput2, "")
    print(binOutput2)
    print("Output from roInverse: ", hexOutput2)
    if(hexOutput2 == hexInputTxt):
        print("SUCCESS")


# test()