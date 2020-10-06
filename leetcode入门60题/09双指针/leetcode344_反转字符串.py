class Solution:
    def reverseString(self, s: 'List[str]') -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        i,j = 0,n-1
        while i < j:
            s[j],s[i] = s[i],s[j]
            i += 1
            j -= 1