#
# @lc app=leetcode id=363 lang=python3
#
# [363] Max Sum of Rectangle No Larger Than K
#

# @lc code=start
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        rows, cols, _max = len(matrix), len(matrix[0]), float('-inf')
        for l in range(cols):
            rowSum = [0] * rows
            for r in range(l, cols):
                for i in range(rows):
                    rowSum[i] += matrix[i][r]
                _max = max(_max, self.dpmax(rowSum, k))
                if _max == k:
                    return k
        return _max
    
    def dpmax(self, arr, k):
        rollSum = arr[0]
        rollMax = rollSum
        for i in range(1, len(arr)):
            if rollSum > 0:
                rollSum += arr[i]
            else:
                rollSum = arr[i]
            if rollSum > rollMax:
                rollMax = rollSum
        if rollMax <= k:
            return rollMax
        
        _max = float('-inf')
        for l in range(len(arr)):
            _sum = 0
            for r in range(l, len(arr)):
                _sum += arr[r]
                if _sum > _max and _sum <= k:
                    _max = _sum
                if _max == k:
                    return k
        return _max

        
# @lc code=end

