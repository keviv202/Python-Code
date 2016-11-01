def rotate_array(n,k):
    n=n[len(n)-k:]+n[:len(n)-k]
    return n

print (rotate_array([1,2,3,4,5,6,7],3))
