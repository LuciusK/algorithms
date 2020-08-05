#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return list(ans.values())

    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for w in strs:
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return list(d.values())

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1 
            ans[tuple(count)].append(s)
        return list(ans.values())


# @lc code=end

