#题目地址：https://leetcode-cn.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: 'List[int]', k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)#获取原数组的长度
        #将原数组用切片分两部分
        part1 = nums[n-k:]#右半部分，从第n-k个元素开始，到最后一个元素
        part2 = nums[:n-k]#右半部分，从第0个元素开始，到第n-k-1个元素
        nums.clear()#将原数组清空
        nums.extend(part1)#空数组先拼接右半数组
        nums.extend(part2)#空数组再拼接左半数组

if __name__ == '__main__':
    S = Solution()
    inputAry = [1,2,3,4,5,6,7]
    k = 3
    S.rotate(inputAry,k)
    print(inputAry)