class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()#对nums进行排序
        prenum = 0#默认从0开始
        for x in nums:#循环排好序的nums
            if x != prenum:#如果当前值和prenum不等，说明有缺失
                return prenum
            else:
                prenum += 1#相当，则表示不缺失
        return prenum#对于特殊情况[0]，返回1