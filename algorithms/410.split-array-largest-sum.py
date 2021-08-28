#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def check(x):
            total, cnt = 0, 1
            for num in nums:
                if total + num > x:
                    total = num
                    cnt += 1
                else:
                    total += num
            return cnt <= m
        
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) >> 1
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
        
# @lc code=end

