def symmetric(l):
    c,d=0,0
    for i1 in l:
        d=d+1
        for i2 in i1:
            c=c+1
    if(c==(d*d)):
        return True
    else:
        return False
    print (c,d)
l= [[1, 2], [1,2,1]]
print (symmetric(l))