#For example, given input 43261596 (represented in binary as 00000010100101000001111010011100),
#return 964176192 (represented in binary as 00111001011110000010100101000000).

def reverse(n):
    str= bin(n)[2:]
    l,l1 = [],[]
    n1=32-len(str)
    if n1>0:
        for i in range(0,n1):
            l.append('0')

    for i in range(0,len(str)):
        l.append(str[i])
    print(l)

    for i in l[::-1]:
        l1.append(i)
    print(l1)

    print(''.join(l1))
reverse(43261596)
