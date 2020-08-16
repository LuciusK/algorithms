#
# @lc app=leetcode id=493 lang=python3
#
# [493] Reverse Pairs
#

# @lc code=start
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, l, r):
        if l >= r:
            return 0
        mid = l + ((r - l) >> 1)
        cnt = self.mergeSort(nums, l, mid) + self.mergeSort(nums, mid + 1, r)
        cache = [0] * (r - l + 1)
        i, t, c = l, l, 0
        for j in range(mid + 1, r + 1):
            while t <= mid and (nums[t] + 1) >> 1 <= nums[j]:
                t += 1
            while i <= mid and nums[i] <= nums[j]:
                cache[c] = nums[i]
                c += 1
                i += 1
            cache[c] = nums[j]
            c += 1
            cnt += mid - t + 1
        while i <= mid:
            cache[c] = nums[i]
            c += 1
            i += 1
        nums[l:r + 1] = cache
        return cnt


        
# @lc code=end

