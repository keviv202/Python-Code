class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict={}
        c = 0
        for i in nums:
            if i not in dict:
                dict[i]=1
            else:
                dict[i]=dict[i] + 1

        for i in dict:
            if dict[i]>1:
                return True

        return False


s = Solution()
print(s.containsDuplicate([1,1]))