#
# @lc app=leetcode id=887 lang=python3
#
# [887] Super Egg Drop
#

# @lc code=start
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = dict()
        def dp(K, N):
            if K == 1: return N 
            if N == 0: return 0
            if (K, N) in memo:
                return memo[(K, N)]
            
            res = float('inf')
            
            # for i in range(1, N + 1):
            # 	res = min(res, max(dp(K, N - i), dp(K - 1, i - 1)) + 1)
            
            lo, hi = 1, N
            while lo <= hi:
                mid = (lo + hi) // 2
                broken = dp(K - 1, mid - 1)
                not_broken = dp(K, N - mid)
                if broken > not_broken:
                    hi = mid - 1
                    res = min(res, broken + 1)
                else:
                    lo = mid + 1
                    res = min(res, not_broken + 1)
            
            memo[(K, N)] = res
            return res 
        return dp(K, N)

        
# @lc code=end

