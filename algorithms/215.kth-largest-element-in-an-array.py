#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        size = len(nums)
        if k > size:
            raise Exception("程序出错")
        
        L = []
        for i in range(k):
            heapq.heappush(L, nums[i])
        for i in range(k, size):
            top = L[0]
            if nums[i] > top:
                heapq.heapreplace(L, nums[i])
        return L[0]

    def findKthLargest1(self, nums: List[int], k: int) -> int:    
        import random
        n = len(nums)
        target = n - k
        left = 0
        right = n - 1
        while True:
            index = self.partition(nums, left, right)
            if index == target:
                return nums[target]
            elif index < target:
                left = index + 1
            else:
                right = index - 1
    
    def partition(self, nums, left, right):
        random_index = random.randint(left, right)
        nums[random_index], nums[left] = nums[left], nums[random_index]

        pivot = nums[left]
        j = left
        for i in range(left + 1, right + 1):
            if nums[j] < pivot:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[left], nums[j] = nums[j], nums[left]
        return j
        
# @lc code=end

