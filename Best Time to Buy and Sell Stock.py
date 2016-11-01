class best:
    def best(self,n):
        n.append(-99999999999)
        c=0
        high=n[0]
        min =n[0]

        for i in range (len(n)-1):
            if n[i]>n[i+1]:
                c =c+1

        if c==len(n)-1:
            print ('No profit available')

        else:

            for i in range(len(n)-1):
                if n[i]>high:
                    high = n[i]
                if n[i]<min:
                    min = n[i]

            print (high-min)

best1 = best()
best1.best([7,6,5,4,3,2,1,9])
