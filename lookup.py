def hashtable_lookup(htable,key):
    i,j,k,count = 0,0,0,0
    for i in htable:
        for j in i:
            for k in j:
                if k==key:
                    print (j[1])
                    count = count +1
    if (count==0):
        print ("None")

table = [[['Ellis', 11], ['Francis', 13]], [], [['Bill', 17], ['Zoe', 14]],
[['Coach', 4]], [['Louis', 29], ['Nick', 2], ['Rochelle', 4]]]

hashtable_lookup(table, 'abc')
#>>> 13