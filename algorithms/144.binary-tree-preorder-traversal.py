#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def helper(root):
            if not root: return
            res.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return res

    def preorderTraversal1(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        while root or stack:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop().right
        return res

    


# @lc code=end

