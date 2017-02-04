class Solution(object):
    def maxProfit(self, prices):
        if len(prices) < 2: return 0
        buy = prices[0]
        sale = 0
        profit = 0
        for i in range(len(prices)):
            if prices[i] < buy: #if item lower than buy, set as buy
                buy = prices[i]
            elif prices[i] > buy:
                sale = prices[i]
                if sale - buy > profit:
                    profit = sale - buy
        if sale == 0: return 0
        return profit

s = Solution()
print (s.maxProfit([2,4,1]))