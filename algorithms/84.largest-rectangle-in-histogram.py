#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    #暴力法
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        n = len(heights)
        for i in range(n):
            left_i = i
            right_i = i
            while left_i >= 0 and heights[left_i] >= heights[i]:
                left_i -= 1
            while right_i < n and heights[right_i] >= heights[i]:
                right_i += 1
            res = max(res, (right_i - left_i - 1) * heights[i])
        return res

#该例子也可以加优化
    def largestRectangleArea2(self, heights: List[int]) -> int:
        res = 0
        heights = [0] + heights + [0]
        # 先放入哨兵结点，在循环中就不用做非空判断
        size = len(heights)
        stack = [0]
        for i in range(1, size):
            while heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]
                cur_width = i - stack[-1] - 1
                res = max(res, cur_height * cur_width)
            stack.append(i)
        return res
# @lc code=end

