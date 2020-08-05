#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        p = 0
        q = 1
        while q < len(nums):
            if nums[p] != nums[q]:
                if q - p > 1:
                    nums[p+1] = nums[q]
                p += 1
            q += 1
        
        return p + 1
# @lc code=end

