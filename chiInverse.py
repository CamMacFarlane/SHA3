import DataManipulationUtils as dmu
import copy
import chi
import matrixUtils as mu

#Look up tabke for chi rows
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

def quicktest2():
    for i in range(32):
        row = [0]*5
        binary1 = (format(i,'05b').zfill(5))
        binary2 = str(format(i,'b').zfill(5))
        for j in range(5):
            row[j] = int(binary1[j])
        result1 = SamerReverseRow2(row)
        result2 = reverseChiRow(binary2)

        intResult1 = int(dmu.convertListToString(result1), 2)
        intResult2 = int(result2, 2)
        if(intResult1 != intResult2):
            print("fail")
            print(binary1, "Samer:", result1, "Expected:", result2)
            exit()
        print(binary1, "Samer:", result1, "Expected:", result2)
        
    print("SUCCESS")



def chiInverse(mat):
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


#Binary logic method
def SamerReverseRow2(row):
    x_len = len(row)
    newRow = [0]*x_len
    
    for i in range(x_len):
        x0 = row[i]
        x1 = row[(i+1)%x_len]
        x2 = row[(i+2)%x_len]
        x3 = row[(i+3)%x_len]
        x4 = row[(i+4)%x_len]
        newRow[i] = x0&x1 | (x1^1)&(x3^1)&(x4)&((x0^1)&(x2^1) | (x0&x2)) | ((x1^1)&x3)&(x0^x2) | ((x1^1)&(x4^1))&(x0^x2)
    return newRow
    


b = 200

def test2():
    hexInput = "e4a27d38b34a69506fb76e52e09f11d73edbec15c31e51690f"    
    
    binaryList = dmu.fromHexToBits(hexInput)
    A = dmu.convertListToStateMatrix(binaryList)

    #preimage 
    Ap = chiInverse(A)
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

def test():
    binaryInput = dmu.generateRandomList(b)    
    hexInputTxt = dmu.formatBitsAsByteSplitHexString(binaryInput, "")
    print("input to chi: ", hexInputTxt)
    # print(binaryInput)
    A = dmu.convertListToStateMatrix(binaryInput)
    Ap = chi.chi(A)
    binOutput = dmu.convertMatrixToList(Ap, b)
    hexOutputTxt = dmu.formatBitsAsByteSplitHexString(binOutput, "")
    print("Output from chi: ", hexOutputTxt)
    # print(binOutput)
    App = chiInverse(Ap)
    binOutput2 = dmu.convertMatrixToList(App, b)
    hexOutput2 = dmu.formatBitsAsByteSplitHexString(binOutput2, "")
    # print(binOutput2)
    print("Output from ChiInverse: ", hexOutput2)
    if(hexOutput2 == hexInputTxt):
        print("SUCCESS")
# test()
# quicktest2()