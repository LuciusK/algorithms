#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                if count == 0:
                    continue
                break
            count += 1
        return count
        
# @lc code=end

