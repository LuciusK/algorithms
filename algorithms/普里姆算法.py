from collections import defaultdict
from heapq import *
 
n = 4
edges = [[0,1,1],[0,3,3],[0,2,6],[2,3,2],[1,2,4],[1,3,5]]
adj = defaultdict(list)
for e in edges:
    adj[e[0]].append((e[1], e[2]))
    adj[e[1]].append((e[0], e[2]))

queue = []
cost = 0
visited = set()
heappush(queue, (0, 0))
for _ in range(n):
    while True:
        w, u = heappop(queue)
        if u in visited:
            continue
        cost += w
        visited.add(u)
        for v, w in adj[u]:
            if v in visited:
                continue
            heappush(queue, (w, v))
        break

print(cost)