#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        def maxProfit_k_inf(prices):
            dp_i_0, dp_i_1 = 0, float('-inf')
            for price in prices:
                tmp = dp_i_0
                dp_i_0 = max(dp_i_0, dp_i_1 + price)
                dp_i_1 = max(dp_i_1, tmp - price)
            return dp_i_0
        
        if k >= n / 2:
            return maxProfit_k_inf(prices)
        
        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n)]

        for i in range(n):
            for j in range(k, 0, -1):
                if i == 0:
                    dp[0][j][0] = 0
                    dp[0][j][1] = -prices[0]
                    continue
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        
        return dp[-1][k][0]
    
    def maxProfit1(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        if k >= n / 2:
            return sum(b - a for a, b in zip(prices, prices[1:]) if b > a)
        
        dp = [[0 if i == 0 else -prices[0] for i in range(2)] for _ in range(k + 1)]
        for i in range(1, n):
            for j in range(k, 0, -1):
                dp[j][0] = max(dp[j][0], dp[j][1] + prices[i])
                dp[j][1] = max(dp[j][1], dp[j - 1][0] - prices[i])
        
        return dp[k][0]


        
# @lc code=end

