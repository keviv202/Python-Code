class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        l = []
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] = dict[i] + 1
            if dict[i] > len(nums) / 2:
                return i


s = Solution()
print(s.majorityElement([1, 1, 1, 1, 2, 3]))