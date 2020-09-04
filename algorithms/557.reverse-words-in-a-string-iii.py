#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        return "".join(word[::-1] for word in s.split(" "))
    
    def reverseWords1(self, s: str) -> str:
        stack, res, s = [], "", s + " "
        for i in s:
            stack.append(i)
            if i == " ":
                while stack:
                    res += stack.pop()
        return res[1:]
        
# @lc code=end

