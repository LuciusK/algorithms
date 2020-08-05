#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [1] + [0] * n #最初的初始值，防止第一列或者第一行有障碍
        for i in range(0, m):
            for j in range(0, n):
                dp[j] = 0 if obstacleGrid[i][j] else dp[j] + dp[j-1] #第一列第一行也能用转移公式了
        
        return dp[-2]

# @lc code=end

