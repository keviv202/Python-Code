def bulls_cows(secret,guess):
    secret=str(secret)
    guess=str(guess)
    bulls =0
    cows = 0
    for i in range(0,len(secret)):
        for j in range (0,len(guess)):
            if i==j and secret[i]==guess[j]:
                bulls = bulls +1
                break
            elif i!=j and secret[i]==guess[j]:
                cows= cows +1
                break
    print ('A'+str(bulls)+'B'+str(cows))


bulls_cows('1807', '7810')