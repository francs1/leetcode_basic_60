class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if m == 0:
            return 0
        if n == 0 or m > n:
            return -1
        if haystack == needle:
            return 0

        i,j = 0,0
        idx = i
        while i < n and j < m:
            if haystack[i] != needle[j]:
                i = idx + 1
                idx = i
                j = 0
            else:
                if idx == -1:
                    idx = i
                i += 1
                j += 1
            if j == m:
                return idx
        return -1