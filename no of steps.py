def climbStairs(n):
    l1, l2 = 0, 1
    for i in range(n):
        l1, l2 = l2, l1 + l2
    return l2

print (climbStairs(5))

#OR

'''def climbStairs(n):
    if n == 0 or n==1:
        return 1
    else:
        return climbStairs(n-2) + climbStairs(n-1)

print (climbStairs(4))'''