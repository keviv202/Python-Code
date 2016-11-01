def reverse_number(n):
    l=[]
    while (n>9):
        l.append(n%10)
        n=n//10
    l.append(n)
    print(l)
    sum = 0
    for i in range(len(l)):
        sum = sum +l[i]*10**(len(l)-i-1)
    print (sum)
reverse_number(1234565789)