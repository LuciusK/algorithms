# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        p = root
        pre = float('-inf')
        minval = float('inf')
        stack = []
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            minval = min(minval, p.val - pre)
            pre = p.val
            p = p.right
        return minval