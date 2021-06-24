class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getkelement(k):
            """
            - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
            - 这里的 "/" 表示整除
            - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
            - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
            - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
            - 这样 pivot 本身最大也只能是第 k-1 小的元素
            - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
            - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
            - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
            """
            idx1, idx2 = 0, 0
            while True:
                # 特殊情况
                if idx1 == m:
                    return nums2[idx2 + k - 1]
                if idx2 == n:
                    return nums1[idx1 + k - 1]
                if k == 1:
                    return min(nums1[idx1], nums2[idx2])
                # 正常情况
                newidx1 = min(idx1 + k // 2 - 1, m - 1)
                newidx2 = min(idx2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newidx1], nums2[newidx2]
                if pivot1 < pivot2:
                    k -= newidx1 - idx1 + 1
                    idx1 = newidx1 + 1
                else:
                    k -= newidx2 - idx2 + 1
                    idx2 = newidx2 + 1
        
        m, n = len(nums1), len(nums2)
        total = m + n 
        if total % 2 == 1:
            return getkelement((total + 1) // 2)
        else:
            return (getkelement(total // 2) + getkelement(total // 2 + 1)) / 2