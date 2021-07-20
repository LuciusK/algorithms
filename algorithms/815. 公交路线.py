class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        n = len(routes)
        m = dict()
        for i in range(n):
            for j in routes[i]:
                if j in m:
                    m[j].append(i)
                else:
                    m[j] = [i]
        visited = [False] * n 
        queue = []
        for x in m[source]:
            queue.append(x)
            visited[x] = True
        step = 0
        while queue:
            step += 1
            queue_len = len(queue)
            for i in range(queue_len):
                t = queue.pop(0)
                for j in routes[t]:
                    if j == target:
                        return step
                    for x in m[j]:
                        if not visited[x]:
                            queue.append(x)
                            visited[x] = True
        return -1