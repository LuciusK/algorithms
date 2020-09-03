#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        fst = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < len(fst) and j < len(strs[i]):
                if fst[j] != strs[i][j]:
                    break
                j += 1
            if j == 0:
                return ""
            fst = fst[:j]
        return fst
        
# @lc code=end

