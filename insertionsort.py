import random
import time

def sort_numbers(s):
    for j in range(0, len(s)):
        for i in range(j-1,-1,-1):
            if s[i]>s[i+1]:
                s[i+1],s[i]=s[i],s[i+1]
            else:
                break

    return s


n=[]
k = int(input("enter the range you want to check"))
for i in range (k):
    n.append(random.randrange(-10000000000, 10000000000))

start_time = time.time()
a=sort_numbers(n)
print(a)
print("")
print ("time elapsed: {:.8f}s".format(time.time() - start_time))
