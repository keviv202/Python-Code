def range_sum_query(l,a,b):
    sum=0
    for i in range(a,b+1):
        sum = sum + l[i]
    print(sum)
l=[1,2,3,4,5]
range_sum_query(l,2,4)