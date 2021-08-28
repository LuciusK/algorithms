class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.ans = [0] * len(nums)
        tmp = []
        for idx, val in enumerate(nums):
            tmp.append((val, idx))
        self.merge_sort(tmp)
        return self.ans
    
    def merge_sort(self, nums):
        if len(nums) < 2:
            return nums
        mid = len(nums) >> 1
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        return self.merge(left, right)
    
    def merge(self, left, right):
        res = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i][0] > right[j][0]:
                res.append(right[j])
                j += 1
            else:
                res.append(left[i])
                self.ans[left[i][1]] += j
                i += 1
        if i == len(left):
            res += right[j:]
        else:
            for k in range(i, len(left)):
                self.ans[left[k][1]] += j
            res += left[i:]
        return res