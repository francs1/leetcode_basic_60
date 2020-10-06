class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = 0
        while n != 0:
            cur = n % 2
            if cur == 1:
                ret += 1
            n = n // 2
        return ret

'''
class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31
        while n != 0:
            m = n & 1
            m = m << power
            ret = ret + m#最低位与1，然后左移power位，低位补0
            n = n >> 1#向右移动1位，高位补0
            power -= 1#power自减
        return ret
'''