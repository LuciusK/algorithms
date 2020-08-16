#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0 for _ in range(num + 1)]
        for i in range(1, num + 1):
            res[i] = res[i - 1] + 1 if i & 1 == 1 else res[i // 2]
        return res


        
# @lc code=end

