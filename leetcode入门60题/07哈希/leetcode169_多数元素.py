class Solution:
    def majorityElement(self, nums: 'List[int]') -> int:
        dic = {}#定义一个字典，key是数字，value是出现次数
        length = len(nums)#计算列表的长度
        for n in nums:
            if n not in dic:#如果这个数字第一次出现
                dic[n] = 1#用字典记录出现了1次
            else:
                dic[n] += 1#出现次数增1
            if dic[n] > length // 2:#某个数字出现次数超过数组长度的一半
                return n#返回此数字