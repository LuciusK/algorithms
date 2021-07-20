# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = root.val
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left) # 左子树的最大路径和
            right = dfs(root.right) # 右子树的最大路径和

            innermax = left + root.val + right # 当前子树内部的最大路径和
            self.res = max(self.res, innermax) # 更新最大记录

            outputmax = root.val + max(left, right)
            return max(0, outputmax)
        
        dfs(root)
        return self.res