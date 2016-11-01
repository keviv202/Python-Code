class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        sum = 0
        while num > 0:
            r = num % 10
            num = num // 10
            sum = sum + r
        if sum > 9:
            return self.addDigits(sum)
        else:
            return sum


s = Solution()
s.addDigits(10)
