import DataManipulationUtils as dmu
import copy
import chi
import matrixUtils as mu
def reverseChiRow(row):
    return {
        "00000" : "00000",
        "00001" : "10101",
        "00010" : "01011",
        "00011" : "01010",#
        "00100" : "10110", #
        "00101" : "00001",
        "00110" : "10100",#
        "00111" : "10111",
        "01000" : "01101",
        "01001" : "01000",
        "01010" : "00010", #
        "01011" : "00011", #
        "01100" : "01001",
        "01101" : "01100",
        "01110" : "01111",
        "01111" : "01110",
        "10000" : "11010",
        "10001" : "00101",
        "10010" : "10000",
        "10011" : "11011",
        "10100" : "00100",
        "10101" : "10001",
        "10110" : "00110",
        "10111" : "00111",
        "11000" : "10010",
        "11001" : "11101",
        "11010" : "11000",
        "11011" : "10011",
        "11100" : "11110",
        "11101" : "11001",
        "11110" : "11100",
        "11111" : "11111",
    }[row]
def quicktest():
    for i in range(32):
        binary = str(format(i,'b').zfill(5))
        result = reverseChiRow(binary)
        intResult = int(result, 2)
        print(i, binary, result, intResult)

def chiBreaker(mat):
    matp = copy.deepcopy(mat)
    w = len(mat[0][0])
    count = 0
    for y in range(5):
        for z in range(w):
            row = []
            for x in range(5):
                row = row + [mat[x][y][z]]

            binStr = dmu.convertListToString(row)
            newBinStr =  reverseChiRow(binStr)
            # print(newBinStr)
            newrow = list(newBinStr)
            # print(newrow)
            # count = count + 1
            for x in range(5):
                matp[x][y][z] = int(newrow[x])
    # print(count)
    return matp


# def test():
    


b = 200

def test2():
    hexInput = "e4a27d38b34a69506fb76e52e09f11d73edbec15c31e51690f"    
    
    binaryList = dmu.fromHexToBits(hexInput)
    A = dmu.convertListToStateMatrix(binaryList)

    #preimage 
    Ap = chiBreaker(A)
    binOutput = dmu.convertMatrixToList(Ap, b)
    hexOutput = dmu.formatBitsAsByteSplitHexString(binOutput, "")
    
    realPreimageHex = "b8a2fc30b1ca4ec027b3ce43e05110171acaee1d82b643e93b"
    binaryList = dmu.fromHexToBits(realPreimageHex)
    realPreimage = dmu.convertListToStateMatrix(binaryList)
    
    # print(App == A)    
    if (hexOutput == realPreimageHex):
       print("Derived preimage matches given preimage") 
    print("preimage attempt:", hexOutput)
    # mu.matPrint(Ap, 'r', True, True, realPreimage)                

# test2()
# quicktest()