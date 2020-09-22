#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict = {}
        for i in range(len(s)):
            if s[i] not in dict.keys():
                if t[i] in dict.values():
                    return False
                dict[s[i]] = t[i]
            else:
                if dict[s[i]] != t[i]:
                    return False
        return True
        
# @lc code=end

