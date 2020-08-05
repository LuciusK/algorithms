#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, n = [], len(nums)
        if not nums or n < 4:
            return []
        nums.sort()
        for k in range(n - 3):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            for l in range(k+1, n-2):
                if l > k+1 and nums[l] == nums[l-1]:
                    continue
                i = l + 1
                j = n - 1
                while i < j:
                    if nums[k] + nums[l] + nums[i] + nums[j] == target:
                        res.append([nums[k], nums[l], nums[i], nums[j]])
                        while i < j and nums[i] == nums[i+1]:
                            i += 1
                        while i < j and nums[j] == nums[j-1]:
                            j -= 1
                        i += 1
                        j -= 1
                    elif nums[k] + nums[l] + nums[i] + nums[j] > target:
                        while i < j and nums[j] == nums[j-1]:
                            j -= 1
                        j -= 1
                    else:
                        while i < j and nums[i] == nums[i+1]:
                            i += 1
                        i += 1
        return res
# @lc code=end