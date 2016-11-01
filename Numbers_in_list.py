def numbers_in_lists(string):
    s, a,c = 0, 0,0
    p, q = [], []
    while (s < len(string)):

        print(string[s])

        if (s == 0):
            a = int(string[0])
            q.append(string[s])
            s=s+1
            continue




        if (a > int(string[s])):
            p.append(string[s])
            c= c+1

        if (c > 0 ):

            if(int(string[s])>a):
                q.append(p)
                p = []
                c=0

        if((a < int(string[s]))):
            q.append(string[s])

        a = int(string[s])



        #q.append(string[s])
        s = s + 1

    print(q)


# testcases
string = '543987'
numbers_in_lists(string)