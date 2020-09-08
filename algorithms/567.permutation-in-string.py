#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        needs = dict((i, s1.count(i)) for i in s1)
        right, left, match = 0, 0, 0
        window = {}

        while right < len(s2):
            c1 = s2[right]
            if c1 in needs.keys():
                window[c1] = window.get(c1, 0) + 1
                if window[c1] == needs[c1]:
                    match += 1
            right += 1

            while match == len(needs):
                if right - left == len(s1):
                    return True
                c2 = s2[left]
                if c2 in needs.keys():
                    window[c2] -= 1
                    if window[c2] < needs[c2]:
                        match -= 1
                left += 1
        return False
        
# @lc code=end

