#https://leetcode-cn.com/problems/sum-of-two-integers/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        l = [a,b]
        result = sum(l)#直接使用python内置函数sum()求和
        return result

if __name__ == '__main__':
    S = Solution()
    result = S.getSum(-2,3)
    print(result)
