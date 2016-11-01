def excel_title(n):
    l=[]
    if n%26==0:
        l.append('Z')
        n=n-26
    else:
        while n%26 > 26:
            l.append(chr(64 + n % 26))
            n=n//26
        l.append(chr(64 + n % 26))
    while(n>26):
        n=n//26
        l.append(chr(64+n%26))

    print(l)

excel_title(475308)

