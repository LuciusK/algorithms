#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        ans = 0

        for j in range(len(s)):
            for i in range(j + 1):
                if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    ans += 1
        return ans
        
# @lc code=end

