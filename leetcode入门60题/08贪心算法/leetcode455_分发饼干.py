class Solution:
    def findContentChildren(self, g: 'List[int]', s: 'List[int]') -> int:
        g.sort()#对g排序
        s.sort()#对s排序
        a, b = 0, 0#设定两个指针，分别指向g和s的0索引
        res = 0#记录结果
        while a < len(g) and b < len(s):
            if g[a] <= s[b]:#满足值<=饼干大小
                res += 1#得到满足的孩子数量+1
                a += 1#指向下一个孩子(的满足值)
                b += 1#指向下一块饼干(的大小)
            else:
                b += 1#这个孩子不能满足，孩子不动，只移动饼干指针
        return res
