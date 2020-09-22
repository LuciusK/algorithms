#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s)))
    
    def findTheDifference1(self, s: str, t: str) -> str:
        from collections import Counter
        c1 = Counter(s)
        c2 = Counter(t)
        for i in range(ord("a"), ord("z") + 1):
            tmp = chr(i)
            if c2[tmp] - c1[tmp] == 1:
                return tmp
        
# @lc code=end

