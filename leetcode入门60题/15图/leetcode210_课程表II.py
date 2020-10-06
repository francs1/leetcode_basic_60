class Solution:
    def dfs(self,visited,memo,dic,i,postCourse):
        if visited[i]:
            return True
        if memo[i] == 0:
            return False
        elif memo[i] == 1:
            return True
        for cs in dic[i]:
            visited[i] = True
            bl = self.dfs(visited,memo,dic,cs,postCourse)
            visited[i] = False
            if bl:
                memo[i] = 1
                return True
        memo[i] = 0
        postCourse.append(i)
        return False
    def findOrder(self, numCourses: int, prerequisites: 'List[List[int]]') -> 'List[int]':
        dic = {}
        n = len(prerequisites)
        for i in range(numCourses):
            dic[i] = []
        for i in range(n):
            cs = prerequisites[i][0]#当前课程
            pre = prerequisites[i][1]#前置课程
            dic[cs].append(pre)
        visited = [False for _ in range(numCourses)]
        memo = [-1 for _ in range(numCourses)]
        postCourse = []
        for i in range(numCourses):
            if self.dfs(visited,memo,dic,i,postCourse):
                return []
        return postCourse