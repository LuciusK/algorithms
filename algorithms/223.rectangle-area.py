#
# @lc app=leetcode id=223 lang=python3
#
# [223] Rectangle Area
#

# @lc code=start
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        if B >= H or C <= E or D <= F or A >= G:
            return (D - B) * (C - A) + (G - E) * (H - F)
        left = max(A, E)
        right = min(C, G)
        up = min(D, H)
        down = max(B, F)
        return (D - B) * (C - A) + (G - E) * (H - F) - (right - left) * (up - down)
        
# @lc code=end

