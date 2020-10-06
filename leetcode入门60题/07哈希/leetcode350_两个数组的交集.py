import collections

class Solution:
    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        result = []
        c1 = collections.Counter(nums1)#计算nums1的元素及出现频率
        c2 = collections.Counter(nums2)#计算nums2的元素及出现频率
        for k in c1.keys():#循环c1
            if k in c2:#如果c2中也出现过
                times = min(c1[k],c2[k])#计算出现了多少次(较少的)
                result += [k] * times#将元素添加进结果数组
        return result
        