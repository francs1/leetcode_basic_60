import sys
class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        sums = 0
        maxsum = -sys.maxsize
        n = len(nums)
        for i in range(n):
            if sums < 0:
                sums = nums[i]
                maxsum = max(maxsum,nums[i])#使用当前值更新最大值
            else:
                sums += nums[i]
                maxsum = max(maxsum,sums)#使用当前连续和更新最大值
        return maxsum