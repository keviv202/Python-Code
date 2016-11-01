def Count_Primes(n):
    l=[2]
    c=0
    for i in range(3,n):
        for j in range (2,int(i/2)+1):
            if i%j ==0:
                c=c+1
                break
        if c==1:
            c=0
        else:
            l.append(i)





    print(l)

Count_Primes(100)
