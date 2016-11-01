class zero:
    def move_zero(self,n):
        for i in n:
            if i == 0:
                n.remove(i)
                n.append(0)

        print (n)

n=[0,1,0,3,0,0,0,0,0,12,0,0,0,0,0]

z= zero()
z.move_zero(n)