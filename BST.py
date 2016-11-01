import sys

i=-1
class bst:
    root=None
    left=None
    right= None
    l,l1,f=[0],[0],[]
    b1,b2,b3,b4=[0],[],[],[]

    def insert(self,n):
        if self.root is None:
            self.root = n
        elif self.root is not None and n<self.root and self.left is None:
            self.left=bst()
            self.left.root=n
        elif self.root is not None and n>self.root and self.right is None:
            self.right=bst()
            self.right.root=n
        elif self.root is not None and n<self.root and self.left is not None:
            self.left.insert(n)
        elif self.root is not None and n>self.root and self.right is not None:
            self.right.insert(n)

        '''if self.left is not None and self.right is not None:
            print (self.root,self.left.root,self.right.root)
        elif self.left is None and self.right is not None:
            print((self.root,self.left,self.right.root))
        elif self.left is not None and self.right is None:
            print(self.root,self.left.root,self.right)'''

    def preorder(self,n):
        if self.root:
            print(self.root)
            if self.left:
                self.left.preorder(self.left.root)
            if self.right:
                self.right.preorder(self.right.root)

    def postorder(self,n):
        if self.root:
            if self.left:
                self.left.postorder(self.left.root)

            if self.right:
                self.right.postorder(self.right.root)
            print(self.root)

    def inorder(self,n):
        if self.root:
            if self.left:
                self.left.inorder(self.left.root)
                #print(self.left.root)
            #if self.left and self.right:
             #   print (self.root)
            print(self.root)
            if self.right:
                self.right.inorder(self.right.root)
                #print(self.right.root)
            #print(self.root)

    def find(self,n):
        if self.root==n:
            return True
        if self.left:
            return self.left.find(n)
        if self.right:
            return self.right.find(n)
        else:
            return False

    def depth(self):
        if self.root:
            if self.left:
                self.left.depth()
                self.l[0]=self.l[0]+1
            if self.right:
                self.right.depth()
                self.l1[0]=self.l1[0]+1

    def balanced_binary_tree(self):
        b.depth()
        if self.l[0]==self.l1[0]:
            return True
        else:
            return False

    def invert(self):
        if self.root:
            self.left,self.right=self.right,self.left
            if self.left is not None and self.right is not None:
                print (self.root,self.left.root,self.right.root)
            elif self.left is None and self.right is not None:
                print(self.root,self.left,self.right.root)
            elif self.left is not None and self.right is None:
                print(self.root,self.left.root,self.right)
            if self.left:
                self.left.invert()
            if self.right:
                self.right.invert()


    def lca(self,n,n1):
        self.lca_a(n,n1)
        self.lca_b(n,n1)


    def lca_a(self,n,n1):
        #n1=0
        if self.root:
            if n>self.root:
                self.right.lca_a(n,n1)
                self.b3.append(self.root)
            if n<self.root:
                self.left.lca_a(n,n1)
                self.b3.append(self.root)

    def lca_b(self,n,n1):
        #n=0
        if self.root:
            if n1>self.root:
                self.right.lca_b(n,n1)
                self.b4.append(self.root)
            if n1<self.root:
                self.left.lca_b(n,n1)
                self.b4.append(self.root)

    def lot(self):
        if self.root:
            self.b1[0] = self.b1[0] + 1
            self.b1.append([self.root, self.b1[0]])
            if self.left:
                self.lot_left()
            if self.right:
                self.b1[0] = 1
                self.lot_right()

    def lot_left(self):
        if self.left and self.right is None:
            self.b1[0] = self.b1[0] + 1
            self.b1.append([self.left.root, self.b1[0]])

        if self.left and self.right:
            self.b1[0] = self.b1[0] + 1
            self.b1.append([self.left.root, self.b1[0]])
            self.b1.append([self.right.root, self.b1[0]])
        if self.right and self.left is None:
            self.b1[0] = self.b1[0] + 1
            if [self.right.root, self.b1[0]] not in self.b1:
                self.b1.append([self.right.root, self.b1[0]])
        if self.left:
            self.left.lot_left()

    def lot_right(self):
        if self.right and self.left is None:
            self.b1[0] = self.b1[0] + 1
            if [self.right.root, self.b1[0]] not in self.b1:
                self.b1.append([self.right.root, self.b1[0]])

        if self.left and self.right:
            self.b1[0] = self.b1[0] + 1
            if [self.right.root, self.b1[0]] not in self.b1:
                self.b1.append([self.right.root, self.b1[0]])
            if [self.right.root, self.b1[0]] not in self.b1:
                self.b1.append([self.left.root, self.b1[0]])
        if self.left and self.right is None:
            self.b1[0] = self.b1[0] + 1
            if [self.left.root, self.b1[0]] not in self.b1:
                self.b1.append([self.left.root, self.b1[0]])
        if self.right:
            self.right.lot_right()

    def tree_path(self):
        if self.root:
            self.f.append(self.root)
            if self.left:
                self.left.tree_path()
                if self.left is not None and self.right is not None and self.left.left is None:
                    print(self.left.root,self.right.root)
            if self.left is None and self.right is not None:
               #print(self.right.root)
               self.right.tree_path()


    def tree_path1(self):
        if self.root:
            print(self.root)
            if self.right:
                self.right.tree_path()
            if self.right is None and self.left is not None:
               #print(self.right.root)
               self.left.tree_path()

b = bst()
b.insert(5)
b.insert(4)
b.insert(6)
b.insert(2)
b.insert(1)
b.insert(3)
#b.insert(-1)
b.insert(8)
#b.insert(-0.5)
#b.insert(-0.75)
#b.insert(6.5)
#b.preorder(-1)
#b.postorder(6)
#b.inorder(5)
#print (b.find(99))
#b.depth()
#if (b.l[0]>b.l1[0]):
#    print ("Highest depth is "+str(b.l[0]))
#else:
#    print("Highest depth is "+str(b.l1[0]))
#b.invert()
#print(b.lca(-1,6.5))
#print(b.b3,b.b4)
c=[]

'''for a in b.b1:
    for a1 in b.b2:
        if a==a1:
            c.append(a)
print(min(c))'''

#b.lot()
#b.b1.remove(b.b1[0])
#print(b.b1,b.b2)

#print(c)

#print(b.balanced_binary_tree())
b.tree_path()
#print(b.f)
b.tree_path1()