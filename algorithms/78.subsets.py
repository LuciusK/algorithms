#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsetsMOST(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        if size == 0:
            return []
        res = []
        for i in range(size + 1):
            self._dfs(nums, i, 0, [], res)
        return res

    def _dfs(self, nums, depth, begin, path, res):
        if len(path) == depth:
            res.append(path[:])
            return
        
        for i in range(begin, len(nums)):
            path.append(nums[i])
            self._dfs(nums, depth, i + 1, path, res)
            path.pop()
    
    def subsets2(self, nums: List[int]) -> List[List[int]]: # 参考
        size = len(nums)
        n = 1 << size
        res = []
        for i in range(n):
            cur = []
            for j in range(size):
                if i >> j & 1:
                    cur.append(nums[j])
            res.append(cur)
        return res


# @lc code=end

