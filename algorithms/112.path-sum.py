#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

    def hasPathSum1(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        queue = collections.deque()
        queue.append((root, root.val))
        while queue:
            node, path = queue.popleft()
            if not node.left and not node.right and path == sum:
                return True
            if node.left:
                queue.append((node.left, path + node.left.val))
            if node.right:
                queue.append((node.right, path + node.right.val))
        return False

# @lc code=end

