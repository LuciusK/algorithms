#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        def my_rob(nums):
            prev, curr = 0, 0
            for i in nums:
                prev, curr = curr, max(curr, prev + i)
            return curr
        
        return max(my_rob(nums[:-1]), my_rob(nums[1:])) if len(nums) != 1 else nums[0]
        
# @lc code=end

