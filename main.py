import copy
import matrixUtils as mu
import theta
import ro
import pi
import chi
import l
w = 4
x_len = 5
y_len = 5
z_len = w
IR = 5
A = [[[0 for k in range(z_len)] for k in range(y_len)]
     for k in range(x_len)]
mu.populate(A)

def test():
    Ap = theta.theta(A)
    print("    After theta (A') | Before theta (A)")
    mu.matPrint(Ap, 'c', True, True, A)

    A = Ap
    Ap = ro.ro(Ap)
    print("           After Ro | Before Ro")
    mu.matPrint(Ap, 'l', True, True, A)


    AFIPS = mu.matToFIPS(Ap)
    A = Ap
    Ap = pi.pi(Ap)

    AFIPS = mu.matToFIPS(A)
    ApFIPS = mu.matToFIPS(Ap)
    mu.printSheet(AFIPS , ApFIPS, "A", "A'")

    A = Ap
    Ap = chi.chi(Ap)
    print("    After chi (A')   | Before chi (A)")
    mu.matPrint(Ap, 'r', True, True, A)                

    A = Ap
    Ap = l.l(Ap, IR)
    print("    After l (A')   | Before l (A)")
    mu.matPrint(Ap, 'l', True, True, A)   

def RND(mat, roundIndex):
    A = copy.deepcopy(mat)
    Ap = copy.deepcopy(mat)
    Ap = l.l(chi.chi(pi.pi(ro.ro(theta.theta(mat)))),roundIndex)
    
    AFIPS = mu.matToFIPS(A)
    ApFIPS = mu.matToFIPS(Ap)
    mu.printSheet(AFIPS , ApFIPS, "A", "A'")

RND(A, 1)