def excel_col(n):
    sum=0

    for i in range (0,len(n)):
        sum = sum + (ord(n[i])-64)* 26 ** (len(n)-i-1)
    print (sum)

excel_col('AAAB')