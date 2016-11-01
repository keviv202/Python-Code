def selection(s):
    min = s[0]
    b = []
    for i in range(0,len(s)):
        min = s[0]
        for j in range(0,len(s)):
            if(min > s[j]):
                min = s[j]
        s.remove(min)

        b.append(min)
    return b

print (selection([4,6,1,8]))
