import collections

class Solution:
    #方法一排序
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
    #方法二：哈希
    '''
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = collections.Counter(s)
        c2 = collections.Counter(t)
        if len(c1) != len(c2):
            return False
        for k,v in c1.items():
            if k not in c2 or v != c2[k]:
                return False
        return True
    '''


if __name__ == "__main__":
    S = Solution()
    S.isAnagram('hello','elloh')
