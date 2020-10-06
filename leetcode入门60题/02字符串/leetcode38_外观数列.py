#https://leetcode-cn.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            l = []#定义n=1,2,3……时对应的字符串
            l.append('1')#第0位固定是'1'
            result = ''#定义用于存储最终结果的字符串
            pre = ''#定义上一个字符串
            for i in range(1,n):#外层循环，从index=1开始
                pre = l[i-1]#n取前一个值的时候，得到的字符串
                c = pre[0]#前一个字符串的第0位
                newrow = ''#空行
                count = 1#计数器为1
                for j in range(1,len(pre)):#遍历前一个字符串，从index=1开始
                    cur = pre[j]#当前位置的字符
                    if c != cur:#如果当前字符和前一个字符不想等，例如'21'
                        newrow += str(count)#新字符串+'1'
                        newrow += c#新字符串+'2'
                        count = 1#计数器归1
                        c = cur#c更新为当前值cur
                    else:
                        count += 1#两个字符相同，例如'11'，则计数器+1
                newrow += str(count)#新字符串+count
                newrow += c#新字符串+c
                l.append(newrow)#n在当前取值时的字符串已经生成完毕，添加到集合l中
        result = l[-1]#集合最后一个元素，就是n取最后一个值时生成的字符串
        return result


if __name__ == '__main__':
    S = Solution()
    result = S.countAndSay(5)
    print(result)