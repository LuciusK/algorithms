import collections
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        self.res = 0
        n = len(edges) + 1
        adj = collections.defaultdict(list)
        visited = dict()
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            visited[a] = False
            visited[b] = False
        
        self.dfs(adj, 0, visited)
        return self.res
        
    def dfs(self, adj, index, visited):
        visited[index] = True
        max_path1, max_path2 = 0, 0 
        for child in adj[index]:
            if not visited[child]:
                max_path = self.dfs(adj, child, visited)
                if max_path > max_path1:
                    max_path2 = max_path1
                    max_path1 = max_path
                elif max_path > max_path2:
                    max_path2 = max_path
        visited[index] = False
        self.res = max(self.res, max_path1 + max_path2)
        return max(max_path1, max_path2) + 1