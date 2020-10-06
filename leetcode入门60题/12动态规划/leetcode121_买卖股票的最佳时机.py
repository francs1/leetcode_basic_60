import sys
class Solution:
    def maxProfit(self, prices: 'List[int]') -> int:
        n = len(prices)
        maxval = 0
        minval = sys.maxsize
        for i in range(n):
            cur = prices[i]
            minval = min(minval,cur)
            maxval = max(maxval,cur-minval)
        return maxval