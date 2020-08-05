#
# @lc app=leetcode id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        traversal = [root.val]
        for child in root.children:
            traversal.extend(self.preorder(child))
        return traversal

    def preorder1(self, root: 'Node') -> List[int]:
        if not root: 
            return []
        stack = [root]
        res = []
        while stack:
            temp = stack.pop()
            res.append(temp.val)
            stack.extend(reversed(temp.children))
        return res


# @lc code=end

