class Solution:
    def countPrimes(self, n: int) -> int:
        nfilter = [False] * n
        count = 0
        for i in range(2,n):
            if nfilter[i]:#非素数
                continue
            count += 1#假如i是质数，那i的所有倍数都是非素数
            k = i + i#i的2倍
            while k < n:
                nfilter[k] = True#都标记为True，非素数
                k += i#i再增加一倍
        return count
'''
使用质数筛法查询质数：
nfilter用于标记哪些数字是素数，质数标记False，非质数标记为True
'''