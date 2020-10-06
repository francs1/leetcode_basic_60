#https://leetcode-cn.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power#最低位与1，然后左移power位，低位补0
            n = n >> 1#向右移动1位，高位补0
            power -= 1#power自减
        return ret

if __name__ == '__main__':
    S = Solution()
    result = S.reverseBits(43261596)
    print(result)