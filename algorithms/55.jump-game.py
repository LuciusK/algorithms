#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums == [0]:
            return True
        maxDist = 0
        end_index = len(nums) - 1
        for i, jump in enumerate(nums):
            if maxDist >= i and i + jump > maxDist:#最远距离大过终点index
                maxDist = i + jump
                if maxDist >= end_index:
                    return True
        
        return False

        
# @lc code=end

