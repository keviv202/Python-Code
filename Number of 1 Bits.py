def hammingWeight(n):

    c = 0
    while n:
        n = n & n - 1
        c += 1
    return c
n= 0o0000000000000000000000000001010
print (hammingWeight(n))
