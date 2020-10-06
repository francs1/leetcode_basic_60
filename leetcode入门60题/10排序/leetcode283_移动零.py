class Solution:
    def moveZeroes(self, nums: 'List[int]') -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,j = 0,0
        n = len(nums)
        while i < n:
            cur = nums[i]
            if cur == 0:
                i += 1
            else:
                nums[j] = cur
                i += 1
                j += 1
        while j < n:
            nums[j] = 0
            j += 1