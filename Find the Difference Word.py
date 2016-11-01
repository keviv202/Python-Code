class first:
    def diff(self,s):
        d=[]
        result=0
        for i in range(0,len(s)):
            d.append(s[i])

        for k in d:
            result = result +ord(k)

        return (result)

s='hello'
s1='hello2'

firs = first()
sec  = first()
print (chr(sec.diff(s1)-firs.diff(s)))
#print (diff(s,s1))