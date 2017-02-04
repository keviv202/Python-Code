def cut_rod(p,n,c):
    r,s = [0]*n,[0]*n

    for j in range(0,n):
        q = p[j]
        s[j]=j+1
        for i in range (0,j+1):
            if q < p[i]+(r[j-i-1]-c):
                q= p[i]+(r[j-i-1]-c)
                s[j]=i+1
        r[j]=q
    return r,s

def print_rod(p,n,c):
    (r,s) = cut_rod(p,n,c)
    print("The maximum revenue is " +str(r[n - 1]))
    while n > 0:
        print("Cut" +str(s[n-1]))
        n= n - s[n-1]
    #print("The cuts are" + str(s))
print_rod([1,5,8,9,10,17,17,20,24,30],8,1)