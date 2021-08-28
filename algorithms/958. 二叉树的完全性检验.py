# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = []
        pre = root
        queue.append(root)
        while queue:
            cur = queue.pop(0)
            if pre is None and cur != None:
                return False
            if cur:
                queue.append(cur.left)
                queue.append(cur.right)
            pre = cur
        return True