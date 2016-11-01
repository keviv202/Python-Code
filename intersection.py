class intersection:
    def inse(self,n,n1):
        n2 = []
        for i in n:
            for j in range(0,len(n1)):
                if i ==n1[j] and i not in n2:
                    n2.append(i)
        print (n2)



n=[1,2,3,4,5]
n1=[1,2,2]
i = intersection()
if len(n)>len(n1):
    i.inse(n,n1)
else:
    i.inse(n1,n)