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
        n = len(nums)
        tail = [nums[0]]
        dp = [1] * n
        for i in range(1, n):
            if nums[i] > tail[-1]:
                tail.append(nums[i])
                dp[i] = len(tail)
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
            dp[i] = left + 1
        
        res = []
        j = len(tail)
        i = n - 1
        while j >= 1 and i >= 0:
            if dp[i] == j:
                res.append(nums[i])
                j -= 1
            i -= 1
        return res[::-1]
        
# @lc code=end

