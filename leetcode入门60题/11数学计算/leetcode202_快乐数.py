class Solution:
    def isHappy(self, n: int) -> bool:
        s = set([n])
        while n != 1:
            sn = str(n)
            sums = 0
            for i in range(len(sn)):
                sums += int(sn[i]) ** 2
            if sums in s:
                return False
            s.add(sums)
            n = sums
        return True