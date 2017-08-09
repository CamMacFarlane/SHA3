from random import randint
import copy
import DataManipulationUtils as dmu 

x_len = 5
y_len = 5
z_len = 0

def printRows(mat, label):
    for y in range(y_len):
        for z in range(z_len):
            print()
            if label == True:
                print("Y =", y , "Z =", z)
            for x in range(x_len):
                print(mat[x][y][z], end="")    
    print()

def printCompRows(mat, mat2, label):
    for y in range(y_len):
        for z in range(z_len):
            print()
            if label == True:
                print("Y =", y , "Z =", z, " : ", end="")
            for x in range(x_len):
                print(mat[x][y][z], end="")
            print(" | ", end="")
            for x in range(x_len):
                print(mat2[x][y][z], end="")    
    print()

 
def printColoumns(mat, label):
    for x in range(x_len):
        for z in range(z_len):            
            print()
            if label == True:
                print("X =", x , "Z =", z , " : ", end="")
            for y in range(y_len):
                print(mat[x][y][z], end="")
    print()    

def printCompColoumns(mat,mat2, label):
    for x in range(x_len):
        for z in range(z_len):            
            print()
            if label == True:
                print("X =", x , "Z =", z , " : ", end="")
            for y in range(y_len):
                print(mat[x][y][z], end="")
            print(" | ", end="")
            for y in range(y_len):
                print(mat2[x][y][z], end="")
    print()    

def printLanes(mat, label):
    for x in range(x_len):
        for y in range(y_len):            
            print()
            if label == True:
                print("X =", x , "Y =", y , " : ", end="")
            for z in range(z_len):
                print(mat[x][y][z], end="")
    print()    

def printLanesHex(mat, label):
    binstr = []
    x_len = 5
    y_len = 5
    z_len = len(mat[0][0])
    for x in range(x_len):
        for y in range(y_len):            
            print()
            if label == True:
                print("X =", x , "Y =", y , " : ", end="")
            for z in range(z_len):
                # print(mat[x][y][z], end="")
                binstr = binstr + [mat[x][y][z]]
            print(binstr, end="")
            print(dmu.formatsBitsAsHexString(binstr), end="")
            binstr = []

    print()    

def printCompLanes(mat,mat2, label):
    for x in range(x_len):
        for y in range(y_len):            
            print()
            if label == True:
                print("X =", x , "Y =", y , " : ", end="")
            for z in range(z_len):
                print(mat[x][y][z], end="")
            print(" | ", end="")
            for z in range(z_len):
                print(mat2[x][y][z], end="")
    print()    

def printSheet(mat, mat2, matName, mat2Name):
    for z in range(z_len):
        print("Sheet Z = ", z, "\n")
        print(matName)     
        for y in range(y_len):
            for x in range(x_len):
                print(mat[x][y][z] , " ", end="")
            print()        
        print("\n---------------")
        print(mat2Name)
        for y in range(y_len):
            for x in range(x_len):
                print(mat2[x][y][z] , " ", end="")
            print()
        print("\n")

'''
Prints a matrix by row, coloumnd or lane

variables: 
    mat = the matrix to print
    format = r, c, or l to prints rows, coloumns or lanes respectively
    comp = boolean states whether to compare matrix mat with another matrix supplied as the final argument
    lable = boolean states whether or not to lable to output
    *args = where the comparison matix is supplied 
'''
def xtoFIPS(x):
    return{
       0:2,
       1:3,
       2:4,
       3:0,
       4:1,
    }.get(x, "ERROR")

def ytoFIPS(y):
    return{
       0:2,
       1:1,
       2:0,
       3:4,
       4:3,
    }.get(y, "ERROR")

def matToFIPS(mat):
    matp = copy.deepcopy(mat)

    for x in range(len(mat)):
        for y in range(len(mat[0])):
            for z in range(len(mat[0][0])):
                matp[xtoFIPS(x)][ytoFIPS(y)][z] = mat[x][y][z]
                # print(x,y,z, "->", xtoFIPS(x),ytoFIPS(y),z )
    return matp

def matPrint(mat, format, comp, label, *args):
    global z_len
    if(z_len == 0):
        z_len = len(mat[0][0])
        # print (z_len)
        # exit()
        # print("ERROR: You must set the z length using matrixUtils.setZLen()")
        # return 

    if comp and len(args) > 0 and  type(args[0] == type(mat)):
        mat2 = args[0]
    elif comp:
        print("For comparisons argument 3 must be of the same type as argument 1")
        return

    if format == "r":
        if comp:
            printCompRows(mat, mat2, label)
        else:
            printRows(mat, label)
    
    if format == "c":
        if comp:
            printCompColoumns(mat, mat2, label)
        else:
            printColoumns(mat, label)
            
    if format == "l":
        if comp:
            printCompLanes(mat, mat2, label)
        else:
            printLanes(mat, label)
            
def setZLen(z):
    global z_len
    z_len = z
    
def populate(mat):
    global z_len
    z_len = len(mat[0][0])
    
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            for z in range(len(mat[0][0])):
                mat[x][y][z] = randint(0, 1)

def populateTemp(mat):
    global z_len
    z_len = len(mat[0][0])
    
    for x in range(len(mat)):
        for y in range(len(mat[0])):
            for z in range(len(mat[0][0])):
                mat[x][y][z] = randint(10,99)
    