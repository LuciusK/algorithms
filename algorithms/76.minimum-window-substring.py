#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start, left, right, minLen, match = 0, 0, 0, float('inf'), 0
        window = {}
        needs = dict((i, t.count(i)) for i in t)

        while right < len(s):
            c1 = s[right]
            if c1 in needs.keys():
                window[c1] = window.get(c1, 0) + 1
                if window[c1] == needs[c1]:
                    match += 1
            right += 1

            while match == len(needs):
                if right - left < minLen:
                    start = left
                    minLen = right - left
                c2 = s[left]
                if c2 in needs.keys():
                    window[c2] -= 1
                    if window[c2] < needs[c2]:
                        match -= 1
                left += 1
        return '' if minLen == float('inf') else s[start:start + minLen]

        
# @lc code=end

