class Heap:
    l =[-99999999]
    def insert(self,n):
        self.l.append(n)



    def create_heap(self):
        n = int(len(self.l)/2)
        flag = 1
        while flag >0:
            for i in range(1,n+1):
                #print("parent "+str(self.l[i]))
                #print ("child " +str(self.l[2*i]),str(self.l[2*i+1]))
                if (self.l[i-1] > self.l[int((i-1)*2)]):
                    self.l[int((i-1)*2)], self.l[i-1] = self.l[i-1], self.l[int((i-1)*2)]
                    flag = 1
                    break
                if (self.l[i-1] > self.l[int((i-1)*2)+1]):
                    self.l[int((i-1)*2)+1], self.l[i-1] = self.l[i-1], self.l[int((i-1)*2)+1]
                    flag = 1
                    break
                flag = 0
        print(self.l)
h = Heap()
h.insert(4)
h.insert(9)
h.insert(3)
h.insert(7)
h.insert(1)
#h.insert(8)
#h.insert(-2)
#h.insert(33)
h.create_heap()