#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        size = len(nums)
        if size == 0:
            return 0
        
        if nums[size - 1] < target:
            return size
        
        left = 0
        right = size - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
        
# @lc code=end

