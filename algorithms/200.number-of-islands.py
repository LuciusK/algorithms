#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                if not marked[i][j] and grid[i][j] == '1':
                    count += 1
                    self._dfs(grid, i, j, m, n, marked)
        return count

    def _dfs(self, grid, i, j, m, n, marked):
        marked[i][j] = True
        for direction in self.directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if 0 <= new_i < m and 0 <= new_j < n and not marked[new_i][new_j]\
                and grid[new_i][new_j] == '1':
                self._dfs(grid, new_i, new_j, m, n, marked)
    
    def numIslands1(self, grid: List[List[str]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        marked = [[False for _ in range(n)] for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):
                if not marked[i][j] and grid[i][j] == '1':
                    count += 1
                    queue = deque()
                    queue.append((i, j))
                    marked[i][j] = True
                    
                    while queue:
                        cur_x, cur_y = queue.popleft()
                        for direction in self.directions:
                            new_i = cur_x + direction[0]
                            new_j = cur_y + direction[1]
                            if 0 <= new_i < m and 0 <= new_j < n and not marked[new_i][new_j] \
                                and grid[new_i][new_j] == '1':
                                queue.append((new_i, new_j))
                                marked[new_i][new_j] = True
        return count

    def numIslands2(self, grid: List[List[str]]) -> int:
        
        class UnionFind:

            def __init__(self, n):
                self.count = n
                self.parent = [i for i in range(n)]
                self.rank = [1 for _ in range(n)]

            def get_count(self):
                return self.count
            
            def find(self, p):
                while p != self.parent[p]:
                    self.parent[p] = self.parent[self.parent[p]]
                    p = self.parent[p]
                return p
            
            def is_connect(self, p, q):
                return self.find(p) == self.find(q)
            
            def union(self, p, q):
                p_root = self.find(p)
                q_root = self.find(q)
                if p_root == q_root:
                    return 
                
                if self.rank[p_root] > self.rank[q_root]:
                    self.parent[q_root] = p_root
                elif self.rank[p_root] < self.rank[q_root]:
                    self.parent[p_root] = q_root
                else:
                    self.parent[q_root] = p_root
                    self.rank[p_root] += 1
                
                self.count -= 1
        
        row = len(grid)

        if row == 0:
            return 0
        col = len(grid[0])

        def get_index(x, y):
            return x * col + y
        
        directions = [(1, 0), (0, 1)]
        dummy_node = row * col

        uf = UnionFind(dummy_node + 1)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    uf.union(get_index(i, j), dummy_node)
                if grid[i][j] == '1':
                    for direction in directions:
                        new_x = i + direction[0]
                        new_y = j + direction[1]
                        if new_x < row and new_y < col and grid[new_x][new_y] == '1':
                            uf.union(get_index(i, j), get_index(new_x, new_y))
        
        return uf.get_count() - 1


# @lc code=end

