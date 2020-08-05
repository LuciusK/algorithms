#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, n = [], len(nums)
        if not nums or n < 3:
            return []
        nums.sort()
        for k in range(n - 2):
            if nums[k] > 0:
                return res
            if k > 0 and nums[k] == nums[k-1]:
                continue
            i = k + 1
            j = n - 1
            while i < j:
                if nums[k] + nums[i] + nums[j] == 0:
                    res.append([nums[k], nums[i], nums[j]])
                    while i < j and nums[i] == nums[i+1]:
                        i += 1
                    while i < j and nums[j] == nums[j-1]:
                        j -= 1
                    i += 1
                    j -= 1
                elif nums[k] + nums[i] + nums[j] > 0:
                    while i < j and nums[j] == nums[j-1]:
                        j -= 1
                    j -= 1
                else:
                    while i < j and nums[i] == nums[i+1]:
                        i += 1
                    i += 1
        return res


    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # sort 以后[nums[i], nums[j], nums[k]]就是有序的为以后判重方便
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if nums[k] + nums[i] + nums[j] == 0 and [nums[i], nums[j], nums[k]] not in res:
                        res.append([nums[i], nums[j], nums[k]])
        return res
    
    
# @lc code=end