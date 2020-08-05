#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return
        
        n = len(triangle)
        for row in range(n - 2, -1, -1):
            for col in range(len(triangle[row])):
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
        
        return triangle[0][0]

    def minimumTotal1(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return
        
        res = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                res[j] = min(res[j], res[j + 1]) + triangle[i][j]

        return res[0]


# @lc code=end

