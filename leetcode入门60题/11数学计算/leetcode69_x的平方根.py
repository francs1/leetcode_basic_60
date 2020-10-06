class Solution:
    def mySqrt(self, x: int) -> int:
        return x ** 0.5

    # #不使用内置函数
    # def mySqrt(self, x: int) -> int:
    #     r = x
    #     while r * r > x:
    #         r = (r + x // r) // 2
    #     return int(r)