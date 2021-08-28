nums = [['b', 'd'], ['c', 'd'], ['f', 'b'], ['a', 'b'], ['g', 'h'], ['e', 'c']]
def find(nums):
    indegrees = dict()
    adj = dict()
    for pre, cur in nums:
        indegrees[pre] = 0
        indegrees[cur] = 0
        adj.setdefault(pre, [])
        adj.setdefault(cur, [])

    for pre, cur in nums:
        indegrees[cur] += 1
        adj[pre].append(cur)

    res = []
    queue = []
    for str in indegrees:
        if indegrees[str] == 0:
            queue.append(str)

    while queue:
        pre = queue.pop(0)
        res.append(pre)
        for cur in adj[pre]:
            indegrees[cur] -= 1
            if indegrees[cur] == 0:
                queue.append(cur)
    return res

print(find(nums))