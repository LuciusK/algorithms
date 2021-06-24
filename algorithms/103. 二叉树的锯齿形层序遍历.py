# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        depth = 0
        cur_level = [root]
        while cur_level:
            tmp = []
            next_level = []
            for node in cur_level:
                tmp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if depth % 2 == 1:
                res.append(tmp[::-1])
            else:
                res.append(tmp)
            depth += 1
            cur_level = next_level
        return res
    
    def zigzagLevelOrder1(self, root: TreeNode) -> List[List[int]]:
        def dfs(root, depth, res):
            if not root:
                return
            if len(res) == depth:
                res.append([])
            if depth % 2 == 1:
                res[depth].insert(0, root.val)
            else:
                res[depth].append(root.val)
            if root.left:
                dfs(root.left, depth + 1, res)
            if root.right:
                dfs(root.right, depth + 1, res)
        
        res = []
        dfs(root, 0, res)
        return res