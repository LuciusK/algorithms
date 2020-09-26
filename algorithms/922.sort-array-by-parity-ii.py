#
# @lc app=leetcode id=922 lang=python3
#
# [922] Sort Array By Parity II
#

# @lc code=start
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        n = len(A)
        ans = [None] * n
        
        ans[::2] = (x for x in A if x % 2 == 0)
        ans[1::2] = (x for x in A if x % 2 == 1)
        return ans

    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A
        
# @lc code=end

