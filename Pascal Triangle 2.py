def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)

def pascal(n):


        l = []
        for k in range(n+1):
            c1=fact(n)
            c2=fact(k)
            c3=fact(n-k)
            c4 = c2*c3
            ans = int(c1/c4)
            l.append(ans)
        print (l)


pascal(7)