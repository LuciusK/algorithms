#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans, extra = '', 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0:
            if i >= 0:
                extra += ord(a[i]) - ord('0')
            if j >= 0:
                extra += ord(b[j]) - ord('0')
            ans += str(extra % 2)
            extra //= 2
            i -= 1
            j -= 1
        if extra == 1:
            ans += '1'
        return ans[::-1]
        
# @lc code=end

