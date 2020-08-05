#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        nums1[:m+n] = sorted(nums1[:m] + nums2)

    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if len(nums1) > m + n:
            numsleft = nums1[m+n:]
        else:
            numsleft = []
        nums1_copy = nums1[:m]
        nums1[:] = []

        p1 = 0
        p2 = 0

        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1
        
        if p1 < m:
            nums1[p1+p2:] = nums1_copy[p1:] + numsleft
        if p2 < n:
            nums1[p1+p2:] = nums2[p2:] + numsleft

    def merge3(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1
        p2 = n - 1

        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                 nums1[p] = nums2[p2]
                 p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        
        nums1[:p2+1] = nums2[:p2+1]


# @lc code=end

