def prime(n):
    flag=0
    for i in range(2,n//2+1):
        if n%i==0:
            flag = flag+1
            break

    if(flag==1):
        return n
    else:
        return 'ok'

prime(140)