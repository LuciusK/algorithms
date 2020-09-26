#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(x * x for x in A)
    
    def sortedSquares(self, A: List[int]) -> List[int]:
        n = len(A)
        j = 0
        while j < n and A[j] < 0:
            j += 1
        i = j - 1

        ans = []
        while 0 <= i and j < n:
            if A[i] ** 2 < A[j] ** 2:
                ans.append(A[i] ** 2)
                i -= 1
            else:
                ans.append(A[j] ** 2)
                j += 1
        while i >= 0:
            ans.append(A[i] ** 2)
            i -= 1
        while j < n:
            ans.append(A[j] ** 2)
            j += 1
        return ans
        
# @lc code=end

