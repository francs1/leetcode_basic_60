class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 2 and n % 3 == 0:
            n = n // 3
        return n == 1