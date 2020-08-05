#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start  
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        s1, s2 = 0, 0
        max1, max2 = 0, 0
        for i in range(n):
            if height[i] > max1:
                max1 = height[i]
            if height[n-i-1] > max2:
                max2 = height[n-i-1]
            s1 += max1
            s2 += max2
        
        res = s1 + s2 - max1 * n - sum(height)
        return res

    # def trap1(self, height: List[int]) -> int:和下面的思路一样
    #     if not height: return 0
    #     left = 0
    #     right = len(height) - 1
    #     res = 0

    #     left_max = height[left]
    #     right_max = height[right]
    #     while left < right:
    #         if height[left] < height[right]:
    #             if left_max > height[left]:
    #                 res += left_max - height[left]
    #             else:
    #                 left_max = height[left]
    #             left += 1
    #         else:
    #             if right_max > height[right]:
    #                 res += right_max - height[right]
    #             else:
    #                 right_max = height[right]
    #             right -= 1
    #     return res

    def trap2(self, height: List[int]) -> int:
        n = len(height)
        if n == 0: 
            return 0
        right = [0] * n
        right[-1] = height[-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])
        res = 0
        cur = height[0]
        for i in range(1, n-1):
            cur = max(height[i], cur)
            res += min(cur, right[i]) - height[i]
        
        return res

    def trapfast(self, height: List[int]) -> int:
        if not height: 
            return 0
        n = len(height)
        stack = []
        res = 0
        for i in range(n):
            while stack and height[stack[-1]] < height[i]:
                tmp = stack.pop()
                if not stack: 
                    break
                res += (min(height[i], height[stack[-1]]) - height[tmp]) * (i - stack[-1] - 1)
            stack.append(i)
        return res

    def trap3(self, height: List[int]) -> int:
        ans = 0
        for i in range(len(height)):
            max_left, max_right = 0, 0
            for j in range(0, i):
                max_left = max(max_left, height[j])
            for j in range(i, len(height)):
                max_right = max(max_right, height[j])
            if min(max_left, max_right) > height[i]:
                ans += min(max_left, max_right) - height[i]
        
        return ans

# @lc code=end

