#题目地址：https://leetcode-cn.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: 'List[int]') -> 'List[int]':
        n = len(digits)#获取原来数组的长度
        temp = [0] * n#生成一个与原数组相同长度的全0数组
        up = 0#是否进位
        last = digits[-1]#最低位的数字[4,3,2,1][-1] => 1
        last += 1#将最低位的数字+1
        if last == 10:#判断+1后是否是10
            temp[-1] = 0#如果是0，则最低位更新为0
            up = 1#表示有一个进位
        else:
            temp[-1] = last#没有进位

        for i in range(n-2,-1,-1):
            cur = digits[i]#从倒数第二位开始，向左(高位)循环
            cur += up#增加进位(up的值可以取0表示没有进位，可以取1表示有进位)
            if cur == 10:#进一步判断是否会产生新的进位
                temp[i] = 0
                up = 1
            else:
                temp[i] = cur
                up = 0
        if up == 1:#当循环结束的时候，已经计算到了最高位(index=0的位置)，如果还存在进位
            temp.insert(0,1)#则在结果数组的左端(index=0的位置)，插入一个1
        return temp#返回结果数组

if __name__ == '__main__':
    S = Solution()
    result = S.plusOne([4,3,2,1])
    print(result)

    # a = [1,2,3,4,5]#list
    # # for i in range(len(a)-1,-1,-1):
    # #     print(a[i])
    # #range(10)   ==  range(0,10)   ==range(0,         10,          1)
    #                                       #从谁开始  到谁结束（不含） 步进
    # # for i in range(9,-1,-1):#倒序4
    # #     print(i)
    # b = []
    # #b = a[:]

    # #b = a.copy()
    # b.extend(a)
    # print(b)                                      #10,9,2……
    # # a.reverse()#1倒序
    # # for x in b:
    # #     print(x)

    # # for x in reversed(a):#2倒序
    # #     print(x)

    # # for x in a[::-1]:#3倒序
    # #     print(x)



