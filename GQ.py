import random

def quick(n,start,end):
    if(start<end):
        partition=quicksort(n,start,end)
        quick(n,start,partition-1)
        quick(n,partition+1,end)


def quicksort(n,start,end):
    l = random.randrange(start,end+1)
    pivot=n[l]
    n[end],n[l]=n[l],n[end]
    i = start - 1
    for k in range(start,end+1):
        if n[k]<pivot:
            i=i+1
            n[k],n[i]=n[i],n[k]
    n[end],n[i+1]=n[i+1],n[end]
    return i+1

def hIndex(citations):
    start = 0
    end = len(citations) - 1
    quick(citations, start, end)
    n = len(citations)
    for i in range(n):
        if citations[i] >= (n-i):
            return n-i
    return 0


k = input("enter no of categories")
l= input("Enter no of items per category")
l= [int(x) for x in l.split()]

#for i in range (0,10000000):
#    citations.append(i)

print("The GQ is "+str(hIndex(l)))
