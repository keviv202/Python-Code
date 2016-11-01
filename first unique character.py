class unique:
    def first_unique(self,s):
        s=list(s)
        count = 0
        for s1 in s:
            for s2 in s:
                if s1==s2:
                    count=count+1
            if count>=2:
                count=0
                continue
            elif count==1:
                print("The unique letter is ",s1)
                break

s="helloh"
u = unique()
u.first_unique(s)