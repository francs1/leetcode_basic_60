class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        operation = 1
        if x < 0:
            operation = -1
        sx = str(x)
        if sx[0] == '-':
            sx = sx[1:]
        n = len(sx)
        result = []
        for i in range(n-1,-1,-1):
            result.append(sx[i])
        r = int(''.join(result))
        r *= operation
        if r >= 2 ** 31 or r < (-2) ** 31:
            r = 0
        return r