class find:
    def find(self,i,j):
        n = []
        for i1 in i:
            if i1 in j:
                n.append(i1)
        print(n)

j=[2, 2]
i=[1,2, 2,1]
f = find()
if len(j)>len(i):
    f.find(i,j)
else:
    f.find(j,i)