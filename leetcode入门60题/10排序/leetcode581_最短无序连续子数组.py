class Solution:
    def findUnsortedSubarray(self, nums: 'List[int]') -> int:
        n = len(nums)
        temp = sorted(nums)
        start,end = 0,n-1
        while start < n and temp[start] == nums[start]:
            start += 1
        while end > start and temp[end] == nums[end]:
            end -= 1
        return end - start + 1