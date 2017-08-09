import copy
import matrixUtils as mu
from random import randint
import DataManipulationUtils as dmu
x_len = 5
y_len = 5

# coloumn parity
def C(mat, x, z):

    ret = mat[x][0][z]
    for y in range(1, y_len):
        ret = ret ^ mat[x][y][z]
    return ret

# collapsing function
def D(mat, x, z):
    w = len(mat[0][0])
    return (C(mat, (x-1) % x_len, z) ^ C(mat, (x+1) % x_len, (z-1) % w))


#Theta function, performs theta function on matrix mat 
def theta(mat):
    matp = copy.deepcopy(mat)
    w = len(mat[0][0])
    for x in range(x_len):
        for y in range(y_len):
            for z in range(w):
                matp[x][y][z] = matp[x][y][z] ^ D(mat, x,z)
                
    return matp

#*******************************************************************#
#Test functions
test_w = 4

# test()
def randomlyPopulatePlane(plane):
    for x in range(len(plane)):
        for z in range(len(plane[0])):
            plane[x][z] = randint(0, 1)


#Prints a labled plane
def printPlane(plane):
    for x in range(len(plane)):
        print(x, " ", end="")
    print("X/Z\n")
    for z in range(len(plane[0])-1, -1 ,-1):
        for x in range(len(plane)):
            print(plane[x][z] , " ", end="")
        print(" ",z)
    print()
        # print()

#perform D function
def performD(plane):
    planeP = copy.deepcopy(plane)
    x_len = len(plane)
    w = len(plane[0])
    
    for x in range(len(plane)):
        for z in range(len(plane[0])):
            planeP[x][z] = plane[(x-1)%(x_len)][z] ^ plane[(x+1)%(x_len)][(z-1)%w] 
        
    return planeP

#Fills a row with a binary number given as an int i
#Example, given a row = [x,x,x,x,x] and i = 3 it will change the row to be [0,0,0,1,1]
def fillRowWithBinaryNumber(row, i ):
    candidate_first_row = str(format(i,'b').zfill(x_len))
    candidate_first_row = list(candidate_first_row)
    for j in range(len(row)):
        row[j] = int(candidate_first_row[j])

#Replaces a row at rownum in a plane
def replaceRow(plane, rowNum, row):
    for i in range(len(row)):
        plane[i][rowNum] = row[i]

#Gets a row at rownum from a plane
def getRow(plane,rowNum):
    row = [0,0,0,0,0]
    for i in range(len(row)):
        row[i] = plane[i][rowNum]
    return row

#Checks to see if the candidate is valid, returns true if candidate is valid
def checkIfCandidateIsValid(candidate, c_prime):
    testDPlane = performD(candidate)
    validCandidate = True
    for x in range(len(candidate)):
        for z in range(len(candidate[0])):
            if(c_prime[x][z] != (testDPlane[x][z] ^ candidate[x][z])):
                validCandidate = False
    # if(validCandidate == True):
        # print("Candidate!")
    return validCandidate

#Generates the plane C that prduced the given C' plane
#If it's possible that more than one C plane produced C' then will return -1
def generateCPlaneFromCPrime(c_prime):
    x_len = 5
    w = len(c_prime[0])
    last_index = w - 1
    ret = False
    numCandidates = 0
    #Iterating thru all possible first row combinations for D
    final_C_candidate = [[0 for k in range(w)] for k in range(x_len)]
    for i in range(32):
        # print("Start \n\n")
        D_candidate = [[0 for k in range(w)] for k in range(x_len)]
        C_candidate = [[0 for k in range(w)] for k in range(x_len)]
        D_first_row_candidate = [0,0,0,0,0]
        
        #Create test D
        fillRowWithBinaryNumber(D_first_row_candidate, i)
        replaceRow(D_candidate, last_index, D_first_row_candidate)

        
        for k in range(5):
            C_candidate[k][last_index] = c_prime[k][last_index]^D_candidate[k][last_index]

        
        for j in range(last_index-1,-1,-1):
            for k in range(5):
                C_candidate[k][j] = C_candidate[(k-2)%5][j+1] ^ D_candidate[(k-1)%5][j+1]
            for k in range(5):
                D_candidate[k][j] = C_candidate[k][j] ^ c_prime[k][j] 
    
        if(checkIfCandidateIsValid(C_candidate, c_prime)):
            numCandidates = numCandidates + 1
            final_C_candidate = C_candidate
            # exit()
                            
        if(numCandidates > 1):
            print("more than one candidate!")
            return -1

    return final_C_candidate 

#XORs a plane with each plane in a state matrix mat
def xOrPlaneWithMatrix(mat,plane):
    w = len(mat[0][0])

    x_len = y_len = 5
    newMatrix = [[[0 for k in range(w)] for k in range(y_len)]
         for k in range(x_len)]

    for x in range(x_len):
        for y in range(y_len):
            for z in range(w):
                newMatrix[x][y][z] = mat[x][y][z] ^ plane[x][z]
    return newMatrix

#Inverts a state matrix A' to A, returns -1 if there are more than 1 C candidates (collision)
def thetaInverse(mat):
    matp = copy.deepcopy(mat)
    w = len(mat[0][0])
    
    planep = [[0 for k in range(w)] for k in range(x_len)]
    recoveredPlane = [[0 for k in range(w)] for k in range(x_len)]
    diffPlane = [[0 for k in range(w)] for k in range(x_len)]

    for x in range(5):
        for z in range(w):
            planep[x][z] = C(matp, x,z)
    

    recoveredPlane = generateCPlaneFromCPrime(planep)
    if(recoveredPlane == -1):
        return -1
    for x in range(5):
        for z in range(w):
            diffPlane[x][z] = recoveredPlane[x][z] ^ planep[x][z]
    
    preImage = xOrPlaneWithMatrix(matp, diffPlane)
    

    return preImage
    
def test():
    b = 200
    binaryList = dmu.generateRandomList(b)    
    hexInputTxt = dmu.formatBitsAsByteSplitHexString(binaryList, "")
    print("A   = ",hexInputTxt)

    A = dmu.convertListToStateMatrix(binaryList)
    w = len(A[0][0])

    Ap = theta(A)

    binOutput1 = dmu.convertMatrixToList(Ap, b)
    hexOutput1 = dmu.formatBitsAsByteSplitHexString(binOutput1, "")
    print("A'  = ",hexOutput1)
    App = thetaInverse(Ap)
    if(App == -1):
        print("TWO C candidates!")
        print("INPUT to theta was: ",hexInput)
        print("INPUT to thetaInverse was: ", hexOutput1)
        exit()
    binOutput2 = dmu.convertMatrixToList(App, b)
    hexOutput2 = dmu.formatBitsAsByteSplitHexString(binOutput2, "")
    print("A'' = ",hexOutput2)
# test()