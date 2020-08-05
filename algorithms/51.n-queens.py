#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        if n == 0:
            return res
        
        col = set()
        slave = set()
        master = set()
        stack = []

        self.__backtracking(0, n, col, slave, master, stack, res)
        return res
    
    def __backtracking(self, row, n, col, slave, master, stack, res):
        if row == n:
            board = self.__convert2board(stack, n)
            res.append(board)
            return
        
        for i in range(n):
            if i not in col and row + i not in slave and row - i not in master:
                stack.append(i)
                col.add(i)
                slave.add(row+i)
                master.add(row-i)

                self.__backtracking(row+1, n, col, slave, master, stack, res)

                master.remove(row-i)
                slave.remove(row+i)
                col.remove(i)
                stack.pop()
    
    def __convert2board(self, stack, n):
        return ["." * stack[i] + "Q" + "." * (n - stack[i] - 1) for i in range(n)]
        


        
# @lc code=end

