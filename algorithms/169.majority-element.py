#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate

    def majorityElement3(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

    def majorityElement4(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key = counts.get)

        
# @lc code=end

