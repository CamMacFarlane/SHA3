import SHA3Examples as bb
import matrixUtils as mu
import DataManipulationUtils as dmu
import random
import pad
fileName = "output/Sponge"
numDataPoints = 10000
b = 200

CSVBytetarget = open(fileName + "_byteWise" +"_with_b_" + str(b) + "_dataPoints_" + str(numDataPoints) + ".csv", 'w')
CSVtarget = open(fileName  +"_with_b_" + str(b) + "_dataPoints_" + str(numDataPoints) + ".csv", 'w')

TXTBytetarget = open(fileName + "_byteWise"  +"_with_b_" + str(b) + "_dataPoints_" + str(numDataPoints) + ".txt", 'w')
TXTtarget = open(fileName  +"_with_b_" + str(b) + "_dataPoints_" + str(numDataPoints) + ".txt", 'w')

# headerString = "Theta Data generation, b = "+ str(b) + "Generating " +  str(numDataPoints) + " data points" + "\nINPUT                                                     OUTPUT"
# CSVtarget.write(headerString + "\n")
# TXTtarget.write(headerString + "\n")
# print("        INPUT                                                                             OUTPUT")
r = 40
for i in range(numDataPoints):
    messageLength = random.randint(1,(r-3))
    
    binaryInput = dmu.generateRandomList(messageLength)
    
    binaryInput = binaryInput + pad.pad(r,messageLength)
    
    # print(binaryInput, len(binaryInput), messageLength)
    # exit()

    hexInputTxt = dmu.formatBitsAsByteSplitHexString(binaryInput, "")
    hexInputTxtByte = dmu.formatBitsAsByteSplitHexString(binaryInput, " ")
    
    hexInputCSV = dmu.formatBitsAsByteSplitHexString(binaryInput, "")
    hexInputCSVByte = dmu.formatBitsAsByteSplitHexString(binaryInput, ",")
    
    # A = dmu.convertListToStateMatrix(binaryInput)
    binOutput = bb.keccackRCNRM(40,160,2,binaryInput)
    
    # binOutput = dmu.convertMatrixToList(Ap, b)
    hexOutputTxt = dmu.formatBitsAsByteSplitHexString(binOutput, "")
    hexOutputTxtByte = dmu.formatBitsAsByteSplitHexString(binOutput, " ")
    
    hexOutputCSV = dmu.formatBitsAsByteSplitHexString(binOutput, "")
    hexOutputCSVByte = dmu.formatBitsAsByteSplitHexString(binOutput, ",")
    
    CSVtarget.write(hexInputCSV + "  ," + hexOutputCSV + "\n")
    TXTtarget.write(hexInputTxt + "  " + hexOutputTxt + "\n")

    CSVBytetarget.write(hexInputCSVByte + ",  ," + hexOutputCSVByte + "\n")
    TXTBytetarget.write(hexInputTxtByte + "  " + hexOutputTxtByte + "\n")
    print((i*100)//numDataPoints,"% \r", end="")