#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res
    
    def permute1(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, hash_set, path, res):
            if depth == size:
                res.append(path[:])
                return

            for i in range(size):
                if not nums[i] in hash_set:
                    hash_set.add(nums[i])
                    path.append(nums[i])
                
                    dfs(nums, size, depth + 1, hash_set, path, res)
                    path.pop()
                    hash_set.remove(nums[i])

        size = len(nums)
        if size == 0:
            return []
        res = []
        path = []
        hash_set = set()
        dfs(nums, size, 0, hash_set, path, res)
        return res
        
# @lc code=end

