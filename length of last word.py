def lengthofword(s):
    s=str.split(s)
    l=[]
    for i in s:
        l.append(i)

    print(l)

    st=l[-1]
    print(len(st))
lengthofword("Hello World")

