def valid_palindrme(s):
    l=[]
    s=s.lower()
    for i in s:
        if i in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9',
                 '0'):
            l.append(i)
    print (l)

    if l == l[::-1]:
        print ("Yes")
    else:
        print("No")


valid_palindrme('A man, a plan, a canal: Panama')