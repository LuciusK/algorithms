#
# @lc app=leetcode id=493 lang=python3
#
# [493] Reverse Pairs
#

# @lc code=start
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        tmp = [0] * n
        return self.merge_sort(nums, tmp, 0, n - 1)

    def merge_sort(self, nums, tmp, left, right):
        if left >= right:
            return 0
        mid = (left + right) >> 1
        res = self.merge_sort(nums, tmp, left, mid) + \
              self.merge_sort(nums, tmp, mid + 1, right) + \
              self.find_reverse(nums, left, right)
        i, j, k = left, mid + 1, left
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                tmp[k] = nums[i]
                i += 1
            else:
                tmp[k] = nums[j]
                j += 1
            k += 1
        while i <= mid:
            tmp[k] = nums[i]
            i += 1
            k += 1
        while j <= right:
            tmp[k] = nums[j]
            j += 1
            k += 1
        nums[left:right + 1] = tmp[left:right + 1]
        return res

    def find_reverse(self, nums, left, right):
        res, mid = 0, (left + right) >> 1
        j = mid + 1
        for i in range(left, mid + 1):
            while j <= right and nums[i] > 2 * nums[j]:
                res += mid + 1 - i
                j += 1
        return res


        
# @lc code=end

