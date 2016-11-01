def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)

def pascal(n):

    i=0
    while i<n:
        l = []
        for k in range(i+1):
            c1=fact(i)
            c2=fact(k)
            c3=fact(i-k)
            c4 = c2*c3
            ans = int(c1/c4)
            l.append(ans)
        print (l)
        i=i+1

pascal(7)