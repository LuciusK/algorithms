#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left if node.left else node.right
            node = stack.pop()
            res.append(node.val)
            
            if stack and stack[-1].left == node:
                node = stack[-1].right
            else:
                node = None
        return res

# @lc code=end

