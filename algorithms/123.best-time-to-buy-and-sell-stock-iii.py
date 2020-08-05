#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        k = 2
        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n)]
        for i in range(0, n):
            for j in range(k, -1, -1):
                if i == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[0]
                elif j == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = float('-inf')
                else:
                    dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                    dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        
        return dp[-1][k][0]
    
    def maxProfit1(self, prices: List[int]) -> int:
        dp_i10, dp_i11 = 0, float('-inf')
        dp_i20, dp_i21 = 0, float('-inf')

        for price in prices:
            dp_i20 = max(dp_i20, dp_i21 + price)
            dp_i21 = max(dp_i21, dp_i10 - price)
            dp_i10 = max(dp_i10, dp_i11 + price)
            dp_i11 = max(dp_i11, -price)
        
        return dp_i20


        
# @lc code=end

