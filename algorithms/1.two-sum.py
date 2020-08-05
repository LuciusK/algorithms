#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum68ms(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i
    
    """O(n^2)"""
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if nums[x] + nums[y] == target:
                    return [x, y]
                    break
                else:
                    continue
    
    """O(n)"""
    def twoSum1132ms(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for x in range(n):
            a = target - nums[x]
            if a in nums:
                y = nums.index(a)
                if x == y:
                    continue
                else:
                    return [x, y]
                    break
            else:
                continue
# @lc code=end 