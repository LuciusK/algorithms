#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        left_min = self.minDepth(root.left)
        right_min = self.minDepth(root.right)

        if not root.left and not root.right:
            return 1
        elif not root.left or not root.right:
            return left_min + 1 if root.left else right_min + 1
        else:
            return min(left_min, right_min) + 1

        
# @lc code=end

