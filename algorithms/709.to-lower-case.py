#
# @lc app=leetcode id=709 lang=python3
#
# [709] To Lower Case
#

# @lc code=start
class Solution:
    def toLowerCase(self, str: str) -> str:
        s = []
        for i in str:
            if 65 <= ord(i) <= 90:
                s.append(chr(ord(i) + 32))
            else:
                s.append(i)
        return ''.join(s)
    
        """
        大写变小写、小写变大写 : 字符 ^= 32;

        大写变小写、小写变小写 : 字符 |= 32;

        小写变大写、大写变大写 : 字符 &= -33;
        """


# @lc code=end

