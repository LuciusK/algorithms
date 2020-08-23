#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxarea = 0

        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    continue
                
                width = dp[i][j] = dp[i][j - 1] + 1 if j else 1

                for k in range(i, -1, -1):
                    width = min(width, dp[k][j])
                    maxarea = max(maxarea, width * (i - k + 1))
        return maxarea

    def maximalRectangle1(self, matrix: List[List[str]]) -> int:
        if not matrix: 
            return 0

        maxarea = 0
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
            maxarea = max(maxarea, self.leetcode84(dp))
        return maxarea

    def leetcode84(self, heights):
        maxarea = 0
        heights = [0] + heights + [0]
        # 先放入哨兵结点，在循环中就不用做非空判断
        size = len(heights)
        stack = [0]
        for i in range(1, size):
            while heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]
                cur_width = i - stack[-1] - 1
                maxarea = max(maxarea, cur_height * cur_width)
            stack.append(i)
        return maxarea


# @lc code=end

