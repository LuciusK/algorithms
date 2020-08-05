#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    def invertTree1(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        queue = [root]
        while queue:
            tmp = queue.pop(0)
            tmp.left, tmp.right = tmp.right, tmp.left

            if tmp.left:
                queue.append(tmp.left)
            if tmp.right:
                queue.append(tmp.right)
        return root
        
# @lc code=end

