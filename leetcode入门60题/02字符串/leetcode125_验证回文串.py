#https://leetcode-cn.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        S = list()#定义一个列表，模拟栈
        Q = list()#定义一个离诶包，模拟队列
        if len(s) == 0:#空字符串，被当作是回文字符串
            return True
        s = s.lower()#将原字符串转化为小写
        for c in s:#如果当前字符是小写字母(a~z)或者数字(0~9)
            if (ord(c) >= 97 and ord(c) <= 122) or (ord(c) >= 48 and ord(c) <= 57):
                S.append(c)#添加到栈中
                Q.append(c)#添加到队列中
        while len(S) > 0:
            ss = S.pop(-1)#栈取栈顶元素(尾部)
            qq = Q.pop(0)#队列取队头元素(首部)
            if ss != qq:#如果字符不相同，则表示不是回文
                return False
        return True#如果所有字符都比对完毕，没有发现不相同的字符，则是回文

if __name__ == '__main__':
    S = Solution()
    result = S.isPalindrome('A man, a plan, a canal: Panama')
    print(result)