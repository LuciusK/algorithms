#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0 for i in range(cols + 1)] for j in range(rows + 1)]

        maxSide = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1
                    maxSide = max(maxSide, dp[i + 1][j + 1])
        return maxSide * maxSide
# @lc code=end

