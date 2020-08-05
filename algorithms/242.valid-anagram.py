#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        se = set(s)
        if se == set(t):
            for i in se:
                if s.count(i) != t.count(i): return False
            return True
        else:
            return False

    def isAnagram2(self, s: str, t: str) -> bool:
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2

    def isAnagram3(self, s: str, t: str) -> bool:
        dic1, dic2 = [0] * 26, [0] * 26
        for item in s:
            dic1[ord(item) - ord('a')] += 1
        for item in t:
            dic2[ord(item) - ord('a')] += 1
        return dic1 == dic2


# @lc code=end

