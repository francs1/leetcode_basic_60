class Solution:
    def titleToNumber(self, s: 'str') -> 'int':
        s = s.upper()
        n = len(s)
        sums = 0
        k = 0
        for i in range(n-1,-1,-1):
            asci = ord(s[i]) - 64
            sums += 26 ** k * asci
            k += 1
        return sums