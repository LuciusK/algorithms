#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:#解法可以与跳到目的的题目很像，但却不能用，很麻烦
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:#对每个coin进行遍历
            for x in range(coin, amount + 1):#对coin从小到大更新，小的就更新，一样的或者大的就不更新
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

# @lc code=end

