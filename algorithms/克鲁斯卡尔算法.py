n = 4
edges = [[0,1,1],[0,3,3],[0,2,6],[2,3,2],[1,2,4],[1,3,5]]
p = list(range(n))

def find(x):
    if x != p[x]:
        p[x] = find(p[p[x]])
    return p[x]

cost = 0
for u, v, w in sorted(edges, key=lambda x: x[2]):
    ru, rv = find(u), find(v)
    if ru == rv:
        continue
    p[ru] = rv
    cost += w

print(cost)