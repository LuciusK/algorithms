#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution: # dp[i-1][j-1] 表示替换操作，dp[i-1][j] 表示删除操作，dp[i][j-1] 表示插入操作
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for j in range(1, n2 + 1):
            dp[0][j] = dp[0][j - 1] + 1
        for i in range(1, n1 + 1):
            dp[i][0] = dp[i - 1][0] + 1
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        return dp[-1][-1]

        
# @lc code=end

