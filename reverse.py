def reverseString(s):
    i=len(s)
    j=i
    r=[]
    while(i > 0):
        r.append(s[j-1])
        j=j-1
        i=i-1
    print ("".join(r))

s="hello"
reverseString(s)