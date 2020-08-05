#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs36ms(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n):
            a, b = b, a+b
        return a
    
    def climbStairs36ms(self, n: int) -> int:
        dp = {}
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    def climbStairs2(self, n: int) -> int:
        import math
        sqrt5 = 5 ** 0.5
        fibin = math.pow((1+sqrt5)/2, n+1) - math.pow((1-sqrt5)/2, n+1)
        return int(fibin/sqrt5)
# @lc code=end