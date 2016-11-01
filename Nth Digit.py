def nth(n):
    l=[]
    for i in range(n+1):
        l.append(str(i))

    s=(''.join(l))

    print(s[n])

nth(100)