class Solution:
    def generateParenthesis(self, n: 'int') -> 'List[str]':
        y=list()
        string = '('
        L = 1#左括号数量
        R = 0#右括号数量
        self.BackTrack(L,R,n,string,y)
        return y

    def BackTrack(self,L,R,n,string,y):
        if L == R  == n:
            y.append(string)
        elif L == n and R < n:
            self.BackTrack(L,R+1,n,string + ')',y)
        elif L < n and R < n:
            self.BackTrack(L+1,R,n,string + '(',y)
            if L > R:
                self.BackTrack(L,R+1,n,string + ')',y)
        return