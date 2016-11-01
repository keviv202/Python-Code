def validparen(s):
    l2=[]
    l = [['[',0],[']',0],['{',0],['}',0],['(',0],[')',0]]
    for i in s:
        if i =='[':
            l[0][1]=l[0][1]+1
        elif i ==']':
            l[1][1]=l[1][1]+1
        elif i =='{':
            l[2][1]=l[2][1]+1
        elif i  =='}':
            l[3][1]=l[3][1]+1
        elif i == '(':
            l[4][1] = l[4][1] + 1
        elif i == ')':
            l[5][1] = l[5][1] + 1
    #print (l)

    for i in l:
         l2.append(i[1])
    r=0
    for i in l2:
       r=r^i
    if r==0:
        print("Correct")
    else:
        print("Incorrect")
validparen('[[[]]]')