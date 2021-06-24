# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        cur_level = [root]
        res = []
        while cur_level:
            next_level = []
            res.append(cur_level[-1].val)
            for node in cur_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            cur_level = next_level
        return res
    
    def rightSideView1(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(root, depth):
            if not root:
                return
            if len(res) == depth:
                res.append(0)
            res[depth] = root.val
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        dfs(root, 0)
        return res