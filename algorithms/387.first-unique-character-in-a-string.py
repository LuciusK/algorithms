#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1 
        unique_chars = [k for k, v in filter(lambda x: x[1] == 1, dic.items())]
        for i, c in enumerate(s):
            if c in unique_chars:
                return i

        return -1
    
    def firstUniqChar1(self, s: str) -> int:
        dic = {c: s.count(c) for c in set(s)}

        for i, c in enumerate(s):
            if dic[c] == 1:
                return i
        
        return -1
        
# @lc code=end

