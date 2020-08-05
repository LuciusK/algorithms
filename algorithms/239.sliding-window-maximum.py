#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0:
            return []
        
        return [max(nums[i:i+k]) for i in range(n-k+1)]

from collections import deque
    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        res = []
        bigger = deque()
        for i, n in enumerate(nums):
            # make sure the rightmost one is the smallest
            while bigger and nums[bigger[-1]] < n:
                bigger.pop()
            
            # add in
            bigger += [i]

            # make sure the leftmost one is in-bound
            if i - bigger[0] >= k:
                bigger.popleft()
            
            # if i + 1 < k, then we are initializing the bigger array
            if i + 1 >= k:
                res.append(nums[bigger[0]])
        
        return res

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        left = [0] * n
        left[0] = nums[0]
        right = [0] * n
        right[n-1] = nums[n-1]

        for i in range(1, n):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i-1], nums[i])
        
            j = n - i - 1
            if (j+1) % k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(right[j+1], nums[j])
            
        output = []
        for i in range(n-k+1):
            output.append(max(left[i+k-1], right[i]))

        return output

# @lc code=end

