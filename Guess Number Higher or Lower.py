def guess(mid):
    if n[mid] == n1:
        return 0
    elif n[mid] > n1:
        return -1
        #high = mid
    elif n[mid] < n1:
        return 1
        #low = low + mid


def guessnumber(n,n1):
    low=0
    high=len(n)
    while low<high:
        mid= int((low+high)/2)
        s=guess(mid)
        if s==0:
            print("Yoo")
            break
        elif s==-1:
            high = mid
        elif s==1:
            #return 1
            low = low + mid
        guess(mid)


n=[]
n1=53
for i in range(100):
    n.append(i)

s=guessnumber(n,n1)
