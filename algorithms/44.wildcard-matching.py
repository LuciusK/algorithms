#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        nrow = len(p) + 1
        ncol = len(s) + 1

        dp = [[False for _ in range(ncol)] for _ in range(nrow)]
        dp[0][0] = True

        if p.startswith("*"):
            dp[1] = [True] * ncol

        for m in range(1, nrow):
            path = False
            for n in range(1, ncol):
                if p[m - 1] == "*":
                    if dp[m - 1][0] == True:
                        dp[m] = [True] * ncol
                    if dp[m - 1][n] == True:
                        path = True
                    if path:
                        dp[m][n] = True
                elif p[m - 1] == "?" or p[m - 1] == s[n - 1]:
                    dp[m][n] = dp[m - 1][n - 1]
        return dp[-1][-1]

        
# @lc code=end

