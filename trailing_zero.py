def trailingZeroes(n):
    c=0
    for i in range(1,n+1):
        #print (i%5)
        while i%5==0:
            i=i//5
            c=c+1
    print (c)

print(trailingZeroes(100))

#OR
'''
def trailingZeroes(n):
    count = 0
    while n:
        k = n / 5
        count += k
        n = k
    return count
'''