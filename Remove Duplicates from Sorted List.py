def duplicate(n):
    n.append(9999999999999)
    a=len(n)
    i=0
    while i < len(n)-1:
        if n[i]==n[i+1]:
            n.remove(n[i])
        if n[i]!=n[i+1]:
            i=i+1

    n.remove(l[len(l)-1])
    print (n)
l = [1,2,3,4,5,6]
duplicate(l)