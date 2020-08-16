#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x
        
        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

    def myPow2(self, x: float, n: int) -> float:
        if x == 0.0:
            return 0.0
        res = 1.0

        if n < 0:
            x, n = 1.0 / x, -n
        
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res

# @lc code=end

