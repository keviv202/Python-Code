def freq_analysis(message):
    s, a,c = 0, 0,0
    p, q = [], []
    while (s < len(message)):
        t=message[s]
        while (a<len(message)):
            if(t == message[a]):
                c=c+1
            a=a+1
        print ("Frequency of "+message[s]+" is "+str(c))
        c=0
        a=0
        s=s+1

#Tests

print (freq_analysis("abcd"))