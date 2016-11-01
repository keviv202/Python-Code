def wordpattern(s,s1):
    s2=str.split(s1)
    l,l1,l2=[],[],[]
    for i in s:
        l.append(i)
    for j in s2:
        l1.append(j)
    #print (l,l1)

    for i in range(len(l)):
        l2.append([l[i],l1[i]])
    print(l2)

    for i in l2:
        for j in l2:
            if i[0]==j[0] and i[1]!=j[1]:
                return False
    else:
        return True
print(wordpattern('abba','dog cat cat dog'))