#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height, right_height) + 1
    
    
    def maxDepth1(self, root: TreeNode) -> int:
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack:
            curren_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, curren_depth)
                stack.append((curren_depth+1, root.left))
                stack.append((curren_depth+1, root.right))
        
        return depth

        
# @lc code=end

