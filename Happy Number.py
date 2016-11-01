def happy_number(n):
    l =[]
    b=str(n)
    sum = 0
    for i in b:
            l.append(i)
    print (l)
    for j in l:
        sum = sum + int(j)*int(j)

    if sum<7:
        if sum == 1:
            print("happy number")
        else:
            print("not a happy number")
    else:
        happy_number(sum)


happy_number(4)