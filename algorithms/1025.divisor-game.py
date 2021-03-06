#
# @lc app=leetcode id=1025 lang=python3
#
# [1025] Divisor Game
#

# @lc code=start
class Solution:
    def divisorGame(self, N: int) -> bool:
        # 最终结果应该是占到 2 的赢，占到 1 的输；
        # 若当前为奇数，奇数的约数只能是奇数或者 1，因此下一个一定是偶数；
        # 若当前为偶数， 偶数的约数可以是奇数可以是偶数也可以是 1，因此直接减 1，则下一个是奇数；
        # 因此，奇则输，偶则赢。
        return N % 2 == 0
    
    def divisorGame1(self, N: int) -> bool:
        # 记dp[N]为黑板上数字为N的情况下,Alice的输赢情况， 如果Alice取了数字x, 那么显然
        # dp[N]与dp[N -x]输赢情况相反。x可以取的值很多，只要dp[N -xi]中任意一个为False, 那么dp[N]肯定为True, 否则dp[N]肯定为False
        dp = {}
        dp[1] = False
        dp[2] = True
        for i in range(3, N + 1):
            dp[i] = False
            for j in range(1, i):
                if i % j == 0 and dp[i - j] == False:
                    dp[i] = True
                    break
        return dp[N]
        
# @lc code=end

