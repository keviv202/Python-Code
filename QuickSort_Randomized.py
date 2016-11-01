import random
import time

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

n=[]
k = int(input("enter the range you want to check"))
for i in range (k):
    n.append(random.randrange(-10000000000, 10000000000))

start=0
end=len(n)-1
start_time = time.time()
quick(n,start,end)
print(n)
print("")
print ("time elapsed: {:.8f}s".format(time.time() - start_time))

