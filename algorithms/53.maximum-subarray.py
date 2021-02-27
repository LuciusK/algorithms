#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        dp = [0 for _ in range(size)]

        dp[0] = nums[0]
        for i in range(1, size):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)

    def maxSubArray1(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        
        pre = nums[0]
        res = pre
        for i in range(1, size):
            pre = max(nums[i], pre + nums[i])
            res = max(pre, res)
        
        return res
    


        
# @lc code=end

