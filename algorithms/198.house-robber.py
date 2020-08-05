#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for k in range(2, n + 1):
            dp[k] = max(dp[k - 1], dp[k - 2] + nums[k - 1])
        return dp[n]
    
    def rob1(self, nums: List[int]) -> int:
        prev = 0
        curr = 0
        for i in nums:
            # 循环开始时，curr 表示 dp[k-1]，prev 表示 dp[k-2]
            # dp[k] = max{dp[k-1], dp[k-2] + i}
            prev, curr = curr, max(curr, prev + i)
            # 循环结束时，curr 表示 dp[k]，prev 表示 dp[k-1]
        return curr

        
# @lc code=end

