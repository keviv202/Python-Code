def run_length(s):
    a = [['A',0],['B',0],['C',0],['D',0],['E',0],['F',0],['G',0],['H',0],['I',0],['J',0],['K',0],['L',0],['M',0],['N',0],['O',0],['P',0],['Q',0],
         ['R', 0],['S',0],['T',0],['U',0],['V',0],['W',0],['X',0],['Y',0],['Z',0]]
    for i in s:
        k = ord(i)-65
        a[k][1]=a[k][1]+1
    b = []
    for i in a:
            if i[1] > 0:
                b.append(str(i[1])+i[0])
    print (''.join(b))

s='AAAABBBBCCCCCCCCC'
run_length(s)


'''Method 2
def run_length(s):
    a = []
    j = 0
    c=0
    for i in s:
        if len(a)==0:
            a.append([i,0])

        while (j<len(a)):
            if a[j][0]==i:
                a[j][1]=a[j][1]+1
                break
            else:
                c=c+1
                j=j+1

        if(c==len(a)):
            a.append([i,1])

    b = []
    for i in a:
        if i[1] > 0:
            b.append(str(i[1]) + i[0])
    print(''.join(b))





s='AAAABBBBCCCCCCCCCFFFFFFFF'
run_length(s)'''