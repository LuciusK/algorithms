#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack

    def isValid1(self, s: str) -> bool:
        while '[]' in s or '()' in s or '{}' in s:
            s = s.replace('[]', '').replace('()', '').replace('{}', '')
        return not len(s)
# @lc code=end

