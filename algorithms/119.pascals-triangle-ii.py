#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        for i in range(1, rowIndex + 1):
            res = [a + b for a, b in zip([0] + res, res + [0])]
        return res
        
# @lc code=end

