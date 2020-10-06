class Solution:
    def containsDuplicate(self, nums: 'List[int]') -> bool:
        dic = {}
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                return True
        return False