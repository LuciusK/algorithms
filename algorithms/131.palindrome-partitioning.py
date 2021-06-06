#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        if n == 0:
            return res
        path = []
        self.dfs(s, n, 0, path, res)
        return res

    def dfs(self, s, n, start, path, res):
        if start == n:
            res.append(path[:])
            return 
        for i in range(start, n):
            if not self.check_pali(s, start, i):
                continue
            path.append(s[start:i + 1])
            self.dfs(s, n, i + 1, path, res)
            path.pop()
    
    def check_pali(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left = left + 1
            right = right - 1
        return True
        
# @lc code=end

