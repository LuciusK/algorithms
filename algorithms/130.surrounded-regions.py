#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])

        def dfs(i, j):
            board[i][j] = 'B'
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                tmp_i = i + x
                tmp_j = j + y
                if 0 <= tmp_i < row and 0 <= tmp_j < col and board[tmp_i][tmp_j] == 'O':
                    dfs(tmp_i, tmp_j)
        
        for j in range(col):
            if board[0][j] == 'O':
                dfs(0, j)
            if board[row - 1][j] == 'O':
                dfs(row - 1, j)
        
        for i in range(row):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][col - 1] == 'O':
                dfs(i, col - 1)
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'B':
                    board[i][j] = 'O'
    
    def solve1(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])

        def bfs(i, j):
            queue = []
            queue.append((i, j))
            while queue:
                i, j = queue.pop(0)
                if 0 <= i < row and 0 <= j < col and board[i][j] == 'O':
                    board[i][j] = 'B'
                    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        queue.append((i + x, j + y))
        
        for j in range(col):
            if board[0][j] == 'O':
                bfs(0, j)
            if board[row - 1][j] == 'O':
                bfs(row - 1, j)
        
        for i in range(row):
            if board[i][0] == 'O':
                bfs(i, 0)
            if board[i][col - 1] == 'O':
                bfs(i, col - 1)
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'B':
                    board[i][j] = 'O'
    
    def solve2(self, board: List[List[str]]) -> None:
        f = {}
        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]
        def union(x, y):
            f[find(y)] = find(x)
        
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])

        dummy = row * col
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O': # O以外的全部按照原样，i = p[i]
                    if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                        union(dummy, i * col + j)
                    else:
                        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if board[i + x][j + y] == "O":
                                union(i * col + j, (i + x) * col + (j + y))

        for i in range(row):
            for j in range(col):
                if find(dummy) == find(i * col + j):
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"


        
# @lc code=end

