#
# @lc app=leetcode id=403 lang=python3
#
# [403] Frog Jump
#

# @lc code=start
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        from functools import lru_cache
        end = stones[-1]
        s = set(stones)
        @lru_cache(None)
        def helper(start, jump):
            if start == end:
                return True
            for j in [jump - 1, jump, jump + 1]:
                if j <= 0:
                    continue
                if start + j in s and helper(start + j, j):
                    return True
            return False
        return helper(0, 0)
    
    def canCross1(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = [set() for _ in range(n)]
        dp[0].add(0)
        for i in range(n):
            cur = stones[i]
            for j in range(i):
                need = cur - stones[j]
                if need - 1 in dp[j] or need + 1 in dp[j] or need in dp[j]:
                    dp[i].add(need)
        return len(dp[-1]) > 0
        
# @lc code=end

