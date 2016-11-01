def atoi(s):
    n=0
    for i in range(0,len(s)):
        if ord(s[i]) == 48:
            n=n + 0* (10**(len(s)-1-i))
        elif ord(s[i]) == 49:
            n=n + 1* (10**(len(s)-1-i))
        elif ord(s[i]) == 50:
            n=n + 2* (10**(len(s)-1-i))
        elif ord(s[i]) == 51:
            n=n + 3* (10**(len(s)-1-i))
        elif ord(s[i]) == 52:
            n=n + 4* (10**(len(s)-1-i))
        elif ord(s[i]) == 53:
            n=n + 5* (10**(len(s)-1-i))
        elif ord(s[i]) == 54:
            n=n + 6* (10**(len(s)-1-i))
        elif ord(s[i]) == 55:
            n=n + 7* (10**(len(s)-1-i))
        elif ord(s[i]) == 56:
            n=n + 8* (10**(len(s)-1-i))
        elif ord(s[i]) == 57:
            n=n + 9* (10**(len(s)-1-i))
    print (n)
atoi('0123456789')