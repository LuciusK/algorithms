#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque()
        queue.append((root, [root.val]))
        res = []
        while queue:
            node, path = queue.popleft()
            if not node.left and not node.right and sum(path) == sum_:
                res.append(path)
            if node.left:
                queue.append((node.left, path + [node.left.val]))
            if node.right:
                queue.append((node.right, path + [node.right.val]))
        return res

    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        def helper(root, tmp, sum_):
            if not root:
                return
            if not root.left and not root.right and sum_ - root.val == 0:
                tmp += [root.val]
                res.append(tmp)
            helper(root.left, tmp + [root.val], sum_ - root.val)
            helper(root.right, tmp + [root.val], sum_ - root.val)
        res = []
        helper(root, [], sum_)
        return res
        
# @lc code=end

