class Solution:
    def findDisappearedNumbers(self, nums: 'List[int]') -> 'List[int]':
        dic = {}
        maxvalue = len(nums)
        result = []        
        for n in nums:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
        for i in range(1,maxvalue+1):
            if i not in dic:
                result.append(i)
        return result