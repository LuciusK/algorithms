class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        from collections import defaultdict, Counter

        edge_map = defaultdict(list)
        for edge in edges:
            edge_map[edge[0]].append(edge[1])
            edge_map[edge[1]].append(edge[0])

        def _dfs(i):
            visited.add(i)
            data = Counter({labels[i]: 1})
            for nxt in edge_map[i]:
                if nxt in visited:
                    continue

                data += _dfs(nxt)
            
            ans[i] = data[labels[i]]
            return data
        
        visited = set()
        ans = [1] * n
        _dfs(0)

        return ans