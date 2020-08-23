#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

    def lengthOfLIS1(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 2:
            return size

        tail = [nums[0]]
        for i in range(1, size):
            if nums[i] > tail[-1]:
                tail.append(nums[i])
                continue

            left = 0
            right = len(tail) - 1
            while left < right:
                mid = (left + right) >> 1
                if tail[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            
            tail[left] = nums[i]
        return len(tail)
        
# @lc code=end

