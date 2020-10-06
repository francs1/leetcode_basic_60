#题目地址：https://leetcode-cn.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> 'List[List[int]]':
        result = []#定义一个空数组，用于保存基本最终结果(二维数组))
        for i in range(numRows):
            if i == 0:#第一行：[1]
                result.append([1])
            elif i == 1:#第二行：[1,1]
                result.append([1,1])
            else:# i >= 2#第三行以后
                prerow = result[-1]#上一行
                currow = []#当前行
                for j in range(i+1):#循环j，表示二维数组中的：第i行、第j列
                    if j == 0 or j == i:#第一列和最后一列是1
                        currow.append(1)
                    else:#中间列，上一行的第j-1列元素 + 上一行的第j列元素
                        currow.append(prerow[j-1] + prerow[j])
                result.append(currow)#将当前行添加到结果数组中
        return result#返回结果数组

if __name__ == '__main__':
    S = Solution()
    result = S.generate(5)
    print(result)



    #  python:list     (Java:Array)
    #多个list组成的1个list

    # result = []
    # result.append([1])   -> [[1]]
    # result.append([1,1])  ->[[1],[1,1]]
    # result.append([1,2,1]) ->[[1],[1,1],[1,2,1]]
    # print(result)
    # result.append([1,3,3,1])
    # print(result)
