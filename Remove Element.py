def remove(n,m):
    for i in n:
        if i == m:
            n.remove(m)
    print (len(n))

n=[3,2,2,3]
remove(n,3)
