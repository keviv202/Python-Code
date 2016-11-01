l1=[]
def rotate(l):
    #print (l[-1:] , l[:-1])
    return l[-1:] + l[:-1]

def rotate_function(l):
    j=0
    while j<len(l):
        l = rotate(l)
        sum=0
        for i in range (len(l)):
            sum = sum + i*l[i]
        l1.append(sum)
        j=j+1
    print(max(l1))


example_list = [4,3,2,6]
(rotate_function(example_list))
# [3, 4, 5, 1, 2]