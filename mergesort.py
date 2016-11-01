def mergesort(a):
    l=0
    h=len(a)
    p = int((l+h)/2)
    n1= h-p
    n2 = p
    b,c,d,e,f = [],[],[],[],[]
    for k in range(0,n1):
        b.append(a[k])
    print (b)
    for l in range(n1,h):
        c.append(a[l])
    print (c)
    for i in range(0,len(b)):
        min=b[0]
        for j in range(0,len(b)):
            if(min>b[j]):
                min=b[j]
        b.remove(min)
        d.append(min)
    print (d)
    for m in range(0,len(c)):
        min=c[0]
        for j in range(0,len(c)):
            if(min>c[j]):
                min=c[j]
        c.remove(min)
        e.append(min)
    print (e)

    d.append(99999)
    e.append(99999)

    i,j = 0,0
    for k in range (0,h+1):
        if d[i]>e[j]:
            f.append(e[j])
            j=j+1
        else:
            f.append(d[i])
            i=i+1

    print (f)

a= [10,12,33,1,5,112]
mergesort(a)