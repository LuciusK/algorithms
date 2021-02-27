#
# @lc app=leetcode id=552 lang=python3
#
# [552] Student Attendance Record II
#

# @lc code=start
class Solution:
    def checkRecord(self, n: int) -> int:
        _Mod = 1000000007
        dp = [[[0 for i in range(3)] for i in range(2)] for i in range(n + 1)]
        dp[1][1][0] = 1
        dp[1][0][1] = 1
        dp[1][0][0] = 1
        for i in range(2, n + 1):
            # +P
            dp[i][0][0] = (dp[i - 1][0][0] + dp[i - 1][0][1] + dp[i - 1][0][2]) % _Mod
            dp[i][1][0] = (dp[i - 1][1][0] + dp[i - 1][1][1] + dp[i - 1][1][2]) % _Mod
            # +L
            dp[i][0][1] = dp[i - 1][0][0]
            dp[i][0][2] = dp[i - 1][0][1]
            dp[i][1][1] = dp[i - 1][1][0]
            dp[i][1][2] = dp[i - 1][1][1]
            # +A
            dp[i][1][0] = (dp[i - 1][0][0] + dp[i - 1][0][1] + dp[i - 1][0][2]) % _Mod

        return (dp[n][0][0] + dp[n][0][1] + dp[n][0][2] + dp[n][1][0] + dp[n][1][1] + dp[n][1][2]) % _Mod

    def checkRecord1(self, n: int) -> int:
        _Mod = 1000000007
        dp00 = dp01 = dp10 = 1
        dp11 = dp02 = dp12 = 0
        for i in range(2, n + 1):
            t00, t01, t02, t10, t11, t12 = dp00, dp01, dp02, dp10, dp11, dp12
            
            dp00 = (t00 + t01 + t02) % _Mod
            dp10 = (t10 + t11 + t12) % _Mod

            dp01 = t00
            dp02 = t01
            dp11 = t10
            dp12 = t11

            dp10 += (t00 + t01 + t02) % _Mod
        
        return (dp00 + dp01 + dp02 + dp10 + dp11 + dp12) % _Mod
        
# @lc code=end

