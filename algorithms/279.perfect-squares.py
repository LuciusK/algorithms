#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i - j * j < 0:
                    break
                else:
                    dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[-1]
        
# @lc code=end

