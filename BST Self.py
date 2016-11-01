l = []

def bst(n,l):

    if not l:
        l.append([[] , n , []])
    elif l[0][1]>n:
        bst(n,l[0][0])
    elif l[0][1]<n:
        bst(n,l[0][2])

bst(14,l)
bst(6,l)
bst(2,l)
bst(1,l)
bst(8,l)
bst(5,l)
bst(9,l)
bst(10,l)
bst(17,l)
bst(12,l)
bst(13,l)
print(l)
