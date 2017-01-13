import pprint
import copy
from random import randint
w = 4
x_len = 5
y_len = 5
z_len = w

A = [[[0 for k in range(z_len)] for k in range(y_len)]
     for k in range(x_len)]


def generateA(w):

    for x in range(x_len):
        for y in range(y_len):
            for z in range(z_len):
                A[x][y][z] = randint(0, 1)


# coloumn parity
def C(x, z):

    ret = A[x][0][z]
    for y in range(1, y_len):
        ret = ret ^ A[x][y][z]
    return ret

# collapsing function
def D(x, z):
    return (C((x-1) % 5, z) ^ C((x+1) % 5, (z-1) % z_len))


def theta():
    Ap = copy.deepcopy(A)
    for x in range(x_len):
        for y in range(y_len):
            for z in range(z_len):
                Ap[x][y][z] =Ap[x][y][z] ^ D(x,z)
                
    return Ap



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
                print("Y =", y , "Z =", z)
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
                print("X =", x , "Z =", z)
            for y in range(y_len):            
                print(mat[x][y][z])
    print()    

def printCompColoumns(mat, mat2, label):
    for x in range(x_len):
        for z in range(z_len):
            print()
            if label == True:
                print("X =", x , "Z =", z)
            for y in range(y_len):            
                print(mat[x][y][z], " | " ,mat2[x][y][z])
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

generateA(w)



Ap = theta()
# pprint.pprint(A)

# pprint.pprint('-------------------')

# pprint.pprint(Ap)

#print(printRows(Ap, False))
# print(printColoumns(A, False))
#print(printLanes(Ap, True))
# print(printCompColoumns(A, Ap, False))
# print(printCompLanes(A,Ap, True))


printCompRows(A,Ap,True)