"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        self.res = 0
        def dfs(root):
            if not root:
                return 0
            max_path1, max_path2 = 0, 0
            for child in root.children:
                max_path = dfs(child)
                if max_path > max_path1:
                    max_path2 = max_path1
                    max_path1 = max_path
                elif max_path > max_path2:
                    max_path2 = max_path
            self.res = max(self.res, max_path1 + max_path2)
            return max(max_path1, max_path2) + 1
            
        dfs(root)
        return self.res