#https://leetcode-cn.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: 'List[int]') -> int:
        a = 0
        for i in nums:
            a ^= i
        return a

if __name__ == '__main__':
    S = Solution()
    result = S.singleNumber([4,1,2,1,2])
    print(result)

'''
分析：利用位运算的两个性质：
性质1:
1 ^ 0 = 1
0 ^ 0 = 0
因此
x ^ 0 = x

性质2:
1 ^ 1 = 0
0 ^ 0 = 0
因此
x ^ x = 0


异或运算是符合"交换律"和"结合律"的，可以理解为实数的加法
也就是说
0 ^ 4 ^ 1 ^ 2 ^ 1 ^ 2
等价于
0 ^ 4 ^ (1 ^ 1) ^ (2 ^ 2)
等价于(利用性质1，将1^1计算出来，将2^2计算出来)
0 ^ 4 ^ 0 ^ 0
等价于
0 ^ 4
等于(利用性质2)
4
而这正好就是在nums中只出现过一次的数字
'''