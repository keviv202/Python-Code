def plus_one(a):
    a1,a2=[],[]
    c=0
    for i in range(len(a)):
        a1.append(9)
        a2.append(0)

    for i in range(len(a)):
        if a[i]==a1[i]:
            c=c+1
    if c ==len(a):
        a=[]
        a.append(1)
        for i in a2:
            a.append(i)

    elif a[len(a)-1]<9:
        a[len(a) - 1]=a[len(a)-1]+1

    elif a[len(a)-1]==9:
        a[len(a) - 1] = 0
        a[len(a) - 2] = a[len(a) - 2] + 1



    print(a)

plus_one([9,9,9])