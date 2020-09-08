# 76
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start, left, right, minLen, match = 0, 0, 0, float('inf'), 0
        window = {}
        needs = dict((i, t.count(i)) for i in t)

        while right < len(s):
            c1 = s[right]
            if c1 in needs.keys():
                window[c1] = window.get(c1, 0) + 1
                if window[c1] == needs[c1]:
                    match += 1
            right += 1

            while match == len(needs):
                if right - left < minLen:
                    start = left
                    minLen = right - left
                c2 = s[left]
                if c2 in needs.keys():
                    window[c2] -= 1
                    if window[c2] < needs[c2]:
                        match -= 1
                left += 1
        return '' if minLen == float('inf') else s[start:start + minLen]

# 438
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        left, right, match = 0, 0, 0
        window = {}
        needs = dict((i, p.count(i)) for i in p)

        while right < len(s):
            c1 = s[right]
            if c1 in needs.keys():
                window[c1] = window.get(c1, 0) + 1
                if window[c1] == needs[c1]:
                    match += 1
            right += 1

            while match == len(needs):
                if right - left == len(p):
                    res.append(left)
                c2 = s[left]
                if c2 in needs.keys():
                    window[c2] -= 1
                    if window[c2] < needs[c2]:
                        match -= 1
                left += 1
        return res

# 3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right, left, res = 0, 0, 0
        window = {}

        while right < len(s):
            c1 = s[right]
            window[c1] = window.get(c1, 0) + 1
            right += 1
            while window[c1] > 1:
                c2 = s[left]
                window[c2] -= 1
                left += 1
            res = max(res, right - left)
        return res

# 567
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        needs = dict((i, s1.count(i)) for i in s1)
        right, left, match = 0, 0, 0
        window = {}

        while right < len(s2):
            c1 = s2[right]
            if c1 in needs.keys():
                window[c1] = window.get(c1, 0) + 1
                if window[c1] == needs[c1]:
                    match += 1
            right += 1

            while match == len(needs):
                if right - left == len(s1):
                    return True
                c2 = s2[left]
                if c2 in needs.keys():
                    window[c2] -= 1
                    if window[c2] < needs[c2]:
                        match -= 1
                left += 1
        return False

# 322
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

# 122
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i-1]
            if tmp > 0:
                profit += tmp
        return profit

    def maxProfit1(self, prices: List[int]) -> int:
        return sum(b - a for a, b in zip(prices, prices[1:]) if b > a)

    def maxProfit2(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp_i_0, dp_i_1 = 0, float('-inf')
        for i in range(n):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, tmp - prices[i])
        return dp_i_0
