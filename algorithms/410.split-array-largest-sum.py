#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)
        def test_mid(mid):
            num = 1
            s = 0
            for i in nums:
                if s + i > mid:
                    s = i
                    num += 1
                else:
                    s += i
            return num > m
        
        while left < right:
            mid = (left + right) // 2
            if_right = test_mid(mid)
            if if_right:
                left = mid + 1
            else:
                right = mid
        return left
        
# @lc code=end

