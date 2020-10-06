class Solution:
    #返回True表示有环，返回False表示无环
    def dfs(self,visited,memo,dic,i):
        if visited[i]:
            return True
        if memo[i] == 0:
            return False
        elif memo[i] == 1:
            return True
        for cs in dic[i]:
            visited[i] = True
            bl = self.dfs(visited,memo,dic,cs)
            visited[i] = False
            if bl:
                #当前线路中出现了环，则标记当前课程为1，返回True
                memo[i] = 1
                return True
        ##当前线路，已经找到最早的前置课程，没有出现"环"，则标记为0，表示课程i是可以学习的
        memo[i] = 0
        return False#返回False表示无环，当前课程i，可以完成学习

    def canFinish(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'bool':
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
        for i in range(numCourses):
            #只要出现过一个有环的线路，则不能符合题目"所有课程都完成"的目标
            if self.dfs(visited,memo,dic,i):
                return False
        return True