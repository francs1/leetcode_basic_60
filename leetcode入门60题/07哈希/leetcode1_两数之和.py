#题目地址：https://leetcode-cn.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: 'List[int]', target: int) -> 'List[int]':
        s = {}
        for i in range(len(nums)):
            n = nums[i]
            cop = target - n
            if cop in s.keys():
                return [s[cop],i]
            s[nums[i]] = i
        return  []

'''
算法分析：
为方便理解，先定义一个概念——“补”。(我自己定义的，不是数学的定义)
假设a + b = target，则定义：在目标为target的情况下，a 是 b 的补，同样 b 是 a 的补。
使用字典s来存储已经遍历过的数值的“补”，即目标值与已遍历的值的差。
这样在遍历到一个新值时，如果 当前值 与s中已经存在的key相同，则表示当前值是已经遍历过的另一个值的“补”。
则可以获得本题所要求的两个和为target的数值的下标。
'''