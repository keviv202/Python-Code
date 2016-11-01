# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.

def rotate(strg, n):
    i = 0
    s = []
    while (i < len(strg)):
        if (ord(strg[i]) == 32):
            s.append(chr(32))
            i = i + 1
            continue
        s.append(chr(ord(strg[i]) + n))
        if (ord(s[i]) > 122):
            s[i] = chr(ord(s[i]) - 26)
        elif (ord(s[i]) < 97):
            s[i] = chr(ord(s[i]) + 26)
        i = i + 1

    return "".join(str(x) for x in s)


print (rotate('sarah', 13))
# >>> 'fnenu'
print (rotate('fnenu', 13))
# >>> 'sarah'
print (rotate('dave', 5))
# >>>'ifaj'
print (rotate('ifaj', -5))
# >>>'dave'
print (rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
        "sv rscv kf ivru kyzj"), -17))
# >>> ???