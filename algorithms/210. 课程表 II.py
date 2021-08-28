class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = len(prerequisites)
        if n == 0:
            return [i for i in range(numCourses)]
        indegrees = [0 for _ in range(numCourses)]
        adj = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adj[pre].append(cur)
        res = []
        queue = []
        for i in range(numCourses):
            if indegrees[i] == 0:
                queue.append(i)
        while queue:
            pre = queue.pop(0)
            res.append(pre)
            for cur in adj[pre]:
                indegrees[cur] -= 1
                if indegrees[cur] == 0:
                    queue.append(cur)
        if len(res) != numCourses:
            return []
        return res