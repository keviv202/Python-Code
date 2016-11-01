def isomorphic(s,t):
    l=[]
    c=0
    for i in range(0,len(s)):
            l.append([s[i],t[i]])

    for i in l:
        for j in l:
            if i[0]==j[0] and i[1] !=j[1]:
                return False
    return True


print(isomorphic('egg','add'))