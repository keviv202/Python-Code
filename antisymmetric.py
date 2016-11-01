# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True
# if the given square is antisymmetric and False otherwise.
# An nxn square is called antisymmetric if A[i][j]=-A[j][i]
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def antisymmetric(A):
    i, j, c, d = 0, 0, 0, 0
    while (i < len(A)):
        while (j < len(A)):
            if (A[i][j] == -A[j][i]):
                c = c + 1
            i=i+1
            j=j+1

    if(c==len(A)):
        return True
    else:
        return False


# Test Cases:


print (antisymmetric(([[0, 1, 2],
               [-1, 0, 3],
               [-2, -3, 0]])))
# >>> True


antisymmetric(([[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]))
# >>> True


antisymmetric(([[0, 1, 2],
               [-1, 0, -2],
               [2, 2, 3]]))
# >>> False


(antisymmetric([[1, 2, 5],
               [0, 1, -9],
               [0, 0, 1]]))
# >>> False
