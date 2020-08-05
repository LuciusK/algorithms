#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        dp = [0 for _ in range(size)]

        dp[0] = nums[0]
        for i in range(1, size):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)

    def maxSubArray1(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        
        pre = nums[0]
        res = pre
        for i in range(1, size):
            pre = max(nums[i], pre + nums[i])
            res = max(pre, res)
        
        return res
    
    def maxSubArray2(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        return self.__max_sub_array(nums, 0, size - 1)
    
    def __max_sub_array(self, nums, left, right):
        if left == right:
            return nums[left]
        mid = (left + right) >> 1
        return max(self.__max_sub_array(nums, left, mid),
                    self.__max_sub_array(nums, mid + 1, right),
                    self.__max_cross_array(nums, left, mid, right))
    
    def __max_cross_array(self, nums, left , mid, right):
        left_sum_max = 0
        start_left = mid - 1
        s1 = 0
        while start_left >= left:
            s1 += nums[start_left]
            left_sum_max = max(left_sum_max, s1)
            start_left -= 1
        
        right_sum_max = 0
        start_right = mid + 1
        s2 = 0
        while start_right <= right:
            s2 += nums[start_right]
            right_sum_max = max(right_sum_max, s2)
            start_right += 1
        return left_sum_max + nums[mid] + right_sum_max


        
# @lc code=end

