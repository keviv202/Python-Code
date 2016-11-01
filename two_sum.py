def two_sum(l,n):
    l1=[]
    for i in l:
        if n>i:
            l1.append(i)
        if l1[0]==i and i not in l1:
            l1.append(i)
    print(l1)

l=[2, 7, 11, 15]
two_sum(l,9)