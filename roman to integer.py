class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        sum1, sum2 = 0, 0
        for i in range(0, len(num1)):
            sum1 = sum1 + (ord(num1[(len(num1) - i - 1)]) - 48) * (10 ** i)
        for i in range(0, len(num2)):
            sum2 = sum2 + (ord(num2[(len(num2) - i - 1)]) - 48) * (10 ** i)
        return str(sum1 + sum2)


s = Solution()
print (s.addStrings('123','1234'))