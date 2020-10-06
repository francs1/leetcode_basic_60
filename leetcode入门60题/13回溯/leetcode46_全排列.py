import itertools
#import itertools.combinations

class Solution:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        n = len(nums)
        temp = itertools.permutations(nums,n)
        #print(temp)
        result = []
        for i in temp:
            result.append(list(i))
        return result

# class Solution:
#     def dfs(self,nums,n,path,l,visited):
#         if len(path) == n:
#             l.append(path[:])
#         else:
#             if nums != None:
#                 for i in range(len(nums)):
#                     if visited[i] == 1:
#                         continue
#                     path.append(nums[i])
#                     visited[i] = 1
#                     self.dfs(nums,n,path,l,visited)
#                     visited[i] = 0
#                     path.pop(-1)


#     def permute(self, nums: 'List[int]') -> 'List[List[int]]':
#         n = len(nums)
#         path = list()
#         l = list()
#         visited = [0] * n
#         self.dfs(nums,n,path,l,visited)
#         return l

if __name__ == '__main__':
    S = Solution()
    S.permute([1,2,3])