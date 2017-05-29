import chi
import matrixUtils as mu
import DataManipulationUtils as dmu

fileName = "output/chi"
numDataPoints = 10
b = 200

CSVBytetarget = open(fileName + "_byteWise" +"_with_b_" + str(b) + "_dataPoints_" + str(numDataPoints) + ".csv", 'w')
CSVtarget = open(fileName  +"_with_b_" + str(b) + "_dataPoints_" + str(numDataPoints) + ".csv", 'w')

TXTBytetarget = open(fileName + "_byteWise"  +"_with_b_" + str(b) + "_dataPoints_" + str(numDataPoints) + ".txt", 'w')
TXTtarget = open(fileName  +"_with_b_" + str(b) + "_dataPoints_" + str(numDataPoints) + ".txt", 'w')

# headerString = "Theta Data generation, b = "+ str(b) + "Generating " +  str(numDataPoints) + " data points" + "\nINPUT                                                     OUTPUT"
# CSVtarget.write(headerString + "\n")
# TXTtarget.write(headerString + "\n")
# print("        INPUT                                                                             OUTPUT")

for i in range(numDataPoints):
    binaryInput = dmu.generateRandomList(b)
    
    hexInputTxt = dmu.formatBitsAsByteSplitHexString(binaryInput, "")
    hexInputTxtByte = dmu.formatBitsAsByteSplitHexString(binaryInput, " ")
    
    hexInputCSV = dmu.formatBitsAsByteSplitHexString(binaryInput, "")
    hexInputCSVByte = dmu.formatBitsAsByteSplitHexString(binaryInput, ",")
    
    A = dmu.convertListToStateMatrix(binaryInput)
    Ap = chi.chi(A)
    
    binOutput = dmu.convertMatrixToList(Ap, b)
    hexOutputTxt = dmu.formatBitsAsByteSplitHexString(binOutput, "")
    hexOutputTxtByte = dmu.formatBitsAsByteSplitHexString(binOutput, " ")
    
    hexOutputCSV = dmu.formatBitsAsByteSplitHexString(binOutput, "")
    hexOutputCSVByte = dmu.formatBitsAsByteSplitHexString(binOutput, ",")
    
    CSVtarget.write(hexInputCSV + "  ," + hexOutputCSV + "\n")
    TXTtarget.write(hexInputTxt + "  " + hexOutputTxt + "\n")

    CSVBytetarget.write(hexInputCSVByte + ",  ," + hexOutputCSVByte + "\n")
    TXTBytetarget.write(hexInputTxtByte + "  " + hexOutputTxtByte + "\n")
    print((i*100)//numDataPoints,"% \r", end="")