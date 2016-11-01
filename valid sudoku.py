class suduku:
    l = [[[5, 3, -1], [6, -1, -1], [-1, 9, 8]], [[-1, 7, -1], [1, 9, 5], [-1, -1, -1]],
         [[-1, -1, -1], [-1, -1, -1], [-1, 6, -1]], [[8, -1, -1], [4, -1, -1], [7, -1, -1]],
         [[-1, 6, -1], [8, -1, 3], [-1, 2, -1]], [[-1, -1, 3], [-1, -1, 1], [-1, -1, 6]],
         [[-1, 6, -1], [-1, -1, -1], [-1, -1, -1]], [[-1, -1, -1], [4, 1, 9], [-1, 8, -1]],
         [[2, 8, -1], [-1, -1, 5], [-1, 7, 9]]]
    l1 = []
    m,n,o,x,y=0,3,0,0,0

    def valid_sudoku(self):

        for i in self.l:
            for j in range(0,3):
                for k in range(0,3):
                    if i[j][k]!=-1:
                        self.l1.append(i[j][k])

            if len(self.l1)==len(set(self.l1)):
                self.l1=[]
            else:
                return False
        self.rows(self.m,self.n,self.o)
    def rows(self,m,n,o):
        for i in range(self.m,self.n):
            for j in self.l[i][self.o]:
                if j != -1:
                    self.l1.append(j)

        if len(self.l1)==len(set(self.l1)):
            self.l1=[]
            if self.m<6 and self.n<9:
                self.n,self.m,self.o=self.n+3,self.m+3,self.o+1
                self.rows(self.m,self.n,self.o)
            else:
                self.column(self.x,self.y)
        else:
            return False


    def column(self,x,y):
            for j in range(0,3):
                if self.l[self.x][j][self.y] != -1:
                    self.l1.append(self.l[self.x][j][self.y])

            if self.x ==0 or x==3:
                self.x=self.x+3
                self.column(self.x,self.y)
            elif self.x ==1 or x==4:
                self.x=self.x+3
                self.column(self.x,self.y)
            elif self.x ==2 or x==5:
                self.x=self.x+3
                self.column(self.x,self.y)
            if len(self.l1) == len(set(self.l1)):
                self.l1 = []

            else:
                return False
            if self.y <2 and self.x==6:
                #print("New column")
                self.y=self.y+1
                self.x=0
                self.column(self.x,self.y)
            elif self.y <2 and self.x==7:
                #print("New column")
                self.y=self.y+1
                self.x=1
                self.column(self.x,self.y)
            elif self.y <2 and self.x==8:
                #print("New column")
                self.y=self.y+1
                self.x=2
                self.column(self.x,self.y)
            if self.x==6:
                self.x=1
                self.y=0
                self.column(self.x, self.y)
            elif self.x==7:
                self.x = 2
                self.y = 0
                self.column(self.x, self.y)

s = suduku()
str=(s.valid_sudoku())
if str==False:
    print("Invalid")
else:
    print("Valid")

