def longestcommonprefix(l):
    l1=[]
    for i in l:
        for j in l:
            if j in i and j!=i and j not in l1:
                l1.append(j)


    print (l1)

longestcommonprefix(['leetcode','leet','lee','le'])