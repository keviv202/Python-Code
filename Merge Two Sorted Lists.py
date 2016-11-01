class merge:
    def merge_list(self,n,n1):
        n.append(999999999999)
        n1.append(999999999999)
        a = []
        i = len(n)+len(n1)
        j,k,m=0,0,0
        while (j<i-2):
                if n[m]<n1[k]:
                    a.append(n[m])
                    j=j+1
                    m=m+1
                else:
                    a.append(n1[k])
                    k = k+1
                    j=j+1
        print (a)
n=[4,5,6,7,8]
n1=[1,2,3,9]
merge1 = merge()
merge1.merge_list(n,n1)