#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if not s and len(p) == 1:
            return False
        
        nrow = len(s) + 1
        ncol = len(p) + 1

        dp = [[False for c in range(ncol)] for _ in range(nrow)]
        dp[0][0] = True
        dp[0][1] = False
        for c in range(2, ncol):
            j = c - 1
            if p[j] == "*":
                dp[0][c] = dp[0][c - 2]
        
        for r in range(1, nrow):
            i = r - 1
            for c in range(1, ncol):
                j = c - 1
                if s[i] == p[j] or p[j] == ".":
                    dp[r][c] = dp[r - 1][c - 1]
                elif p[j] == "*":
                    if p[j - 1] == s[i] or p[j - 1] == ".":
                        dp[r][c] = dp[r - 1][c] or dp[r][c - 2]
                    else:
                        dp[r][c] = dp[r][c - 2]
        return dp[-1][-1]

        
# @lc code=end

