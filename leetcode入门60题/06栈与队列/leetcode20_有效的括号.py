#地址:https://leetcode-cn.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)#获取字符串的长度
        if n == 0:#如果长度为0，则表示空串，本题认为是合法的串
            return True
        if n % 2 == 1:#如果是奇数个括号，则必然不合法
            return False
        stack = []#定义一个列表用来模拟栈
        for c in s:#循环字符串中的每个字符
            if c == '(' or c == '{' or c == '[':#如果是左括号
                stack.append(c)#直接入栈
            elif c == ')':#如果是右括号
                if len(stack) > 0:#栈不为空
                    if stack[-1] == '(':#栈顶元素是对应的左括号
                        stack.pop(-1)#目前合法，则将栈顶出栈
                    else:
                        stack.append(')')#栈顶元素无法匹配，则当前右括号入栈
                else:#栈为空，则无法匹配
                    return False
            elif c == '}':
                if len(stack) > 0:
                    if stack[-1] == '{':
                        stack.pop(-1)
                    else:
                        stack.append('}')
                else:
                    return False
            elif c == ']':
                if len(stack) > 0:
                    if stack[-1] == '[':
                        stack.pop(-1)
                    else:
                        stack.append(']')
                else:
                    return False
        if len(stack) == 0:#如果栈可以左右都匹配（成对消除）
            return True#则是合法串
        else:
            return False

'''
题目解析：
本题使用栈的“先进后出”的特点，使用python的list的append()和pop()方法，
实现栈的入栈和出栈操作。

'''