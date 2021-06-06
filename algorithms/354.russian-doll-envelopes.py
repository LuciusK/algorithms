#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#

# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        if n < 2:
            return n
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        tail = [envelopes[0][1]]
        for i in range(n):
            if envelopes[i][1] > tail[-1]:
                tail.append(envelopes[i][1])
                continue
            
            left = 0
            right = len(tail) - 1
            while left < right:
                mid = (left + right) >> 1
                if tail[mid] < envelopes[i][1]:
                    left = mid + 1
                else:
                    right = mid
            tail[left] = envelopes[i][1]
        return len(tail)
            
# @lc code=end

