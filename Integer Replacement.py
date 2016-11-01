def Integer_Replacement(n):
    c=0
    while n !=1:
        if n%2==0:
            n=n/2
            c=c+1
        else:
            n=n-1
            c=c+1
    return c

print(Integer_Replacement(7))
