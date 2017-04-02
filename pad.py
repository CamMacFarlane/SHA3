def pad(x,m):
    j = (-m-2)%x
    z = [0] * j
    ret = [1]
    ret += z
    ret += [1]
    print(ret)

pad(10,7)    