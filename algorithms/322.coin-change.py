#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        import functools
        @functools.lru_cache(amount)
        def dp(rem):
            if rem < 0:#除不尽的返回负值
                return -1
            if rem == 0: #确保除尽
                return 0
            mini = int(1e9)
            for coin in self.coins:
                res = dp(rem - coin)#自顶向下
                if res >= 0 and res < mini:#此处确保mini是最小
                    mini = res + 1
            return mini if mini < int(1e9) else -1#确保除不尽的始终返回为-1
        
        self.coins = coins
        if amount < 1: 
            return 0
        return dp(amount)
    
    def coinChange1(self, coins: List[int], amount: int) -> int:#解法可以与跳到目的的题目很像，但却不能用，很麻烦
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:#对每个coin进行遍历
            for x in range(coin, amount + 1):#对coin从小到大更新，小的就更新，一样的或者大的就不更新
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
    

        
# @lc code=end

