#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(s in J for s in S)
    
    def numJewelsInStones1(self, J: str, S: str) -> int:
        Jset = set(J)
        return sum(s in Jset for s in S)

# @lc code=end

