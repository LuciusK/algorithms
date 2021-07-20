#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k <= 0 or k > len(nums):
            return
        heap = self.build_heap(nums[:k])
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heap[0] = nums[i]
                self.sink(heap, 0)
        return heap[0]
    
    def sink(self, array, k):
        n = len(array)
        l = 2 * k + 1
        r = 2 * k + 2
        if l >= n:
            return
        min_i = l 
        if r < n and array[r] < array[l]:
            min_i = r 
        if array[min_i] < array[k]:
            array[min_i], array[k] = array[k], array[min_i]
            self.sink(array, min_i)
    
    def build_heap(self, array):
        n = len(array)
        for i in range(n // 2 - 1, -1, -1):
            self.sink(array, i)
        return array
    
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

