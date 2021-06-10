#
# @lc app=leetcode id=132 lang=python3
#
# [132] Palindrome Partitioning II
#

# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
    	if n < 2:
    		return 0
    	dp = [i for i in range(n)]
    	check = [[False] * n for _ in range(n)]
    	for i in range(n):
    		check[i][i] = True
    	
    	for j in range(1, n):
    		for i in range(j):
    			check[i][j] = s[i] == s[j] and (j - i < 3 or check[i + 1][j - 1])
    	
    	for i in range(1, n):
    		if check[0][i]:
    			dp[i] = 0
    			continue
    		dp[i] = min([dp[j] + 1 for j in range(i) if check[j + 1][i]])
    	return dp[-1]
        
# @lc code=end

