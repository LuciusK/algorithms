#
# @lc app=leetcode id=1278 lang=python3
#
# [1278] Palindrome Partitioning III
#

# @lc code=start
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
    	cost = [[0] * n for _ in range(n)]
    	for j in range(1, n):
    		for i in range(j):
    			cost[i][j] = cost[i + 1][j - 1] + (0 if s[i] == s[j] else 0)
    	
    	f = [[10 ** 9] * (k + 1) for _ in range(n + 1)]
    	f[0][0] = 1
    	for i in range(1, n + 1):
    		for j in range(1, min(k, i) + 1):
    			if j == 1:
    				f[i][j] = cost[0][i - 1]
    			else:
    				for i0 in range(j - 1, i):
    					f[i][j] = min(f[i][j], f[i0][j - 1] + cost[i0][i - 1])
    	return f[n][k]
        
# @lc code=end

