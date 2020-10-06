#题目地址：https://leetcode-cn.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> str:
        n = len(strs)#获取数组长度
        if n == 0:#如果是空数组，则返回空串
            return ''
        if n == 1:#如果数组中只有一个字符串
            return strs[0]#则返回这个字符串
        j = 0#定义索引j用于遍历每个字符串中的字符
        while True:
            for i in range(1,n):#从index=1开始，比较“当前位置”和“前一个位置”的字符串
                if j >= len(strs[i-1]) or j >= len(strs[i]):#如果索引就超过了当前用于对比的任意一个字符串的长度
                    return strs[i][:j]#则返回当前字符串的前半部分的切片(不包含j的位置的字符)
                if strs[i-1][j] != strs[i][j]:#如果用于对比的两个字符串的当前字符不相同
                    return strs[i][:j]#则返回当前字符串的前半部分的切片(不包含j的位置的字符)
            j += 1#内存循环没有return，则j自增继续下一次循环
        return strs[0]#循环都执行完毕，说明所有的字符都是一样的，此时j==len(strs[0])

if __name__ == '__main__':
    S = Solution()
    result = S.longestCommonPrefix(["flower","flow","flight"])
    print(result)