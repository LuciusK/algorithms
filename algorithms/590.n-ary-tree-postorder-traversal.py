#
# @lc app=leetcode id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
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
    def postorder1(self, root: 'Node') -> List[int]:
        res = []
        if root is None: 
            return res

        def recursion(root, res):
            for child in root.children:
                recursion(child, res)
            res.append(root.val)

        recursion(root, res)
        return res

    def postorder(self, root: 'Node') -> List[int]:
        res = []
        if root is None: 
            return res

        stack = [root]
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            stack.extend(cur.children)

        return res[::-1]


# @lc code=end

