s = 'hello'
count = 0
for i in range (0,len(s)):
    if (s[i]==s[len(s)-1-i]):
        count = count +1

if count==len(s):
    print('palindrome')
else:
    print('not palindrom')