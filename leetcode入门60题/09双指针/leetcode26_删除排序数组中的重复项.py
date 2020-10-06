class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> int:
        prevalue = 0
        n = len(nums)
        count = 0
        i,j = 0,0
        while i < n:
            if i == 0:#第一个元素
                prevalue = nums[i]
                count += 1
                i += 1
                j += 1
            else:#非第一个元素
                cur = nums[i]
                if cur == prevalue:#连续相同值
                    i += 1#指针后移
                else:#非相同值
                    nums[j] = cur#给数组重新赋值
                    count += 1#不同元素的数量+1
                    prevalue = cur#更新prevalue
                    i += 1#读取下标+1
                    j += 1#写入下标+1
        return count

if __name__ == '__main__':
    S = Solution()
    ary = [1,1,2]
    res = S.removeDuplicates(ary)
    print(res,ary)