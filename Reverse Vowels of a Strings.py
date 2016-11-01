class reverse_vowel:
    def rev_vow(self,s):
        a=['a','e','i','o','u']
        b=[]
        c=[]
        d=[]
        for i in s:
            b.append(i)
        #print(b)

        for i in range(len(s)):
            if s[i] in a:
                c.append(s[i])
                b[i]='!'
        k = len(c)
        for j in range(len(c)):
            d.append(c[k-1])
            k=k-1
        j=0
        for i in range(len(b)):
            if b[i]=='!':
                b[i]=d[j]
                j=j+1

        print ("".join(b))
s='leotcede'
rever = reverse_vowel()
rever.rev_vow(s)
