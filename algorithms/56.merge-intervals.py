#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort()
        res = [intervals[0]]
        for x, y in intervals[1:]:
            if res[-1][1] < x:
                res.append([x, y])
            else:
                res[-1][1] = max(y, res[-1][1])
        return res


        
# @lc code=end

