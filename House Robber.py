def rob(nums):
        n = len(nums)
        s = [0,0]
        for i in range(n):
            s.append(max(s[i]+nums[i], s[i+1]))
        return s[-1]

s=[123,334,556,778,999,1000]
print (rob(s))