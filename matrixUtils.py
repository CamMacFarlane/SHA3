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

# def printColoumns(mat, label):
#     for x in range(x_len):
#         for z in range(z_len):
#             print()
#             if label == True:
#                 print("X =", x , "Z =", z, " : ", end="")
#             for y in range(y_len):            
#                 print(mat[x][y][z])
#     print()    

# def printCompColoumns(mat, mat2, label):
#     for x in range(x_len):
#         for z in range(z_len):
#             print()
#             if label == True:
#                 print("X =", x , "Z =", z)
#             for y in range(y_len):            
#                 print(mat[x][y][z], " | " ,mat2[x][y][z])
#     print()   


'''
Prints a matrix by row, coloumnd or lane

variables: 
    mat = the matrix to print
    format = r, c, or l to prints rows, coloumns or lanes respectively
    comp = boolean states whether to compare matrix mat with another matrix supplied as the final argument
    lable = boolean states whether or not to lable to output
    *args = where the comparison matix is supplied 
'''
def matPrint(mat, format, comp, label, *args):
    if(z_len == 0):
        print("ERROR: You must set the z length using matrixUtils.setZLen()")
        return 

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
    